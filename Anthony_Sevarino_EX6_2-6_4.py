import math
import cmath

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "6.2":
        closeVal = False

        class Lottery: #instantiate class

            def __init__(self, name): #set class parameters
                from random import randint
                numList = [] #instantiate list for generated numbers to be stored
                for i in range(6):
                    self.num = randint(0,9) #generate random number
                    numList.append(self.num) #append generated number to list

                print('Hello {}, your generated numbers are: {}.'.format(name, numList))

        decision1 = Lottery('Anthony') #call Lottery with name Anthony
        decision2 = Lottery('Masood')  #call Lottery with name Masood
    elif choice == "6.3":
        closeVal = False

        class IsPrime: #instantiate class

            def __init__(self, num): #set class parameters
                if num <= 1 or (num % 2 == 0 and num != 2): #eliminate small and even numbers
                    print('No')
                    return
                elif num == 2:
                    print('yes') #include 2 case in primes
                    return
                for i in range(3, int(num**0.5) + 1, 2): #check prime formula
                    if num % i == 0:
                        print('No')
                        return
                print('Yes')
    
        numCheck1 = IsPrime(int(input('Please enter a number'))) #call IsPrime with user entered number
                            
    elif choice == "6.4":
        closeVal = False

        class Area: #instantiate Area super class

            def __init__(self, d1, d2): #accept user parameters for base and height from subclasses
                self.d1 = d1
                self.d2 = d2

            def calc(self): #calculate basic area inside super class
                return self.d1 * self.d2

        class Triangle(Area): #bh/2
                def tArea(self):
                    return 0.5 * self.calc() #calculate triangle specific area with value from calc in super class
        class Rectangle(Area): #lw
                def rArea(self):
                    return self.calc() #accept basic area calculation from super class

        base, height = [int(x) for x in input('Enter base and height of the triangle, separated by a comma: ').split(',')] #take user input 
        t = Triangle(base, height) #send user input to triangle subclass
        r = Rectangle(base, height) #send user input to rectangle subclass
        print(t.tArea()) #print triangle area
        print(r.rArea()) #print rectangle area
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (6.2, 6.3, or 6.4)\nor type 'exit' to close the program\n")
    menu(choice)
