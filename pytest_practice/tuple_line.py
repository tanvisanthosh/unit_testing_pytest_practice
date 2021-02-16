#tuple_line.py

def slope_line(x1, y1, x2, y2, x):
    #x1 = float(input("Please enter a value for x1:"))
    #y1 = float(input("Please enter a value for y1:"))
    #x2 = float(input("Please enter a value for x2:"))
    #y2 = float(input("Please enter a value for y2:"))
    m = (y2-y1)/(x2-x1)
    #print ("The slope of the line made by the points is {}.".format(m))
    #x = float(input("Please enter a value for x:"))
    y = (m * (x - x1)) + y1
    #print("The line passing through the points given that has a y value of {}.".format(m))
    return y
