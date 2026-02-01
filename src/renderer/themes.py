from renderer.colors import Colors


class Theme:
    themes = [
        {
            "border": Colors.WHITE,
            "background": Colors.BLACK,
            "cell_background": Colors.DARK_GRAY,
            "cell_42": Colors.YELLOW,
            "tracker": Colors.CYAN,
            "path": Colors.GREEN,
            "entry_cell": Colors.ORANGE,
            "exit_cell": Colors.RED,
            "neighboor": Colors.PURPLE,
        },

        {
            "border": Colors.GREEN,
            "background": Colors.BLACK,
            "cell_background": Colors.DARK_GREEN,
            "cell_42": Colors.YELLOW,
            "tracker": Colors.BROWN,
            "path": Colors.LIGHT_GRAY,
            "entry_cell": Colors.GREEN,
            "exit_cell": Colors.ORANGE,
            "neighboor": Colors.CYAN,
        },

        {
            "border": Colors.GRAY,
            "background": Colors.WHITE,
            "cell_background": Colors.LIGHT_GRAY,
            "cell_42": Colors.BLUE,
            "tracker": Colors.CYAN,
            "path": Colors.BLUE,
            "entry_cell": Colors.GREEN,
            "exit_cell": Colors.RED,
            "neighboor": Colors.PURPLE,
        },

        {
            "border": Colors.MAGENTA,
            "background": Colors.BLACK,
            "cell_background": Colors.BLACK,
            "cell_42": Colors.YELLOW,
            "tracker": Colors.CYAN,
            "path": Colors.YELLOW,
            "entry_cell": Colors.GREEN,
            "exit_cell": Colors.RED,
            "neighboor": Colors.ORANGE,
        },

        {
            "border": Colors.WHITE,
            "background": Colors.BLACK,
            "cell_background": Colors.DARK_BLUE,
            "cell_42": Colors.WHITE,
            "tracker": Colors.CYAN,
            "path": Colors.GREEN,
            "entry_cell": Colors.BLUE,
            "exit_cell": Colors.RED,
            "neighboor": Colors.PURPLE,
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

