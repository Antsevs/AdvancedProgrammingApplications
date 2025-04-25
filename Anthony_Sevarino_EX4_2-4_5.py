
def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "4.2":
        closeVal = False
        from math import sqrt,exp,sin,acos
        def Secondorder(t):
            g = float(0.50) #instantiate gamma and list
            a = []
            for x in t: #iterate through provided list
               val = 1-(1/sqrt(1-g**2))*exp(-g*t[x])*sin(sqrt(1-g**2)*t[x]+acos(g)) #calculate indexed value
               a.append(val) #add value to list
            return a #return the list from the function
        testList = [0,1,2,3,4]
        print(Secondorder(testList)) #call the function
    elif choice == "4.3":
        closeVal = False
        
        def series(r): #define the series and parallel resistance equivalence equations in respective functions
            ReqS = sum(r)
            return ReqS
        def parallel(r):
            ReqP = 1/(sum(1/ohm for ohm in r))
            return ReqP

        testList = [200, 500, 1500, 4700] 
        print(series(testList))  #call both functions with test list
        print(parallel(testList))
    elif choice == "4.4":
        closeVal = False

        def countdown(y):#instantiate function
            if y == 0: #Reaching zero means finishing countdown
                return 0
            else:
                return y + countdown(y-1) #recursively move down one while adding current value
        print(countdown(2)) #test
    elif choice == "4.5":
        closeVal = False
        
        def calculate(eq, lst):#instantiate function
            arr = []#instantiate list
            for n in lst:#iterate through given variable substitution list
                arr.append(eq(n))#add to array
            return arr
        
        equation = lambda n: 5+n*3 #lambda function since we don't define n here
        testList = [0,1,2,3,4,5]
        print(calculate(equation, testList))
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (4.2, 4.3, 4.4, or 4.5)\nor type 'exit' to close the program\n")
    menu(choice)

