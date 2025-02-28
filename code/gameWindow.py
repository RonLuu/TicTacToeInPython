from tkinter import *
from tkinter.ttk import *
WINDOW_SIZE = 600
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

class game_window:
    def __init__(self):
        # Create the window
        self.root = Tk() 
        # Set the title
        self.root.title("My Tic Tac Toe")
        # Set the size
        self.root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
        # Center the window
        center_window(self.root)
        # Set the color
        self.root.configure(background='gray24')
        # Draw the board
        self.draw_board()

        self.root.mainloop()
    
    def draw_board(self):
        self.canvas = Canvas(self.root, bd = 1,highlightthickness=0, bg="gray24",height=WINDOW_SIZE, width=WINDOW_SIZE)
        line_width = 10
        off_set = 20
        distance = (WINDOW_SIZE-2*line_width)//3


        for i in range(1,3):
            self.canvas.create_rectangle(i*distance, 0+off_set, line_width+i*distance, WINDOW_SIZE-off_set,fill='gray69',outline="")
            self.canvas.create_rectangle(0+off_set, i*distance, WINDOW_SIZE-off_set, line_width+i*distance,fill='gray69',outline="")
            

        self.canvas.pack()
        