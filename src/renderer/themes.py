from renderer.colors import Colors

class Theme:
    themes =[
        dict({ 
            "cell_background": Colors.GRAY,
            "background": Colors.RED,
            "border": Colors.WHITE,
            "cell_42": Colors.YELLOW,
            "tracker": Colors.GRAY,
            "path": Colors.GREEN,
            "entry_cell": Colors.ORANGE,
            "exit_cell": Colors.PINK,
            "neighboor": Colors.PURPLE,
        }),
        dict({ 
            "cell_background": Colors.GRAY,
            "background": Colors.GRAY,
            "border": Colors.WHITE,
            "cell_42": Colors.WHITE,
            "tracker": Colors.ORANGE,
            "path": Colors.PURPLE,
            "entry_cell": Colors.GREEN,
            "exit_cell": Colors.PINK,
            "neighboor": Colors.PURPLE,
        }),
    ]

    __current_index = 0
    current = themes[__current_index]
    border = themes[__current_index]["border"]
    background = themes[__current_index]["background"]
    cell_background = themes[__current_index]["cell_background"]
    tracker = themes[__current_index]["tracker"]
    path = themes[__current_index]["path"]
    neighboor = themes[__current_index]["neighboor"]
    entry_cell = themes[__current_index]["entry_cell"]
    exit_cell = themes[__current_index]["entry_cell"]
    cell_42 = themes[__current_index]["cell_42"]

    @classmethod
    def change(cls):
        if (cls.__current_index + 1 < len(cls.themes)):
            cls.__current_index += 1
        else:
            cls.__current_index = 0
        current_theme = cls.themes[cls.__current_index]
        cls.border = current_theme["border"]
        cls.background = current_theme["background"]
        cls.cell_background = current_theme["cell_background"]
        cls.tracker = current_theme["tracker"]
        cls.path = current_theme["path"]
        cls.cell_42 = current_theme["cell_42"]
        cls.neighboor = current_theme["neighboor"]
        cls.entry_cell = current_theme["entry_cell"]
        cls.exit_cell = current_theme["exit_cell"]
