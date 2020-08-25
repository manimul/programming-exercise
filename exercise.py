from numpy import * 
from array import *
from tkinter import *
from time import time 


# The Simulation Object - this is the shape that must sit on the table
class SimObject :
    def __init__(self) :
        self.all_directions = ["n","e","s","w"]
        self.direction="n"
        self.location=[]
        self.direction_mod = 0
    
    # Function for moving the object based on the instruction commands
    def movement(self,dir) :
        
        if dir == "forward":

            if self.direction == "n": 
                self.location[1] -= 1
                drawing_object.canvas.move(drawing_object.sprite, 0, -100)
                
            elif self.direction == "e": 
                self.location[0] += 1
                drawing_object.canvas.move(drawing_object.sprite, 100, 0)

                
            elif self.direction == "s": 
                self.location[1] += 1 
                drawing_object.canvas.move(drawing_object.sprite, 0, 100)
                
            else:
                self.location[0] -= 1 
                drawing_object.canvas.move(drawing_object.sprite, -100, 0)
                

        else: 
            if self.direction == "n": 
                self.location[1] += 1
                drawing_object.canvas.move(drawing_object.sprite, 0, 100)

                
            elif self.direction == "e": 
                self.location[0] -= 1
                drawing_object.canvas.move(drawing_object.sprite, -100, 0)

                
            elif self.direction == "s": 
                self.location[1] -= 1
                drawing_object.canvas.move(drawing_object.sprite, 0, -100)

              
            else:
                self.location[0] += 1
                drawing_object.canvas.move(drawing_object.sprite, 100, 0)
                
        drawing_object.window.update()

        return
    # Function for changing the objects direction based on instruction commands   
    def change_direction(self,value) :
        self.direction_mod  += value
        if self.direction_mod  >= 4:
            self.direction_mod = 0
        elif self.direction_mod  <= -1:
            self.direction_mod  = 3

        self.direction = self.all_directions[self.direction_mod ]
        

sim_object = SimObject()

# The visual representation object
class DrawingObject:
    def __init__(self):
        self.window = Tk()
        self.window.title('Simulation')
        self.canvas = Canvas(self.window, background='white', width=0, height=0)
        self.sprite = self.canvas.create_rectangle(0,0,0,0)
        self.canvas.pack()
        self.window.update_idletasks()
        self.window.update()
        #self.window.mainloop()
            

drawing_object = DrawingObject()  

# Class that defines the matrix grid/table
class MatrixObject:
    matrix_values= []
    def __init__(self):
        
        self.matrix_values = [0,0]

    # Function for rendering the matrix visually
    def create_grid(self,window,scale, matrix_values, object_position):
        self.scale = scale
        self.width = matrix_values[0]*self.scale
        self.height = matrix_values[1]*self.scale
        self.pos_x = object_position[0]*self.scale
        self.pos_y = object_position[1]*self.scale
        drawing_object.canvas.config(width=self.width, height=self.height)


        for row in range(0, self.width, self.scale): 
            drawing_object.canvas.create_line([(row , 0), (row , self.height)], fill='black', tags='grid_line_w')


        for col in range(0, self.height, self.scale):
            drawing_object.canvas.create_line([(0, col), (self.width, col)], fill='black', tags='grid_line_h')

        drawing_object.sprite = drawing_object.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x+self.scale, self.pos_y+self.scale, outline="#000", fill="#000")


     

matrix_object = MatrixObject()

   
class InitSim:
   # Start by getting input from stdin and creating matrix, positioning object
    def __init__(self):
        self.raw_inputs = input("Please Enter the first 4 numbers, comma sepeated, to get started: ").split(",")
        try:
            self.init_seq  = list(map(int, self.raw_inputs))
        except:
            print("please enter numbers"+self.raw_inputs)
            self.__init__()
        
        matrix_object.matrix_values = self.init_seq[0:2]
        sim_object.location=self.init_seq[2:4]
        matrix_object.create_grid(drawing_object.window, 100, matrix_object.matrix_values, sim_object.location)
        self.get_commands()

    # Get second range of inputs
    def get_commands(self):    
        self.raw_commands = input("And now enter your simulation commands, comma sepeated: ").split(",")
        try:
            self.sim_commands  = list(map(int, self.raw_commands))
        except:
            print("please enter numbers again")
            self.get_commands()
        
        self.sim_commands_handler(self.sim_commands, self.init_seq)

    


    # Function for parsing through commands, allocate the correct function and check if still within the matrix/table
    def sim_commands_handler(self,sim_seq, init_seq) :
  
        for command in sim_seq:
            if sim_object.location[0] >= 0 and sim_object.location[0] <= (init_seq[0]-1) and sim_object.location[1] >= 0 and sim_object.location[1] <= (init_seq[1]-1):
                if command == 1:
                    sim_object.movement("forward") 
                elif command == 2:
                    sim_object.movement("back") 
                elif command == 3:
                    sim_object.change_direction(+1)
                elif command == 4:
                    sim_object.change_direction(-1)
                elif command == 0:
                    print (str(sim_object.location))
                    self.end_sim()
                    
            # No longer on the matrix
            else:
                print("[-1,-1]")
                self.end_sim()
                
    # Kill simulation - uses a simple timer to show the matrix visualization for 5 seconds after completion
    def end_sim(self):  
            self.time = 5000
            while self.time > 0:
                self.time = self.time - 1
                drawing_object.window.update()


            if self.time == 0:
                drawing_object.window.after(10000, drawing_object.window.destroy)  

           
# Initiate simulation control object
init_sim = InitSim()
