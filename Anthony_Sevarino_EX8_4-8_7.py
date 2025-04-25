import math
import cmath
import matplotlib.pyplot as plt
import numpy

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "8.4":
        closeVal = False

        #instantiate user variables and lists
        timeInit = int(input('Please enter the starting time in seconds of the system: ')) 
        timeFin  = int(input('Please enter the final time in seconds of the system: '))
        step     = float(input('Please enter the desired step seize of the system: '))
        dampCo = [float(x) for x in input('Please enter the damping coefficient of the system as floats less than 1 as a comma separated list: ').split(',')]

        #determine time range list
        t = numpy.arange(timeInit, timeFin, step)

        #Evaluate y against damping coefficient list and graph respective chart
        i = 0
        for g in dampCo:

            i += 1 #increment counter
            
            #alternate color of graph line for ease of reading
            if i%2 == 0:
                color = 'r'
            else:
                color = 'b'
            #now solve equation for current g
            ytg = 1 - (1/numpy.sqrt(abs(1 -(g**2))))* numpy.exp(g*t) * numpy.sin(numpy.sqrt(abs(1-(g**2))) * t + numpy.acos(g))

            plt.subplot(len(dampCo), 1, i)
            plt.plot(t, ytg, color)
            plt.xlabel('Time (s)')
            plt.ylabel('y(t,g)')
            plt.title('Second-order Control System Response based on\nDamping Coefficient {}'.format(g))
            plt.axis([timeInit, timeFin, min(ytg), max(ytg)])
            plt.legend(['\u03B3 = {}'.format(g)])
            plt.grid(True)

        #plot the graphs 
        plt.tight_layout()
        plt.show()
        
    elif choice == "8.6":
        closeVal = False  

        #obtain user values
        data = numpy.array([float(x) for x in input('Please enter the data vector as values separated by commas: ').split(',')])
        VrefP = float(input('Please enter the maximum reference voltage for the ADC: '))
        VrefM = float(input('Please enter the minimum reference voltage for the ADC: '))
        b = int(input('Please enter the number of bits for the ADC: '))

        #calcuate delta and quan
        delta = (VrefP - VrefM)/(2**b)
        n = numpy.arange(len(data))

        quan = numpy.round((data - VrefM) / delta) * delta + VrefM

        
        #Plot 1
        plt.plot(n, data)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Input and Quantized Data')
        plt.grid(True)
        #Plot 2
        plt.step(n, quan)
        plt.legend(['Input', 'Quantized'])
        plt.axis()

        plt.show()
             
    elif choice == "8.7":
        closeVal = False

        #instantiate user data, determine x axis and calculate time period
        V = float(input('Please input the peak voltage of the circuit: '))
        f0 = float(input('Please input the fundamental frequency of the circuit: '))
        k = int(input('Please input the number of harmonics to calculate: '))
        t = 1 / f0
        x = numpy.linspace(0,2 * t,100)

        #evaluate v0t over summation boundaries
        v0t = 0
        for n in range(1, k+1):
            v0t +=(V/numpy.pi)+(V/2)*numpy.sin(2*numpy.pi*f0*x)-((2*V)/numpy.pi)*(numpy.cos(2*n*numpy.pi*f0*t)/(4*(n**2)-1))

        #rectify circuit above 0.7 voltage bias
        v0t = numpy.maximum(0.7, v0t)
        #plot
        plt.plot(x, v0t)
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (v)')
        plt.title('Rectified Output Waveform')
        plt.grid(True)
        plt.show()
        
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (8.4, 8.6, or 8.7)\nor type 'exit' to close the program\n")
    menu(choice)
