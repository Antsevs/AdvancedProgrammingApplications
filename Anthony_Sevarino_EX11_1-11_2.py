import math
import cmath
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FC
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np

def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "11.1":
        closeVal = False
        
        #calculation defs
        def pCalc():
            neperP = 1/(2*r.get()*c.get())
            resP = 1/(math.sqrt(l.get()*c.get()))
            rootsP1 = -neperP + cmath.sqrt(neperP**(2)-resP**(2))
            rootsP2 = -neperP - cmath.sqrt(neperP**(2)-resP**(2))

            result.config(text = 'Resonant Frequency: {}Hz\nNeper Frequency: {}Hz\nRoots: {}\n{}'.format(neperP, resP, rootsP1, rootsP2))

        def sCalc():
            neperS = r.get()/(2*l.get())
            resS = 1/(math.sqrt(l.get()*c.get()))
            rootsS1 = -neperS + cmath.sqrt(neperS**(2)-resS**(2))
            rootsS2 = -neperS - cmath.sqrt(neperS**(2)-resS**(2))

            result.config(text = 'Resonant Frequency: {}Hz\nNeper Frequency: {}Hz\nRoots: {}\n{}'.format(neperS, resS, rootsS1, rootsS2))

            
        #create main window
        main_page = Tk()
        main_page.title("Frequency of Series or Parallel Visualizer")

        #instantiate RLC variables
        r = DoubleVar()
        l = DoubleVar()
        c = DoubleVar()

        #create labels and entries
        labelR = Label(main_page, text = 'Please enter a Resistor value: ')
        entryR = Entry(main_page, textvariable = r)
        
        labelL = Label(main_page, text = 'Please enter an Inductor value: ')
        entryL = Entry(main_page, textvariable = l)
        
        labelC = Label(main_page, text = 'Please enter a capacitor value: ')
        entryC = Entry(main_page, textvariable = c)
        #create buttons
        pCircuit = Button(main_page, bg = 'IndianRed1', text = 'Parallel RLC Circuit', command = pCalc)
        sCircuit = Button(main_page, bg = 'IndianRed1', text = 'Series RLC Circuit', command = sCalc)

        #canvas creation
        canvas = Canvas(main_page, bg = 'thistle2')

        canvas.pack()
        pCircuit.pack()
        sCircuit.pack()
        labelR.pack()
        entryR.pack()
        labelL.pack()
        entryL.pack()
        labelC.pack()
        entryC.pack()

        #calculate frequencies to present

        result = Label(main_page, text = '', bg = 'thistle2')
        result.pack()
        
        mainloop()
        
    elif choice == "11.2":
        closeVal = False
        ##NOTE, THIS PROGRAM IS DERIVED FROM MY EXERCISE 8.4 SOLUTION, AS WELL AS YOUR EXAMPLE 11.6
        
        # Create main window
        main_page = Tk()
        main_page.title("Second-Order Control System Response")

        # Create labels and entries 
        labelStart = Label(main_page, text="Starting Time (seconds):", font=("Times New Roman", 12))
        labelStart.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        
        entryStart = Entry(main_page)
        entryStart.grid(row=0, column=1, padx=5, pady=5)

        labelEnd = Label(main_page, text="End Time (seconds):", font=("Times New Roman", 12))
        labelEnd.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        
        entryEnd = Entry(main_page)
        entryEnd.grid(row=1, column=1, padx=5, pady=5)

        labelSS = Label(main_page, text="Step Size:", font=("Times New Roman", 12))
        labelSS.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        entrySS = Entry(main_page)
        entrySS.grid(row=2, column=1, padx=5, pady=5)

        # Slider for damping coefficient
        labeldampCo = Label(main_page, text="Damping Coefficient:", font=("Times New Roman", 12))
        labeldampCo.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        dampCoSlider = Scale(main_page, from_=0, to=0.95, resolution=0.01, orient=HORIZONTAL, length=300)
        dampCoSlider.grid(row=3, column=1, padx=5, pady=5)

        #Calculations
        def plot_response():
            # Get user input
            timeInit = int(entryStart.get())
            timeFin = int(entryEnd.get())
            step = float(entrySS.get())
            g = dampCoSlider.get()

            # calc t
            t = np.arange(timeInit, timeFin, step)

            # Create fig
            fig = plt.figure(figsize=(6, 4))

            # Determine dampCo
            ytg = 1 - (1 / np.sqrt(abs(1 - (g ** 2)))) * np.exp(g * t) * np.sin(np.sqrt(abs(1 - (g ** 2))) * t + np.arccos(g))

            # Plot
            plt.plot(t, ytg, color='blue')
            plt.xlabel('Time (s)')
            plt.ylabel('y(t, g)')
            plt.title('Second-order Control System Response (Damping Coefficient = {:.2f})'.format(g))
            plt.axis([timeInit, timeFin, min(ytg), max(ytg)])
            plt.legend(['\u03B3 = {:.2f}'.format(g)])
            plt.grid(True)

            # inject plot into window
            canvas = FC(fig, master=main_page)
            canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10, pady=10)
            canvas.draw()

        # Buttons
        Plot_Btn = Button(main_page, text="Plot", bg='khaki', command=plot_response)
        Plot_Btn.grid(row=4, column=0, columnspan=2, sticky=E + W, padx=10, pady=10)

        main_page.mainloop()
        
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (11.1 or 11.2)\nor type 'exit' to close the program\n")
    menu(choice)
