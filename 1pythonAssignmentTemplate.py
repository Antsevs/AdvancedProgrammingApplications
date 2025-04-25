import math
import cmath

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "ENTER EXERCISE NUMBER":
        closeVal = False
        ##CODE HERE
    elif choice == "ENTER EXERCISE NUMBER":
        closeVal = False
        ##CODE HERE
    elif choice == "ENTER EXERCISE NUMBER":
        closeVal = False
        ##CODE HERE
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (EXERCISE NUMBERS)\nor type 'exit' to close the program\n")
    menu(choice)
