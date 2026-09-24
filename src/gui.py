from tkinter import ttk, Tk, N, W, E, S, StringVar, Button, Canvas, SW


from algorithms import bubble_sort
from data_visualization import (
    generate_data,
    draw_data,
    canvas_height,
    canvas_width,
    speed,
)

# Set up the main application window & it's frame widget
root = Tk()
root.title("Sorting Algorithm Visualizer - by Char :3")
root.config(bg="black")
mainframe = ttk.Frame(root, width=1920, height=1080, padding=(3, 3, 12, 12))

# Insert the frame into the user interface
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Set up the canvas
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# Set up the algorithm selection
ttk.Label(mainframe, text="Algorithm: ", background="grey").grid(
    row=0, column=0, padx=5, pady=5, sticky=W
)
algorithm_var = StringVar()
algorithm_menu = ttk.Combobox(
    mainframe, textvariable=algorithm_var, background="grey", values=["Bubble Sort"]
)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)


def start_algorithm():
    data = generate_data()
    algo = algorithm_menu.get()
    if algo == "Bubble Sort":
        print("bubble sort")
        bubble_sort(data, speed, canvas, root, SW)
    draw_data(data, ["green" for x in range(len(data))], canvas, root, SW)


def generate():
    data = generate_data()
    draw_data(data, ["red" for x in range(len(data))], canvas, root, SW)


Button(mainframe, text="START", command=start_algorithm, bg="red").grid(
    row=0, column=3, padx=5, pady=5
)

root.mainloop()
