"""Algorithms"""

from data_visualization import draw_data
import time
from data_visualization import get_color_data


def bubble_sort(data, time_tick, canvas, root, anchor_direction):
    length = len(data)
    for i in range(length):
        for j in range(length - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(
                    data,
                    get_color_data(length, 0, len(data) - 1, j, j + 1, True),
                    canvas,
                    root,
                    anchor_direction,
                )
                time.sleep(time_tick)
    draw_data(data, ["green" for x in range(length)], canvas, root, anchor_direction)


def selection_sort(data, time_tick, canvas, root, anchor_direction):
    length = len(data)
    for i in range(length - 1):
        min_index = i

        for j in range(i + 1, length):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
        draw_data(
            data,
            get_color_data(length, 0, len(data) - 1, j, j + 1, True),
            canvas,
            root,
            anchor_direction,
        )
        time.sleep(time_tick)
    draw_data(data, ["green" for x in range(length)], canvas, root, anchor_direction)
