import math
import cmath

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "3.4":
        closeVal = False

        val = 0 #instantiate necessary check values
        parVal = 0
        closeVal = 0
        nCheck = False
        while closeVal == 0:
            r = [int(x) for x in input('Enter resistor values as a list seperated by commas: ').split(',')] #user input list

            for g in range(len(r)): #negative checker
                if r[g] < 1:
                    nCheck = True
            choice = input("Are the resistors in series, or parallel?")
            
            if choice == 'series' and nCheck == False: #series calculation
                closeVal = 1;
                for t in range(len(r)):
                    val += r[t]
                    
            elif choice == 'parallel' and nCheck == False: #parallel calculation
                closeVal = 1;
                for t in range(len(r)):
                    parVal += 1/r[t]
                val = 1/parVal
                
            elif nCheck == True: #negative catcher
                closeVal = 0
                nCheck = False
                print("Resistors must all be positive values, try again.")
                
            else: #incorrect input catcher
                closeVal=0
                print('Incorrect input, please try again')
                
        print("The calculated resistor value is: {:.2f} ohms".format(val))
        
    elif choice == "3.6":
        closeVal = False
        
        keyVal = {} #instantiate dictionary
        from math import cos, sin, sqrt
        
        x = [float(m) for m in input("Enter some values, seperated by commas, for which the equation will be evaluated: ").split(',')]

        for i in range(len(x)): #iterate through user values from list
            fx = (2*cos(x[i])+5*sin(cos(5*x[i])))/(sqrt(abs(sin(4*x[i])))) #calculate each value
            keyVal[i] = fx #attatch value to key and submit to dictionary
            
        print(keyVal)
        
    elif choice == "3.8":
        closeVal = False

        rng = 0
        listCheck = 0
        x = [int(r) for r in input("Enter a set of numbers, seperated by commas: ").split(',')]
        y = [int(r) for r in input("Enter a second set of numbers, seperated by commas: ").split(',')]

        #Create a set from the two user given lists removing duplicates manually
        if len(x) >= len(y): #determine which set's range to use (the longer one)
            rng = len(x)
            listCheck = 1
        else: 
            rng = len(y)
            listCheck = 2
        for n in range(rng): #iterate through the lists and remove duplicates depending on listCheck
            if listCheck == 1:
                if n < len(y) and y[n] in x:
                    x.remove(y[n])
            elif listCheck == 2:
                if n < len(x) and x[n] in y:
                    y.remove(x[n])
        if listCheck == 1: #correct trimmed list transferred to set
            newSet = set(x)
        elif listCheck == 2:
            newSet = set(y)
        result = []
        from math import sin, cos
        #Use set to evaluate given expression
        for t in newSet:#iterate through the set
            fx = (5*t*cos(6*t)+t**2*sin(t)) #find resulting calculation
            result.append(fx) #add to list
        resSet = set(result) #convert list to set
        print(resSet) 
        
        
        
    elif choice == "3.9":
        closeVal = False
        
        #y(n) = 0.5x(n) + 0.7x(n-1) + 0.9x(n-2)
        #input list and output list
        xn = [int(x) for x in input("Please enter a list of numbers to use as input for the FIR equation: ").split(',')]
        yn = {}
        for n in range(len(xn)+2): #iterate
            n+=1
            if n >= 2: #subsequent iterations
                y = (0.5*xn[n-2] if (n-2) < len(xn) else 0)+(0.7*xn[n-3]if n-3 >= 0 and (n-3) < len(xn) else 0)+(0.9*xn[n-4] if (n-4) >= 0 and (n-4) < len(xn) else 0)
                yn[n] = y
            elif n == 1: #second iteration
                (0.5*xn[n-1] if (n-1) < len(xn) else 0)+(0.7*xn[n-2] if (n-2) >= 0 and (n-2) < len(xn) else 0)
            elif n == 0: #first iteration
                yn[n] = 0.5 * xn[n]
        print("The output for the FIR equation is: {}".format(yn))

    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (3.4, 3.6, 3.8, or 3.9)\nor type 'exit' to close the program\n")
    menu(choice)
