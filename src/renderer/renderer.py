from my_mlx.my_mlx import MyMlx
from controll_pannel.controll_pannel import ControllPannel


class Renderer:
    def __init__(self) -> None:
        self.controll_pannel = ControllPannel()

    def render(self) -> None:
        MyMlx.loop()
