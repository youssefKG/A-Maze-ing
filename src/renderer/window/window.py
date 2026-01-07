from mlx.mlx.mlx import Mlx

class Window:
    def __init__(self, mlx: Mlx, mlx_ptr, width: int, height: int, title: str) -> None: 
        self.mlx = mlx
        self.widht = width
        self.height = height
        self.title = title
        self.win_ptr = self.mlx.mlx_new_window(mlx_ptr, self.widht, self.height, self.title)
        self.mlx_ptr = mlx_ptr
        self.mlx.mlx_key_hook(self.win_ptr, self.mykey, [1, 2])
        self.mlx.mlx_hook(self.win_ptr, 30, 0, self.gere_close, None)


    def mykey(self, keynum, mystuff):
        print(f"Got key {keynum}, and got my stuff back:")
        print(mystuff)
        if keynum == 32:
            self.mlx.mlx_mouse_hook(self.win_ptr, None, None)
        if keynum == 65307:
            self.mlx.mlx_loop_exit(self.mlx_ptr)

    def gere_close(self, dummy):
        self.mlx.mlx_loop_exit(self.mlx_ptr)
