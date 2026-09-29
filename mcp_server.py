import sys
import json
from client import ASCIITerminalRasterizer

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-ascii-art-visual-terminal-rasterizer-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "render_ascii_matrix",
                        "description": "Renders a 2D integer matrix (0-255) as ASCII art for CLI agent terminals",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "matrix": {"type": "array", "items": {"type": "array", "items": {"type": "integer"}}},
                                "invert": {"type": "boolean", "default": False}
                            },
                            "required": ["matrix"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})
        
        if name == "render_ascii_matrix":
            res = ASCIITerminalRasterizer.rasterize_matrix(args.get("matrix", []), args.get("invert", False))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": res}]}}
            
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def run():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    run()
