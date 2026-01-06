# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a_maze_ing.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ytaoussi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 04:41:27 by ytaoussi          #+#    #+#              #
#    Updated: 2026/01/03 04:41:44 by ytaoussi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mlx.mlx import Mlx

if __name__ == "__main__":
    m = Mlx()
    mlx_ptr = m.mlx_init()
    win_ptr = m.mlx_new_window(mlx_ptr, 400, 400, "win title")
    m.mlx_clear_window(mlx_ptr, win_ptr)
    m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Hello PyMlx!")
    m.mlx_loop(mlx_ptr)
