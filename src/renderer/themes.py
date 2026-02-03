from renderer.colors import Colors
from renderer.images.background.background_img import BackgroundImg


class Theme:
    themes = [
        {
            "border": Colors.MAGENTA,
            "background": Colors.BLACK,
            "cell_background": Colors.BLACK,
            "cell_42": Colors.YELLOW,
            "tracker": Colors.CYAN,
            "path": Colors.CYAN,
            "entry_cell": Colors.GREEN,
            "exit_cell": Colors.RED,
            "neighboor": Colors.ORANGE,
            "background_img": BackgroundImg("background.xpm", "xpm")
        },
        {
            "border": Colors.GREEN,
            "background": Colors.BLACK,
            "cell_background": Colors.DARK_BLUE,
            "cell_42": Colors.YELLOW,
            "tracker": Colors.BLUE,
            "path": Colors.YELLOW,
            "entry_cell": Colors.BLUE,
            "exit_cell": Colors.RED,
            "neighboor": Colors.PURPLE,
            "background_img": BackgroundImg("green_background.xpm", "xpm")
        },
        {
            "border": Colors.ORANGE,
            "background": Colors.BLACK,
            "cell_background": Colors.DARK_GRAY,
            "cell_42": Colors.RED,
            "tracker": Colors.CYAN,
            "path": Colors.CYAN,
            "entry_cell": Colors.ORANGE,
            "exit_cell": Colors.RED,
            "neighboor": Colors.CYAN,
            "background_img": BackgroundImg("orange_background.xpm", "xpm")
        },

        {
            "border": Colors.GREEN,
            "background": Colors.BLACK,
            "cell_background": Colors.DARK_GREEN,
            "cell_42": Colors.BLUE,
            "tracker": Colors.BROWN,
            "path": Colors.LIGHT_GRAY,
            "entry_cell": Colors.GREEN,
            "exit_cell": Colors.ORANGE,
            "neighboor": Colors.CYAN,
            "background_img": BackgroundImg("background.xpm", "xpm")
        },
    ]

    __current_index = 0
    current = themes[__current_index]

    border = current["border"]
    background = current["background"]
    cell_background = current["cell_background"]
    tracker = current["tracker"]
    path = current["path"]
    neighboor = current["neighboor"]
    entry_cell = current["entry_cell"]
    exit_cell = current["exit_cell"]
    cell_42 = current["cell_42"]
    background_img = current["background_img"]

    @classmethod
    def change(cls):
        cls.__current_index = (cls.__current_index + 1) % len(cls.themes)
        t = cls.themes[cls.__current_index]
        cls.border = t["border"]
        cls.background = t["background"]
        cls.cell_background = t["cell_background"]
        cls.tracker = t["tracker"]
        cls.path = t["path"]
        cls.neighboor = t["neighboor"]
        cls.entry_cell = t["entry_cell"]
        cls.exit_cell = t["exit_cell"]
        cls.cell_42 = t["cell_42"]
        cls.background_img = t["background_img"]

