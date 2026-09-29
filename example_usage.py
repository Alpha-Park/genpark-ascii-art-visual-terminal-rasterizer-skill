from client import ASCIITerminalRasterizer

matrix = [[0, 50, 100, 150, 200, 255]]
print("ASCII Gradient:\n" + ASCIITerminalRasterizer.rasterize_matrix(matrix))
