###############################################################################
#    Programming Project #5
#
#    Algorithm
#        display welcome statement
#        call function to open file
#            prompt for strings (a file name)
#            loop while the input is incorrect
#                reprompt for strings (a file name)
#        display choices
#        prompt for an integer (a choice number)
#        loop while the input is incorrect
#            reprompt for an integer (a choice number)
#        call a fuction chosen corresponding to the choice no.
#            prompt for input(s) depending on the function called
#            loop while the input(s) is/are incorrect
#                reprompt for input(s)
#            display output(s) 
#        display closing message
###############################################################################       

import math #import math module
    
def open_file():   
    '''
    Open a file (.off). 
    No parameters
    Returns: the opened file for reading only (fp).
    '''
    #while loop to reprompt for input if it's incorrect
    while True:
        filename = input("Enter an <off> file name: ") #prompt for a file name   
        try:                          #open the file if successful
            fp = open(filename, "r")
            break
            
        except FileNotFoundError:  
            print("Error. Please try again") #display error message if not successful
    return fp
            

def read_face_data(fp, index):
    '''
    Read the line containg the particular face data in file 'fp' 
    indicated by the input 'index'.
    fp: returning value of the open_file() fuction.
    Returns: The face data as three integers
    
    '''
    fp.seek(0)       #start reading file at the beginning
    fp.readline()    #skip the first line
    fp.readline()    #skip the second line
    
    count = -1     #initial value of count to find a particular line to read
    x = 0          #inital string value of x (first number of vertex of face)
    y = 0          #inital string value of y (second number of vertex of face)
    z = 0          #inital string value of z (third number of vertex of face)
    
    #for loop to slice face data from the line corresponding to the index
    for line in fp:
        if line[:2].strip() == '3':
            count = count + 1
            if count == int(index):
                x = int(line[3:8])
                y = int(line[8:13])
                z = int(line[13:17])
    return int(x), int(y), int(z)

def read_vertex_data(fp, index):
    ''' 
    Read the line containg the particular vertex data in file 'fp' 
    indicated by the input 'index'.
    fp: returning value of the open_file() fuction.
    Returns: The vertex data as three floats with six decimal places.
    '''
    fp.seek(0)       #start reading file at the beginning
    fp.readline()    #skip the first line
    fp.readline()    #skip the second line
    
    count = -1   #initial value of count to find a particular line to read
    x = ""       #inital string value of x (first coordinate of vertice)
    y = ""       #inital string value of y (second coordinate of vertice)
    z = ""       #inital string value of z (third coordinate of vertice)
    
    #for loop to slice vertex data from the line corresponding to the index
    for line in fp:
        count = count + 1
        if count == int(index):
            x = line[4:15].strip()
            x = float(x)
            y = line[15:30].strip()
            y = float(y)
            z = line[30:].strip()
            z = float(z)
            
    return round(x,6),round(y,6),round(z,6)

def compute_cross(v1, v2, v3, w1, w2, w3):
    '''
    Compute the cross product of the two particular vectors which each vertices
    located in the particular line in 'fp' computed by read_vertex_data(fp, index) function.
    v1: first coordinate of first vector (float)
    v2: second coordinate of second vector (float)
    v3: third coordinate of third vector (float)
    w1: first coordinate of second vector (float)
    w2: second coordinate of second vector (float)
    w3: third coordinate of second vector (float)
    Returns: three coordinates of the cross product vector (floats rounded to 5 decimal places)
    '''
    x = float(v2)*float(w3) - float(v3)*float(w2)  #formula for fisrt coordinate of cross product   
    y = float(v3)*float(w1) - float(v1)*float(w3)  #formula for second coordinate of cross product 
    z = float(v1)*float(w2) - float(v2)*float(w1)  #formula for third coordinate of cross product 
    return round(x,5), round(y,5), round(z,5)
    

    
def compute_distance(x1, y1, z1, x2, y2, z2):
    '''
    Compute the distance between two particular vertices
    located in a particular line in 'fp' computed by read_vertex_data(fp, index) function.
    v1: first coordinate of first vertice (float)
    v2: second coordinate of second vertice (float)
    v3: third coordinate of third vertice (float)
    w1: first coordinate of second vertice (float)
    w2: second coordinate of second vertice (float)
    w3: third coordinate of second vertice (float)
    Returns: the distance between two particular vertices (floats with 2 decimal places)
    '''
    #formula for distance calculation
    D = math.sqrt((float(x1)-float(x2))**2 + (float(y1)-float(y2))**2 + (float(z1)-float(z2))**2)
    return round(D,2)
    


