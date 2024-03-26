from tkinter import *
from cell import Cell
import settings, utils


root = Tk()
# Override the settings of the window
root.configure(bg='black')
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")  # the size of the window
root.title("Shyam's Window") # Name of the window
root.resizable(width=False,height=False) # the flexibility to change the size of the window

top_frame = Frame(
    root,
    background='black', # You can change it later to the colour that you want
    width=f'{settings.WIDTH}',
    height=f'{utils.param_percent(25,settings.HEIGHT)}',
)
top_frame.place(x=0,y=0.0)

left_frame = Frame(
    root,
    background='red', # You can change it later to the colour that you want
    width=f'{utils.param_percent(25,settings.WIDTH)}',
    height=f'{utils.param_percent(75,settings.HEIGHT)}',
)
left_frame.place(x=0,y=utils.param_percent(25,settings.HEIGHT))

centre_frame = Frame(
    root,
    background='blue', # You can change it later to the colour that you want
    width=f'{utils.param_percent(75,settings.WIDTH)}',
    height=f'{utils.param_percent(75,settings.HEIGHT)}',
)
centre_frame.place(x=utils.param_percent(25,settings.WIDTH),y=utils.param_percent(25,settings.HEIGHT))

for row in range(settings.GRID_SIZE):
    for column in range(settings.GRID_SIZE):
        c = Cell(row,column)
        c.create_button_object(centre_frame)
        c.button_object.grid(
            column=column, row=row
        )

Cell.randomise_mines()

## Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(
    x=0,
    y=0
)

# Run the window
root.mainloop()