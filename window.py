from tkinter import *



'''
Compresses making buttons into a single utility for use, because buttons
become prominent in my coding
'''
class boo_tool:
    def __init__(self, location, text, command, side = None, padx = 2, pady = 2):
        self._local = location
        self._text = text
        self._comm = command
        self._side = side
        self._padx = padx
        self._pady = pady
        #self._x = x
        #self._y = y
        boot = Button(self._local, text = self._text, command = self._comm)
        boot.pack(side = self._side, padx = self._padx, pady = self._pady)
        self._boot = boot
    def plak(self, xe, ye):
        self._xe = xe
        self._ye = ye
        self._boot.place(x = xe, y = ye)



classes = []


    
def doNothing():
    print("YOU AT")



'''
Runs through all the setup to output the screen
'''
root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
strang = str(w) + 'x' + str(h)
root.geometry(strang)
root.resizable(0, 0)



'''
Function: Adds a mark to a course
Parameters: None
Returns: None
'''
def add_m():
    global classes
    mark = StringVar()
    e = Entry(root, textvariable = mark, bg = "lightblue").place\
        (x = 207, y = 30, width = 63, height = 40)
    enter = boo_tool(root, "Enter", doNothing).plak(269, 40)
    #classes[i].append(mark)



'''
Function: Adds a course to the memory
Parameters: None
Returns: None
'''
def add_c():
    global classes
    course = StringVar()
    e = Entry(root, textvariable = course, bg = "lightgreen").place\
        (x=130, y=30, relwidth=0, relheight=0, width=72, height=40)
    enter = boo_tool(root, "Enter", doNothing, LEFT).plak(201, 40)
    coursM = []
    coursM.append(e)
    classes.append(coursM)
    



'''
Toolbar menu items
'''

toolbar = Frame(root, bg = "grey")
boo_tool(toolbar, "View Current Courses", doNothing, LEFT)
boo_tool(toolbar, "Add Course", add_c, LEFT)
boo_tool(toolbar, "Add Mark", add_m, LEFT)
boo_tool(toolbar, "Quit", root.destroy, RIGHT)
boo_tool(toolbar, "Remove Mark", doNothing, RIGHT)
boo_tool(toolbar, "Remove Course", doNothing, RIGHT)


toolbar.pack(side = TOP, fill = X)

root.mainloop()