def compute_face_normal(fp, face_index):
    '''
    Compute normal vector (using compute_cross(v1, v2, v3, w1, w2, w3) fuction ) 
    corresponding to two particular vectors which each vertice of the two vectors 
    located in a particular line in 'fp' computed by read_face_data(fp, face_index)
    fuction and read_vertex_data(fp, index) function.
    fp: returning value of the open_file() fuction.
    face_index: an integer start with 0 to the number of faces in particular file 'fp' leading to 
                three indexes for read_vertex_data(fp, index) function. (int)
    Returns: three coordinates of the cross product vector (floats rounded to 5 decimal places) 
    '''
    first, second, third = read_face_data(fp, face_index) #get three vertex numbers 
   
    x1, y1, z1 = read_vertex_data(fp, first)  #get three coordinates of first vertice
    x2, y2, z2 = read_vertex_data(fp, second) #get three coordinates of second vertice
    x3, y3, z3 = read_vertex_data(fp, third)  #get three coordinates of third vertice
   
    a1, a2, a3 = x2-x1, y2-y1, z2-z1 #vector12 #compute vector12 (start at first vertice and end at second vertice)
    
    b1, b2, b3 = x3-x1, y3-y1, z3-z1 #vector13 #compute vector13 (start at first vertice and end at third vertice)
   
    return compute_cross(a1, a2, a3, b1, b2, b3)
    
    
    
def compute_face_area(fp, face_index):
    '''
    Compute face area.
    fp: returning value of the open_file() fuction.
    face_index: an integer start with 0 to the number of faces in particular file 'fp' leading to 
                three indexes for read_vertex_data(fp, index) function. (int)
    Returns: area of face (float rounded to 2 decimal places)
    '''
    first, second, third = read_face_data(fp, face_index) #get three vertex numbers 
    x1, y1, z1 = read_vertex_data(fp, first)     #get three coordinates of first vertice
    x2, y2, z2 = read_vertex_data(fp, second)    #get three coordinates of second vertice
    x3, y3, z3 = read_vertex_data(fp, third)     #get three coordinates of third vertice
    a = compute_distance(x1, y1, z1, x2, y2, z2) #compute distance between first and second vertice
    b = compute_distance(x1, y1, z1, x3, y3, z3) #compute distance between first and third vertice
    c = compute_distance(x2, y2, z2, x3, y3, z3) #compute distance between second and third vertice
    p = (a+b+c)/2                        #formula for p (a nessessary value to compute area of a triangle)
    A = math.sqrt(p*(p-a)*(p-b)*(p-c))   #formula for area of a triangle #a, b, and c represent length of each side  
    return round(A,2)

def is_connected_faces(fp, f1_ind, f2_ind):
    '''
    Check whether two faces are connected or NOT using read_face_data(fp, f1_ind) function 
    and read_vertex_data(fp, index). Two faces are connected if they shared same two vertices.
    fp: returning value of the open_file() fuction.
    f1_ind: face index of first face (int)
    f2_ind: face_index of second face (int)
    Returns: True if two faces are connected or False if NOT (Boolean) 
    '''
    
    first1, second1, third1 = read_face_data(fp, f1_ind) #pull out three vertex index of face1
    first2, second2, third2 = read_face_data(fp, f2_ind) #pull out three vertex index of face2
    
    a = read_vertex_data(fp, first1)   #first vertice of face1   
    b = read_vertex_data(fp, second1)  #second vertice of face1
    c = read_vertex_data(fp, third1)   #third vertice of face1
    
    x = read_vertex_data(fp, first2)   #first vertice of face2
    y = read_vertex_data(fp, second2)  #second vertice of face2 
    z = read_vertex_data(fp, third2)   #third vertice of face2
       
    #conditions for connected two faces 
    if a == x and (b == y or b == z):
        return True
    
    elif a == x and (c == y or c == z):
        return True
     
    elif b == x and (a == y or a == z):
        return True
    
    elif b == x and (c == y or c == z):
        return True

    elif c == x and (a == y or a == z):
        return True
    
    elif c == x and (b == y or b == z):
        return True
    
    elif a == y and (b == z or c == z):
        return True
     
    elif c == y and (b == z or a == z):
        return True
    
    elif a == z and (b == y or c == y):
        return True
    
    elif b == z and (a == y or c == y):
        return True
     
    else:
        return False
        
        
        
