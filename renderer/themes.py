"""Color themes and background images used when rendering the maze."""

from renderer.colors import Colors
from renderer.images.background.background_img import BackgroundImg
from typing import Any


class ColorScheme:
    """Fluent builder for a single color theme configuration."""

    def set_border(self, border: int) -> Any:
        """Set the color for maze borders and return ``self``."""
        self.border = border
        return self

    def set_background(self, background: int) -> Any:
        """Set the background color and return ``self``."""
        self.background = background
        return self

    def set_cell_background(self, cell_background: int) -> Any:
        """Set the color used to fill cell interiors and return ``self``."""
        self.cell_background = cell_background
        return self

    def set_cell_42(self, cell_42: int) -> Any:
        """Set the color for the decorative “42” cells and return ``self``."""
        self.cell_42 = cell_42
        return self

    def set_tracker(self, tracker: int) -> Any:
        """
        Set the tracker color (used for animated cursors) and return
        ``self``.
        """
        self.tracker = tracker
        return self

    def set_path(self, path: int) -> Any:
        """Set the solver path color and return ``self``."""
        self.path = path
        return self

    def set_exit_cell(self, exit_cell: int) -> Any:
        """Set the exit cell highlight color and return ``self``."""
        self.exit_cell = exit_cell
        return self

    def set_entry_cell(self, entry_cell: int) -> Any:
        """Set the entry cell highlight color and return ``self``."""
        self.entry_cell = entry_cell
        return self

    def set_neighboor(self, neighboor: int) -> Any:
        """Set the neighbor-highlight color and return ``self``."""
        self.neighboor = neighboor
        return self

    def set_background_img(self, filename: str, image_type: str) -> Any:
        """Attach a background image and return ``self``."""
        self.background_img = BackgroundImg(filename, image_type)
        return self


class Theme:
    """Global theme manager cycling between predefined color schemes."""

    themes = [
        ColorScheme()
        .set_border(Colors.MAGENTA)
        .set_background(Colors.BLACK)
        .set_cell_background(Colors.BLACK)
        .set_cell_42(Colors.YELLOW)
        .set_tracker(Colors.CYAN)
        .set_path(Colors.CYAN)
        .set_exit_cell(Colors.BLUE)
        .set_entry_cell(Colors.RED)
        .set_neighboor(Colors.ORANGE)
        .set_background_img("pink_back.png", "png"),
        ColorScheme()
        .set_border(Colors.GREEN)
        .set_background(Colors.BLACK)
        .set_cell_background(Colors.DARK_BLUE)
        .set_cell_42(Colors.BLUE)
        .set_tracker(Colors.BLUE)
        .set_path(Colors.PURPLE)
        .set_exit_cell(Colors.BLUE)
        .set_entry_cell(Colors.RED)
        .set_neighboor(Colors.BLUE)
        .set_background_img("green_back.png", "png"),
        ColorScheme()
        .set_border(Colors.ORANGE)
        .set_background(Colors.BLACK)
        .set_cell_background(Colors.DARK_GRAY)
        .set_cell_42(Colors.RED)
        .set_tracker(Colors.CYAN)
        .set_path(Colors.CYAN)
        .set_exit_cell(Colors.RED)
        .set_entry_cell(Colors.YELLOW)
        .set_neighboor(Colors.CYAN)
        .set_background_img("orange_back.png", "png"),
        ColorScheme()
        .set_border(Colors.GREEN)
        .set_background(Colors.BLACK)
        .set_cell_background(Colors.DARK_GREEN)
        .set_cell_42(Colors.BLUE)
        .set_tracker(Colors.BROWN)
        .set_path(Colors.LIGHT_GRAY)
        .set_exit_cell(Colors.WHITE)
        .set_entry_cell(Colors.RED)
        .set_neighboor(Colors.WHITE)
        .set_background_img("background_img.xpm", "xpm"),
    ]

    __current_index = 0
    current = themes[__current_index]

    border = current.border
    background = current.background
    cell_background = current.cell_background
    tracker = current.tracker
    path = current.path
    neighboor = current.neighboor
    entry_cell = current.entry_cell
    exit_cell = current.exit_cell
    cell_42 = current.cell_42
    background_img = current.background_img

    @classmethod
    def change(cls) -> None:
        """Switch to the next color scheme in the theme list."""
        cls.__current_index = (cls.__current_index + 1) % len(cls.themes)
        t = cls.themes[cls.__current_index]
        cls.border = t.border
        cls.background = t.background
        cls.cell_background = t.cell_background
        cls.tracker = t.tracker
        cls.path = t.path
        cls.neighboor = t.neighboor
        cls.entry_cell = t.entry_cell
        cls.exit_cell = t.exit_cell
        cls.cell_42 = t.cell_42
        cls.background_img = t.background_img
