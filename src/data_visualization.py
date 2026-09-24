import random

frame_width = 1800
frame_height = 900
canvas_width = 1700
canvas_height = 800
heigh_multiplier = 700
min_val = 1
max_val = 400
size = 60
default_speed = 0.01


def generate_data():
    """Generate and draw random data"""

    global data

    data = []
    for _ in range(size):
        data.append(random.randrange(min_val, max_val + 1))

    return data


def get_color_data(data_len, head, tail, border, curr_index, is_swapping=False):
    color_array = []

    for i in range(data_len):
        if i >= head and i <= tail:
            color_array.append("gray")
        else:
            color_array.append("white")

        if i == tail:
            color_array[i] = "blue"
        elif i == border:
            color_array[i] = "red"
        elif i == curr_index:
            color_array[i] = "yellow"

        if is_swapping:
            if i == border or i == curr_index:
                color_array[i] = "green"

    return color_array


def draw_data(data, color_array, canvas, root, anchor_direction):
    canvas.delete("all")
    x_width = canvas_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * heigh_multiplier
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=anchor_direction, text=str(data[i]))

    root.update_idletasks()
