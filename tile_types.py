from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
	[
		("ch", np.int32),
		("fg", "3B"),
		("bg", "3B"),
	]
)

tile_dt = np.dtype(
	[
		("walkable", np.bool),
		("transparent", np.bool),
		("dark", graphic_dt),
		("light", graphic_dt),
	]
)

def new_tile(
	*,
	walkable: int,
	transparent: int,
	dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
	light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
	return np.array((walkable, transparent, dark, light), dtype=tile_dt)

SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

# First set of colors is the graphic, second set is the background

floor = new_tile(
	walkable=True,
	transparent=True,
	dark=(ord("."), (161, 192, 207), (0, 0, 0)), #50,50,150 light blue
	light=(ord("."), (255, 255, 0), (0, 0, 0)), #200,180,50 light yellow
)
wall = new_tile(
	walkable=False,
	transparent=False,
	dark=(ord("#"), (161, 192, 207), (0, 0, 0)), #0,0,100 dark blue
	light=(ord("#"), (255, 255, 0), (0, 0, 0)), # 130, 110, 50 light yellow
)