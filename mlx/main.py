from mlx.mlx import Mlx

mlx = Mlx()
mlx_ptr = mlx.mlx_init()
win_ptr = mlx.mlx_new_window(mlx_ptr, 2000, 2000, "title")
cell_width = 200
cell_height = 200
border_width = int(cell_width * 0.2)
border_height = int(cell_height * 0.2)
image_ptr = mlx.mlx_new_image(mlx_ptr, 1000, 1000)
(image_data, bpp, sl, format_value) = mlx.mlx_get_data_addr(image_ptr)

print(image_data, bpp, sl, format_value)

"""

# north wall
for y in range(border_width):
    for x in range(cell_width):
        mlx.mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0xFFFF0000)
# west wall
for y in range(border_width, cell_height):
    for x in range(border_width):
        mlx.mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0xFFFF0000)

# east wall
for y in range(border_width, cell_height):
    for x in range(cell_width - border_width, cell_width):
        mlx.mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0xFFFF0000)

# south wall
for y in range(cell_height - border_height, cell_height):
    for x in range(border_width, cell_width - border_width):
        mlx.mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0xFFFF0000)
# cell content
for y in range(border_width, cell_height - border_height):
    for x in range(border_width, cell_width - border_width):
        mlx.mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0xFFFFFFFF)
print(mlx_ptr)
"""
mlx.mlx_loop(mlx_ptr)
