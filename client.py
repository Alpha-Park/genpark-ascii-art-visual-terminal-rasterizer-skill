"""ASCII Art Visual Terminal Rasterizer.
100% Python Standard Library.
"""

import math

class ASCIITerminalRasterizer:
    """Rasterizes grayscale pixel arrays into ASCII terminal representations."""
    ASCII_CHARS = " .:-=+*#%@"

    @classmethod
    def rasterize_matrix(cls, matrix: list, invert=False) -> str:
        chars = cls.ASCII_CHARS[::-1] if invert else cls.ASCII_CHARS
        num_chars = len(chars)
        lines = []
        for row in matrix:
            line_chars = []
            for val in row:
                idx = int((val / 255.0) * (num_chars - 1))
                idx = max(0, min(num_chars - 1, idx))
                line_chars.append(chars[idx])
            lines.append("".join(line_chars))
        return "\n".join(lines)

    @classmethod
    def generate_heatmap(cls, width: int, height: int, hot_spots: list) -> str:
        matrix = [[0 for _ in range(width)] for _ in range(height)]
        for y in range(height):
            for x in range(width):
                val = 0.0
                for spot in hot_spots:
                    dist = math.sqrt((x - spot["x"])**2 + (y - spot["y"])**2)
                    if dist <= spot["radius"]:
                        falloff = max(0.0, 1.0 - (dist / spot["radius"]))
                        val += spot["intensity"] * falloff
                matrix[y][x] = min(255, int(val * 255))
        return cls.rasterize_matrix(matrix)