def check_valid(fp, index, shape):
    '''
    Check if the input of index valid. Valid indexes must correspond to either
    number of faces or vertexes in particular file called to be opened.
    fp: returning value of the open_file() fuction.
    index: input leading to a face data or a vertex data (int) 
    shape: "face" or "vertex" (string)
    Returns: True if index correspond to either number of faces or vertexes 
             in particular file called to be opened. False if not. (boolean)
    '''
    fp.seek(0)       #start reading file at the beginning
    fp.readline()    #skip first line
    fp.readline()    #skip second line
    count_faces = 0  #initial value of number of faces
    count_vertices = 0 #initial value of number of vertexes
    
    #counting number of faces
    if shape == "face":

        for line in fp:
            if line[:2].strip() == '3':
                count_faces = count_faces + 1
    #counting number of vertexes            
    if shape == "vertex":        
        
        for line in fp:
            if line[:2].strip() != '3':
                count_vertices = count_vertices + 1
                
    #conditions to identify validity of index
    if index.isdigit(): 
        if int(index) < count_faces or int(index) < count_vertices:
            return True
        else:
            return False
    else:
        return False
        
   
def main():
    ''' 
        This function is the main function that is executed automatically
        while the program is running.
        no parameters
        Returns: the result depends on the loop and conditions within 
        the function.  
    '''
    welcome = ''' Welcome to Computer Graphics!
    We are creating and handling shapes. Any shape can be represented by polygon meshes, 
    which is a collection of vertices, edges and faces.'''
    choices = ''' Please choose an option below:
        1- display the information of the first 5 faces
        2- compute face normal
        3- compute face area
        4- check two faces connectivity
        5- use another file
        6- exit\n '''

    print(welcome)
    fp = open_file()
    print(choices)
    choice = input(">> Choice: ")  
    
    #while loop to reprompt for a choice number
    while choice != '6':    #end the program when input is '6'
        
        #conditions for choice #1: displaythe info of the first 5 faces
        if choice == '1':
            f0, s0, t0 = read_face_data(fp, 0)
            f1, s1, t1 = read_face_data(fp, 1)
            f2, s2, t2 = read_face_data(fp, 2)
            f3, s3, t3 = read_face_data(fp, 3)
            f4, s4, t4 = read_face_data(fp, 4)
            print("{:^7s}{:^15s}".format('face','vertices'))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('0',f0,s0,t0))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('1',f1,s1,t1))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('2',f2,s2,t2))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('3',f3,s3,t3))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('4',f4,s4,t4))
            print(choices)
            choice = input(">> Choice: ")
            
        #conditions for choice #2: compute face normal
        elif choice == '2':
            face_index = input("Enter face index as integer: ")
            while check_valid(fp, face_index, "face") == False:
                print("This is not a valid face index.")
                face_index = input("Enter face index as integer: "  )
            first, second, third = compute_face_normal(fp, face_index)
            print("The normal of face {}: {:>8.5f} {:>8.5f} {:>8.5f}".format(face_index, first, second, third))
            print(choices)
            choice = input(">> Choice: ")  
    
        #conditions for choice #3: compute face area
        elif choice == '3':
            face_index = input("Enter face index as integer: ")
            while check_valid(fp, face_index, "face") == False:
                print("This is not a valid face index.")
                face_index = input("Enter face index as integer: "  )
            area = compute_face_area(fp, face_index)
            print("The area of face {}:{:>9.2f}".format(face_index, area))
            print(choices)
            choice = input(">> Choice: ") 
        
        #conditions for choice #4: check two faces connectivity
        elif choice == '4':
            f1_ind = input("Enter face 1 index as integer: ")
            while check_valid(fp, f1_ind, "face") == False:
                print("This is not a valid face index.")
                f1_ind = input("Enter face 1 index as integer: ")
                
            f2_ind = input("Enter face 2 index as integer: ")
            while check_valid(fp, f2_ind, "face") == False:
                print("This is not a valid face index.")
                f2_ind = input("Enter face 2 index as integer: ")
                
            if is_connected_faces(fp,f1_ind, f2_ind) == True:
                print("The two faces are connected.")
            else:
                print("The two faces are NOT connected.")
                
            print(choices)
            choice = input(">> Choice: ")
        
        #conditions for choice #5: open another file
        elif choice == '5':
            fp = open_file()
            print(choices)
            choice = input(">> Choice: ")
            
        #display error message for invalid input choice number
        #reprompt for a choice number
        else:
            print("Please choose a valid option number.")
            choice = input(">> Choice: ")
            
    #conditions for choice #6: exit the program and display closing message      
    if choice == '6':
        print("Thank you, Goodbye!") 
            
# this was added to make functions to be tested individually on mirmir                
if __name__ == "__main__": 
    main() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
