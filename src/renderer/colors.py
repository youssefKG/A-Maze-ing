def create_color(r, g, b):
    col = 0xFF000000 | (r << 16) | (g << 8) | b
    return col

class Colors:
    WHITE = create_color(255, 255, 255) 
    YELLOW = create_color(255, 255, 51)
    GRAY = create_color(32, 32, 32)
    BLUE = create_color(51, 51, 51)
    RED = create_color(255, 51, 51)
