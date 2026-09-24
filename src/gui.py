from tkinter import ttk, Tk, N, W, E, S, StringVar, Button, Canvas, SW


from algorithms import bubble_sort, selection_sort, insertionSort, merge_sort, heap_sort
from data_visualization import (
    generate_data,
    draw_data,
    canvas_height,
    canvas_width,
    default_speed,
    frame_height,
    frame_width,
)


algorithm_list = [
    "Bubble Sort",
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Heap Sort",
]

# Set up the main application window & it's frame widget
root = Tk()
root.title("Sorting Algorithm Visualizer - by Char :3")
root.config(bg="black")
mainframe = ttk.Frame(
    root, width=frame_width, height=frame_height, padding=(3, 3, 12, 12)
)

# Insert the frame into the user interface
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Set up the canvas
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.grid(row=1, column=0, padx=10, pady=5)

# Set up the algorithm selection
ttk.Label(mainframe, text="Algorithm: ", background="grey").grid(
    row=0, column=0, padx=5, pady=5, sticky=W
)
algorithm_var = StringVar()
algorithm_menu = ttk.Combobox(
    mainframe, textvariable=algorithm_var, background="grey", values=algorithm_list
)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)


# Set up speed
speed = default_speed
sp = StringVar()
label = ttk.Label(root)
label.grid(row=0, column=8, padx=5, pady=5, sticky="we")


def update_speed(val):
    print(f"updating speed to {val}")
    label["text"] = f"Speed: {speed}"


scale = ttk.Scale(
    mainframe,
    orient="horizontal",
    length=200,
    from_=0.001,
    to=0.05,
    variable=sp,
    command=update_speed,
)
scale.grid(row=0, column=9, padx=5, pady=5)
scale.set(default_speed)


def start_algorithm():
    speed = scale.get()
    print(f"speed on start is {speed}")
    data = generate_data()
    algo = algorithm_menu.get()
    match algo:
        case "Bubble Sort":
            bubble_sort(data, float(speed), canvas, root, SW)
        case "Selection Sort":
            selection_sort(data, float(speed), canvas, root, SW)
        case "Insertion Sort":
            insertionSort(data, float(speed), canvas, root, SW)
        case "Merge Sort":
            merge_sort(data, 0, len(data) - 1, float(speed), canvas, root, SW)
        case "Heap Sort":
            heap_sort(data, float(speed), canvas, root, SW)

    draw_data(data, ["green" for x in range(len(data))], canvas, root, SW)


Button(mainframe, text="START", command=start_algorithm, bg="red").grid(
    row=0, column=3, padx=5, pady=5
)

root.mainloop()
