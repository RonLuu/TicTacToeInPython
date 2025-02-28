from tkinter import *
from tkinter.ttk import *
WINDOW_SIZE = 600
CIRCLE_IMAGE_PATH = "resource/Circle.png"
CROSS_IMAGE_PATH = "resource/Cross.png"
LINE_WIDTH = 10
DISTANCE = (WINDOW_SIZE-2*LINE_WIDTH)//3 # Distance between each line
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def printCoordinate(event):
    print(f"{str(event.x)},{str(event.y)}")


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
        # Create a canvas
        self.canvas = Canvas(self.root, bd = 1,highlightthickness=0, bg="gray24",
                             height=WINDOW_SIZE, width=WINDOW_SIZE)
        self.canvas.pack()

        # Draw the board
        self.shape_list = []
        self.draw_shape(CIRCLE_IMAGE_PATH)
        self.draw_shape(CROSS_IMAGE_PATH)
        self.draw_shape(CIRCLE_IMAGE_PATH, 2, 1)
        self.draw_board()
        self.canvas.pack()
        
        self.root.bind("<Button-1>", printCoordinate)
        
        self.root.mainloop()

    def draw_board(self):
        off_set = 20
        for i in range(1,3):
            self.canvas.create_rectangle(i*DISTANCE, 0+off_set, 
                                         LINE_WIDTH+i*DISTANCE, WINDOW_SIZE-off_set,
                                         fill='gray69',outline="")
            self.canvas.create_rectangle(0+off_set, i*DISTANCE, 
                                         WINDOW_SIZE-off_set, LINE_WIDTH+i*DISTANCE,
                                         fill='gray69',outline="")

    def draw_shape(self, filepath, x=0, y=0):        
        self.shape_list.append(PhotoImage(file= filepath).subsample(20))
        off_set = 10
        x_distance = 2*x*(DISTANCE//2)+(off_set) + (DISTANCE//2) 
        y_distance = 2*y*(DISTANCE//2)+(off_set) + (DISTANCE//2) 
        print(f"{x_distance}, {y_distance}")
        self.canvas.create_image(x_distance,y_distance, image=self.shape_list[-1])