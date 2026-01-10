from mlx.mlx import Mlx
from renderer import renderer
from renderer.renderer import Renderer

class Amazeing:
    def __init__(self) -> None:
        self.mlx = Mlx()
        self.mlx_ptr = self.mlx.mlx_init()
        self.renderer = Renderer(self.mlx, self.mlx_ptr)

def main():
    amazeing = Amazeing()
    amazeing.renderer.render()

if __name__ == "__main__":
    main()
