def create_color(r: int, g: int, b: int) -> int:
    col = 0xFF000000 | (r << 16) | (g << 8) | b
    return col

class Colors:
    WHITE = create_color(255, 255, 255) 
    YELLOW = create_color(255, 255, 51)
    GRAY = create_color(32, 32, 32)
    BLUE = create_color(51, 51, 255)
    RED = create_color(255, 51, 51)
    PINK = create_color(255, 0, 127)
    GREEN = create_color(0, 255, 128)
    ORANGE = create_color(255, 165, 0)
    PURPLE = create_color(204, 0, 204)
