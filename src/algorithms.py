"""Algorithms"""

from data_visualization import draw_data
import time
from data_visualization import get_color_array


def bubble_sort(data, time_tick, canvas, root, anchor_direction):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(
                    data,
                    get_color_array(len(data), 0, len(data) - 1, j, j + 1, True),
                    canvas,
                    root,
                    anchor_direction,
                )
                time.sleep(time_tick)
    draw_data(data, ["green" for x in range(len(data))], canvas, root, anchor_direction)
