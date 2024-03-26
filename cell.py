from tkinter import Button, Label
import random, settings

class Cell:
    """
    This class creates an instance of a cell.
    """
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label = None
    def __init__(self, x:float, y:float, is_mine:bool = False) -> None:
        self.is_mine = is_mine
        self.button_object = None
        self.is_opened = False
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_button_object(self, Location):
        button = Button(
            Location,
            # text=f"{self.x},{self.y}",
            width=12,
            height=4
        )
        button.bind("<Button-1>",self.left_click_action) # Left Click
        button.bind("<Button-3>",self.right_click_action) # Right Click
        self.button_object = button

    @staticmethod
    def create_cell_count_label(location):
        label  = Label(
            location,
            bg="black",
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            font=("",30)
        )
        Cell.cell_count_label = label

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_length == 0:
                for cell_object in self.surrounded_cells:
                    cell_object.show_cell()
            self.show_cell()
        

    def show_mine(self):
        """
        A logic to interrupt the game and display a message 
        and show that the player lost
        """
        self.button_object.configure(bg="red")

    @property
    def surrounded_cells(self):
        """
        Returns a list of surrounding cells of a selected cell.
        """
        cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
        ]

        cells = [val for val in cells if val is not None]
        return cells

    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter
    
    def show_cell(self):
        """
        This function will show the number of mines surrounding the 
        clicked cell.
        """
        if not self.is_opened:
            Cell.cell_count-=1
            self.button_object.configure(text=self.surrounded_cells_mine_length)
            # Replace the text of Cell count label with the newer count
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text=f'Cells Left: {Cell.cell_count}')
        
        
        # Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True

    def get_cell_by_axis(self, x, y):
        """
        By giving input of x and y, 
        this functions outputs the if there is a cell
        with that particular x and y value.
        """
        # returns a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
        

    def right_click_action(self, event):
        print(event)
        print("I am right clicked")

    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(
            Cell.all, 
            settings.MINES_COUNT
        )
        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y},{self.is_mine})"
    
