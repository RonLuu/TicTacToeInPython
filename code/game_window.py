from tkinter import *
from tkinter.ttk import *
WINDOW_SIZE = 600
CIRCLE_IMAGE_PATH = "resource/Circle.png"
CROSS_IMAGE_PATH = "resource/Cross.png"
GRAYED_CIRCLE_IMAGE_PATH = "resource/Circle_grayed.png"
GRAYED_CROSS_IMAGE_PATH = "resource/Cross_grayed.png"
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

class GameWindow:
    def __init__(self, gameLogic):
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
        
        # Create a canvas to draw on
        self.canvas = Canvas(self.root, bd = 1,highlightthickness=0, bg="gray24",
                             height=WINDOW_SIZE, width=WINDOW_SIZE)
        self.canvas.pack()
        
        # Initialise the image and character
        self.current_image_path = CROSS_IMAGE_PATH
        self.current_grayed_image_path = GRAYED_CROSS_IMAGE_PATH
        self.current_char = "X"
        self.current_move = ()

        # Store all the images
        self.shape_list = []
        
        # Get the reference of the logic
        self.gameLogic = gameLogic

        # Get the turn
        self.turn = True # True for the first player
        # Draw the board
        self.draw_board()
        
        # Get the user input
        
        # self.detect_hover()
        self.click()
        
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

    # Track the user movement
    def detect_hover(self):
        self.root.bind("<Motion>", self.draw_grayed_shape)

    # Draw the highlight of the current shape
    def draw_grayed_shape(self, event):        
        self.grayed_shape = PhotoImage(file= self.current_grayed_image_path).subsample(20)

        x = event.x//DISTANCE
        y = event.y//DISTANCE

        off_set = 10
        x_distance = 2*x*(DISTANCE//2)+(off_set) + (DISTANCE//2) 
        y_distance = 2*y*(DISTANCE//2)+(off_set) + (DISTANCE//2) 
        
        self.canvas.create_image(x_distance,y_distance, image=self.grayed_shape)

    # Track the user's click
    def click(self):
        self.root.bind("<Button-1>", self.get_coordinate)

    # Get the coordinate of where the user click
    def get_coordinate(self, event):
        x = event.x//DISTANCE
        y = event.y//DISTANCE
        self.current_move = (x,y)

        result = self.gameLogic.move(self.current_char, self.current_move)

        if result != "illegal":
            self.draw_shape(self.current_move[0],self.current_move[1])
            self.swap_turn()
        if result == "win":
            print("X wins")
            self.root.unbind("<Button-1>")
        if result == "lose":
            print("X loses")
            self.root.unbind("<Button-1>")
            
        if result == "draw":
            print("It's a draw")
            self.root.unbind("<Button-1>")


    def draw_shape(self, x, y):        
        self.shape_list.append(PhotoImage(file= self.current_image_path).subsample(20))
        off_set = 10
        x_distance = 2*x*(DISTANCE//2)+(off_set) + (DISTANCE//2) 
        y_distance = 2*y*(DISTANCE//2)+(off_set) + (DISTANCE//2) 
        self.canvas.create_image(x_distance,y_distance, image=self.shape_list[-1])
        
    def swap_turn(self):
        if self.turn:
            self.current_image_path = CIRCLE_IMAGE_PATH
            self.current_grayed_image_path = GRAYED_CIRCLE_IMAGE_PATH
            self.current_char = "O"
            self.turn = False
        else:
            self.current_image_path = CROSS_IMAGE_PATH
            self.current_grayed_image_path = GRAYED_CROSS_IMAGE_PATH
            self.current_char = "X"
            self.turn = True
