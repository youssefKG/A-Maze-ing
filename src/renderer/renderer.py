from mlx.mlx.mlx import Mlx
from my_mlx.my_mlx import MyMlx
from controll_pannel.controll_pannel import ControllPannel

class Renderer:
    def __init__(self):
        self.controll_pannel = ControllPannel()
        
    def render(self):
        MyMlx.loop()
        self.controll_pannel.draw()
