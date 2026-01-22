from mlx.mlx.mlx import Mlx
from my_mlx.my_mlx import MyMlx
from controll_pannel.controll_pannel import ControllPannel

class Renderer:
    def __init__(self):
        self.controll_pannel = ControllPannel()
        self.controll_pannel.draw()
    def render(self):
        MyMlx.loop()
