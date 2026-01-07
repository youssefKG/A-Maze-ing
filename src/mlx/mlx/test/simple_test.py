from mlx import Mlx

def mymouse(button, x, y, mystuff):
    print(f"Got mouse event! button {button} at {x},{y}.")

def mykey(keynum, mystuff):
    print(f"Got key {keynum}, and got my stuff back:")
    print(mystuff)
    if keynum == 32:
        m.mlx_mouse_hook(win_ptr, None, None)

def gere_close(dummy):
    m.mlx_loop_exit(mlx_ptr)
    
class CellImage:
    def __init__(self, mlx: Mlx, mlx_ptr, cell: Cell ) -> None:
        self.mlx = mlx
        self.mlx_ptr =  mlx_ptr
        self.cell = cell
        self.ptr = self.mlx.mlx_new_image(self.mlx_ptr, self.cell.width, self.cell.height)
        (self.data, self.bpp, self.sl, self.format) = self.mlx.mlx_get_data_addr(self.ptr)

        for offset in range(0, self.sl * self.cell.width, 4):
            self.data[offset:offset+4] = (0xFFFF0000).to_bytes(4, 'little')

class CellWalls:
    def __init__(self, north, south, east, west) -> None:
        self.north = north
        self.south = south
        self.east = east
        self.west = west

class Cell:
    def __init__(self, width: int, height: int, walls: CellWalls) -> None:
        self.width = width
        self.height =height
        self.walls  = walls
m = Mlx()
mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, 200, 200, "win title")
m.mlx_clear_window(mlx_ptr, win_ptr)
m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Hello PyMlx!")
(ret, w, h) = m.mlx_get_screen_size(mlx_ptr)
print(f"Got screen size: {w} x {h} .")

cell = Cell(20, 20, cellWall)
cellImg = CellImage(self.mlx, self.mlx_ptr, cell)
self.mlx.mlx_put_image_to_window(mlx_ptr, wind_ptr, cellImg.ptr, 10, 10)

stuff = [1, 2]
m.mlx_mouse_hook(win_ptr, mymouse, None)
m.mlx_key_hook(win_ptr, mykey, stuff)
m.mlx_hook(win_ptr, 33, 0, gere_close, None)

m.mlx_loop(mlx_ptr)
