import math
import cmath
import numpy

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "7.1":
        closeVal = False
        
        Z2P = numpy.linspace(0, 5*math.pi, 200)#0 to 5pi with 200 even steps
        print('y = {}'.format(2*numpy.sin(3*numpy.cos(Z2P))+5*(Z2P**2)))#calculate with numpy trig and print
        
    elif choice == "7.2":
        closeVal = False
        
        Z2P = numpy.arange(0, 5*math.pi, 0.1)#0 to 5pi with step size of 0.1
        print('y = {}'.format(2*numpy.sin(3*numpy.cos(Z2P))+5*(Z2P**2)))#calculate with numpy trig and print
        
    elif choice == "7.5":
        closeVal = False
        
        endArg = 0
        while endArg != 1:#iterate until proper exit
            
            coMat = numpy.matrix(input('Please enter the coefficient matrix: '))#instantiate A
            colVect = numpy.matrix(input('Please enter the column vector: '))#instantiate b
            
            mrows, mcols = coMat.shape #determine rows and columns of A and b
            vrows, vcols = colVect.shape
            
            if mcols != vrows or mrows != mcols: #ensure square A matrix and even A cols to b rows
                
                print('The entered data was invalid, please try again.')
                print(mrows, vrows, mcols, vcols) #print all values for troubleshooting
                print(coMat, colVect)
                
            else:

                print('x = \n{}'.format((coMat.I)*colVect))#invert A and multiply by b to find x
                endArg = 1#break the loop
                
    elif choice == "7.6":
        closeVal = False

        endArg = 0
        while endArg != 1:#iterate until proper exit
            
            coMat = numpy.matrix(input('Please entthe coefficient matrix: '))#instantiate A
            colVect = numpy.matrix(input('Please enter the column vector: '))#instantiate b
            
            mrows, mcols = coMat.shape #determine rows and columns of A and b
            vrows, vcols = colVect.shape

            detA = numpy.linalg.det(coMat) #find determinant of A
            if mcols != vrows or mrows != mcols or detA == 0: #ensure square A matrix and even A cols to b rows and detA not 0
                
                print('The entered data was invalid, please try again.')
                #print(mrows, vrows, mcols, vcols) TROUBLESHOOTING LINE -----------
                #print(coMat, colVect) TROUBLESHOOTING LINE -----------

            else:
                x = numpy.zeros((vrows, 1))
                for n in range(vrows): 
                    Ai = coMat #reset Ai to A
                    #print('{}\n'.format(Ai))#TROUBLESHOOTING LINE -----------
                    Ai = numpy.insert(Ai,n,colVect.flatten(), 1) #add new nth column as colVect
                    #print('{}\n'.format(Ai)) #TROUBLESHOOTING LINE -----------
                    Ai = numpy.delete(Ai, [n+1], 1) #remove old nth column
                    #print('{}\n'.format(Ai)) #TROUBLE SHOOTING LINE -----------
                    x[n, 0] = numpy.linalg.det(Ai) / detA #calculate xi and add to x matrix
                print('x = \n{}'.format(x)) #print x matrix
                endArg = 1#break the loop
        
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (7.1, 7.2 7.5, or 7.6)\nor type 'exit' to close the program\n")
    menu(choice)
