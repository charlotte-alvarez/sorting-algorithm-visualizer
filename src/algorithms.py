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


def insertionSort(data, time_tick, canvas, root, anchor_direction):
    length = len(data)

    if length <= 1:
        draw_data(
            data, ["green" for x in range(length)], canvas, root, anchor_direction
        )
    for i in range(1, length):
        k = data[i]
        j = i - 1
        while j >= 0 and k < data[j]:
            data[j + 1] = data[j]
            draw_data(
                data,
                get_color_data(length, 0, len(data) - 1, j, j + 1, True),
                canvas,
                root,
                anchor_direction,
            )
            time.sleep(time_tick)
            j -= 1
        data[j + 1] = k
        draw_data(
            data,
            get_color_data(length, 0, len(data) - 1, j, j + 1, True),
            canvas,
            root,
            anchor_direction,
        )
        time.sleep(time_tick)


def merge(data, l, m, r, time_tick, canvas, root, anchor_direction):
    length = len(data)
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = data[l + i]
    for j in range(n2):
        R[j] = data[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            draw_data(
                data,
                get_color_data(length, 0, length - 1, j, j + 1, True),
                canvas,
                root,
                anchor_direction,
            )
            time.sleep(time_tick)
            i += 1
        else:
            data[k] = R[j]
            draw_data(
                data,
                get_color_data(length, 0, length - 1, j, j + 1, True),
                canvas,
                root,
                anchor_direction,
            )
            time.sleep(time_tick)
            j += 1
        k += 1

    while i < n1:
        data[k] = L[i]
        draw_data(
            data,
            get_color_data(length, 0, length - 1, j, j + 1, True),
            canvas,
            root,
            anchor_direction,
        )
        time.sleep(time_tick)
        i += 1
        k += 1
    while j < n2:
        data[k] = R[j]
        draw_data(
            data,
            get_color_data(length, 0, length - 1, j, j + 1, True),
            canvas,
            root,
            anchor_direction,
        )
        time.sleep(time_tick)
        j += 1
        k += 1


def merge_sort(data, l, r, time_tick, canvas, root, anchor_direction):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(
            data,
            l,
            m,
            time_tick=time_tick,
            canvas=canvas,
            root=root,
            anchor_direction=anchor_direction,
        )
        merge_sort(
            data,
            m + 1,
            r,
            time_tick=time_tick,
            canvas=canvas,
            root=root,
            anchor_direction=anchor_direction,
        )
        merge(
            data,
            l,
            m,
            r,
            time_tick=time_tick,
            canvas=canvas,
            root=root,
            anchor_direction=anchor_direction,
        )
