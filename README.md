# genpark-ascii-art-visual-terminal-rasterizer-skill

A 10-level grayscale ASCII rasterizer designed for autonomous CLI agents to visualize spatial matrices, attention maps, and low-resolution image buffers directly inside terminal logs.

## Architecture

```mermaid
flowchart LR
    Grid[Pixel/Attention Grid] --> Quantizer[10-Level Grayscale Quantizer]
    Quantizer --> Mapper[ASCII Glyph Character Map]
    Mapper --> TerminalText[Terminal Visual Output]
```

## Features
- **10 Grayscale Glyphs**: High readability across light and dark terminals.
- **Heatmap Generator**: Generates distance-falloff visual density representations.
