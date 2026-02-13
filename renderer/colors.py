"""Color utilities and predefined ARGB color constants for rendering."""


def create_color(r: int, g: int, b: int) -> int:
    """Create a 32-bit ARGB color value from RGB components."""
    col = 0xFF000000 | (r << 16) | (g << 8) | b
    return col


class Colors:
    """Collection of commonly used color constants."""

    WHITE = create_color(255, 255, 255)
    BLACK = create_color(0, 0, 0)

    GRAY = create_color(32, 32, 32)
    LIGHT_GRAY = create_color(192, 192, 192)
    DARK_GRAY = create_color(64, 64, 64)

    RED = create_color(255, 51, 51)
    DARK_RED = create_color(139, 0, 0)

    GREEN = create_color(0, 255, 128)
    DARK_GREEN = create_color(0, 128, 0)

    BLUE = create_color(51, 51, 255)
    DARK_BLUE = create_color(0, 0, 139)

    YELLOW = create_color(255, 255, 51)
    ORANGE = create_color(255, 165, 0)

    PINK = create_color(255, 0, 127)
    PURPLE = create_color(204, 0, 204)

    CYAN = create_color(0, 255, 255)
    MAGENTA = create_color(255, 0, 255)
    BROWN = create_color(139, 69, 19)
