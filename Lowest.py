'''
                  Xavier Kidston
                    Study Time

The purpose of this program is to determine how to split studying time
between courses with different marks
'''



'''
Function: To get the users marks for a single course and determine their current
          weighted average
Parameters: None 
Returns: numerator/denominator
'''
def calc_wm():
    #Establishes variables
    num = 0
    den = 0
    mark = 0
    weight = 0
    answer = ''
    
    while True:
        
        #Gets mark and the weight of the mark
        mark = int(input("Enter a mark: "))
        weight = int(input("Enter the mark's weight: "))
        
        #Error checks if the users put in actually possible weight and mark
        if (mark <= 100 and weight <= 100):
            num += (mark * weight)
            den += weight
        else:
            break
        
        #If the denominator (total weight) is greater than 100 it stops the loop
        if den >= 100:
            break
        
        #Checks if the user has another weighted mark to enter
        answer =\
        input("Do you have another mark for the class to input (y) or (n): ")
    
        # Error checks the users answer to essentially to get if its a yes or no
        if (answer[0] == "y" or answer [0] == "Y"):
            pass
        else:
            break
    
    return num/den



'''
Function: To generate strings with information given to the amount specified
Parameters: Qcour - The question for which course
            Qmark - The question for the mark of the course
            Qweig - The q for if the person knows the weight of their course
            Qhour - How many hours do they have available to study
Returns: Dict - a dictionary containing each course matched with the mark
         Hours - The amount of hours available to study
         grades - A list of the grades
         courses - the list of courses
'''
def inputer(Qcour, Qweig, Qmark, Qhour):
    
    #Sets up variables
    cour = ''
    answer = ''
    answ = ''
    mark = 0
    qball = 0
    hours = 0
    grades = []
    courses = []
    Dict = {}
    
    #Runs the while loop
    while True:
        cour = input(Qcour)
        answer = input(Qweig)
        
        #If the user doesn't know their current weighted mark we get it
        if (answer[0] == "N" or answer [0] == "n"):
            mark = calc_wm()
        
        #If they do know the mark, we get it
        else:
            mark = int(input(Qmark))
        
        #Adds the mark and course, and marks up to qball
        grades.append(mark)
        courses.append(cour)
        qball += 1
        
        #checks if the user has another course to input, and makes sure their
        #total courses are less than 6, because the max course limit if 5
        #And if all those conditions are not meant, breaks the while loop
        answ = input("Do you have another course too input? ")
        if (answ[0] == "y" or answ[0] == "Y" and qball < 6):
            pass
        else:
            break
    
    #Gets the amount of hours available to study with
    for i in range(len(courses)):
        Dict[grades[i]] = courses[i]    
    hours = int(input(Qhour))
                      
    return Dict, hours, grades, courses



'''
Function: To determine the differences between marks
Parameter: grades - a list of the % grades
           hours - the amount of hours available to study
Return: per_cha - A list of the hours per course
'''
def comp(grades, hours):
    
    #sets up variables
    reducer = 0
    total = 0
    avg = 0
    div = 0
    per_cha = []
    
    #Sets the percentage change in time alloted per 10%
    reducer = len(grades)
    for item in grades:
        total += item
    
    #Gets two numbers for the hours per course, and the total average
    avg = total / reducer
    div = hours / reducer
    
    #Gets the amount of time per course alloted, and then appends it to the
    #list
    for item in grades:
        per_cha.append((2 - (item / avg)) * div)
        
    return per_cha



'''
Functions: To compute how the user breaks up their study time
Parameters: Grades - a list of grades
            courses - a list of courses
            hours - the amount of hours available to study with
Returns: Break_down - a dictionary of courses with hours available
'''
def changes(grades, courses, hours, Dict):
    
    #Set up variables
    Break_down = {}
    nums = 0
    reducer = 0
    percent = 0
    course = ''
    new_gra = []
    new_cou = []
    per_cha = []
    Break_down = {}
    
    #While there are items in grades list
    while grades:
        nums = grades[0]
        
        #Compares the numbers to sort for small to large
        for x in range(len(grades)):
            if grades[x] < nums:
                nums = grades[x]
        
        #Creates the two new lists, one using dictionary, and the other from
        #nums then erases the old mark from 
        new_cou.append(Dict.get(nums))
        new_gra.append(nums)
        grades.remove(nums)
    
    #calls a different function to work the computation
    per_cha = comp(new_gra, hours)
    
    #Creates a dictionary of the hours per course to use for a key later
    for item in range(len(per_cha)):
        Break_down[new_cou[item]] = per_cha[item]
    
    return Break_down
    
    

'''
Function: To combine all other functions
Parameters: None
Returns: None
'''
def main():
    
    #calls inputer
    Dict, hours, grades, courses\
        = inputer("Name a course you are taking: ", \
                  "Do you know the weighted grade of that course? ", \
                  "What is the mark for the course? ", \
                  "How many hours do you have to study? ")
    
    #calls changes to get the hours per course
    Ladel = changes(grades, courses, hours, Dict)
    
    #Prints a single line, and then prints off the courses and minutes
    #that should be spent on each course
    print()
    for item in courses:
        print(item + ":", (Ladel[item] * 60), \
        "are the minutes you should spend on this course.")