from tkinter import *



root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
strang = str(w//2) + 'x' + str(h//2)
root.geometry(strang)
root.resizable(0, 0)
classes = []
tem = ''



'''
Compresses making buttons into a single utility for use, because buttons
become prominent in my coding as well as creates the ability to place those
buttons
'''
class boo_tool:
    def __init__(self, location, text, command = None, side = None, padx = 2, pady = 2):
        self._local = location
        self._text = text
        self._comm = command
        self._side = side
        self._padx = padx
        self._pady = pady
        
    def boof(self):
        boof = Button(self._local, text = self._text, command = self._comm)
        boof.pack(side = self._side, padx = self._padx, pady = self._pady)
        self._boof = boof
        
    def tx(self, xe, ye):
        self._x = xe
        self._y = ye
        txt = Text(self._local, height = self._y, width = self._x)
        txt.pack(side = self._side)
        txt.insert(END, self._text)
    
    def plak(self, xe, ye):
        self._xe = xe
        self._ye = ye
        self._boof.place(x = xe, y = ye)    



'''
Function: To open buttons for each course to add marks (view current courses)
Parameters: None
Returns: None
'''
def tarantula():
    
    #Gets a global variables, as perameters are hard pressed for tkinter
    global tem
    
    #Sets up a button for each course dependant on how many courses there are
    #utilizing lambda to pass variables through boo_tool as variables
    #can't be passed through without it
    if len(classes) == 1:
        boo_tool(root, classes[0][0], lambda: terry(classes[0]), LEFT).boof()
    
    #For two classes
    elif len(classes) == 2:
        boo_tool(root, classes[0][0], lambda: terry(classes[0]), LEFT).boof()
        boo_tool(root, classes[1][0], lambda: terry(classes[1]), LEFT).boof()
    
    #For three classes
    elif len(classes) == 3:
        boo_tool(root, classes[0][0], lambda: terry(classes[0]), LEFT).boof()
        boo_tool(root, classes[1][0], lambda: terry(classes[1]), LEFT).boof()
        boo_tool(root, classes[2][0], lambda: terry(classes[2]), LEFT).boof()
    
    #for four classes
    elif len(classes) == 4:
        boo_tool(root, classes[0][0], lambda: terry(classes[0]), LEFT).boof()
        boo_tool(root, classes[1][0], lambda: terry(classes[1]), LEFT).boof()
        boo_tool(root, classes[2][0], lambda: terry(classes[2]), LEFT).boof()
        boo_tool(root, classes[3][0], lambda: terry(classes[3]), LEFT).boof()
    
    #For five classes
    elif len(classes) == 5:
        boo_tool(root, classes[0][0], lambda: terry(classes[0]), LEFT).boof()
        boo_tool(root, classes[1][0], lambda: terry(classes[1]), LEFT).boof()
        boo_tool(root, classes[2][0], lambda: terry(classes[2]), LEFT).boof()
        boo_tool(root, classes[3][0], lambda: terry(classes[3]), LEFT).boof()
        boo_tool(root, classes[4][0], lambda: terry(classes[4]), LEFT).boof()

        
        
'''
Function: to delete a mark from a course in the registry
Parameters: None
Returns: None
'''
def dinosaur():
    
    #sets up variables
    ls = []
    pur = []
    global e, classes
    
    #Ensures the user has a class inputted
    if len(classes) == 0:
        print("Don't work")
        return
    
    #Removes a mark from a course
    string = e.get()
    for item in classes:
        if item[0] in string:
            string = string.replace(item[0], '')
            string = string.split(' ')
            ls = []
            for itm in string:
                if itm.isdigit():
                    ls.append(int(itm))
            item.remove(ls)    



'''
Function: Top remove a course from the list
Parameters: None
Returns: None
'''
def trex():
    
    #Sets up variables
    ls = []
    pur = []
    global e, classes
    
    #Error checks to make sure the user has classes inputted
    if len(classes) == 0:
        print("Don't work")
        return
    
    #Gets the string input, and then runs through which course the user is
    #trying to delete
    string = e.get()
    for item in classes:
        for i in item:
            if string in i:
                classes.remove(item)



'''
Function: Gets input from the user
Parameters: None
Returns: string - a string of the users input
'''
def get_inp():
    global e
    string = e.get()
    return string



'''
Function: To add marks to a course in the classes data structure
Parameters: None
Returns: None
'''
def terry(cuc):
    
    #Sets up variables for later use
    pur = []
    ls = []
    global classes, tem
    string = get_inp()
    
    #This error checks to make sure the user has input classes before
    if len(classes) == 0:
        print("Don't work")
        return
    
    #checks which course the mark is meant to be in, and then puts the mark
    #in that course
    for item in classes:
        if item == cuc:
            pur = string.split(' ')
            for itm in pur:
                if itm.isdigit():
                    ls.append(int(itm))
                    
            item.append(ls)
    
    #Resets the global variable
    
 


'''
Function: To add a course to the data of classes
Parameters: None
Returns: None
'''
def printtext():
    
    #Sets up variables
    LIST = []
    global e, classes
    string = e.get()
    
    #error checks to make sure the user hasn't tried to input the course prior
    for item in classes:
        if string in item:
            return
        
    #Makes a list for the course for later appending of the marks to it
    LIST.append(string)
    classes.append(LIST)
    
    
#Creates the entry point
e = Entry(root)
e.pack()
e.focus_set()


#Sets up the tool bars
toolbar = Frame(root, bg = "grey")
boo_tool(toolbar, "Quit", root.destroy, RIGHT).boof()
boo_tool(toolbar, "Add Marks to Courses", tarantula, LEFT).boof()
boo_tool(toolbar, "Add Course", printtext, LEFT).boof()
boo_tool(toolbar, "Remove Mark", dinosaur, RIGHT).boof()
boo_tool(toolbar, "Remove Course", trex, RIGHT).boof()
boo_tool(root, "The format to Enter a class is 'Course',\
marks are inputted as 'mark weight'.", None, BOTTOM).tx(40, 5)
toolbar.pack(side = TOP, fill = X)



'''
Toolbar menu items
'''
root.mainloop()