from sympy import *

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "9.2":
        closeVal = False

        #solution i
        x = symbols('x') #establish sympy symbols in eq
        f = solve(x**5 + 2*x**4 - 31*x**3 - 8*x**2 + 180*x - 144) #determine roots
        print('\n(i). f = {}'.format(f)) #print

        #solution ii
        f = solve(x**2 + 9) #determine roots
        print('\n(ii). f = {}'.format(f)) #print
        
    elif choice == "9.4":
        closeVal = False

        t = symbols('t') #instantiate sympy symbol for t
        ic = 2*diff(2*t*cos(5*t)) #determine current equation
        #troubleshooting line: print('\n ic equation is {}'.format(ic))
        soln = ic.evalf(subs = {t:2.2})#evaluate current equation @ 2.2 seconds
        print('\nCurrent at 2.2 seconds is {}.'.format(soln))
        
    elif choice == "9.5":
        closeVal = False

        #if C = (4sin(100t))*10**-3, integrate both sides to get v = (1/c) integ(icdt + v0) where v not is the initial voltage

        t = symbols('t') #instantiate sympy symbol for t
        v = (1/(100*10**-3))*integrate((4*sin(100*t))*10**-3, t) #integrate ic with respect to t (no limits)
        print('\nV = {} + v_0'.format(v)) #include initial voltage (integration constant)
        
        
    elif choice == "9.6":
        closeVal = False
        #assuming proper user input
        r, l, c = [float(x) for x in input('Enter resistor values as a list seperated by commas: ').split(',')] #obtain user inputs

        t = symbols('t') #instantiate sympy symbol for t

        v = Function('v') #establish function variable

        eq = Eq(v(t).diff(t, t) + (1/(r*c))*v(t).diff(t)+(1/(l*c))*v(t), 0) #setup equation, homoegenous

        soln = dsolve(eq, v(t)) #ODE solve eq for v(t)

        print('\nv = {}'.format(soln))
    
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (9.2, 9.4, 9.5, 9.6)\nor type 'exit' to close the program\n")
    menu(choice)
