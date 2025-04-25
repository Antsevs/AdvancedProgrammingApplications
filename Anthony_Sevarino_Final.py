import math
import cmath
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FC
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np

##NOTE, THIS PROGRAM IS DERIVED FROM MY EXERCISE 11.2 SOLUTION, AS WELL AS YOUR EXAMPLE 11.6
        
# Create main window
main_page = Tk()
main_page.title("AAmpliutude or Frequency Modulated Signal Plot")

# Create labels and entries 
labelVc = Label(main_page, text="Carrier Voltage (Vc):", font=("Times New Roman", 12))
labelVc.grid(row=0, column=0, padx=5, pady=5, sticky=E)

entryVc = Entry(main_page)
entryVc.grid(row=0, column=1, padx=5, pady=5)

labelFc = Label(main_page, text="Carrier Frequency (fc):", font=("Times New Roman", 12))
labelFc.grid(row=1, column=0, padx=5, pady=5, sticky=E)

entryFc = Entry(main_page)
entryFc.grid(row=1, column=1, padx=5, pady=5)

labelFm = Label(main_page, text="Message Frequency(fm):", font=("Times New Roman", 12))
labelFm.grid(row=2, column=0, padx=5, pady=5, sticky=E)

entryFm = Entry(main_page)
entryFm.grid(row=2, column=1, padx=5, pady=5)

# Slider for damping coefficient
labelM = Label(main_page, text="Modulation Index (m):", font=("Times New Roman", 12))
labelM.grid(row=3, column=0, padx=5, pady=5, sticky=E)

signal = StringVar(value = 'Not Selected')
mSlider = Scale(main_page, from_=0, to=1, resolution=0.1, orient=HORIZONTAL, length=300)
mSlider.grid(row=3, column=1, padx=5, pady=5)

def amSignal():
    signal.set('am')
    mSlider.config(from_=0, to=1, resolution=0.1, label="AM Selected")

def fmSignal():
    signal.set('fm')
    mSlider.config(from_=0, to=10, resolution=0.5, label="FM Selected")

buttonAM = Button(main_page, text="AM", command=amSignal, bg='red')
buttonAM.grid(row=4, column=0, padx=5, pady=5)

buttonFM = Button(main_page, text="FM", command=fmSignal, bg='gold')
buttonFM.grid(row=4, column=1, padx=5, pady=5)

global canvas
fig = plt.figure(figsize=(5,4))
canvas = FC(fig, main_page)
canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, padx=10, pady=10)

#Calculations
def plot_response():
    global canvas
    vc = float(entryVc.get())
    fc = float(entryFc.get())
    fm = float(entryFm.get())
    m = float(mSlider.get())
    t = np.linspace(0, 1, 1000)

    plt.clf()
    
    if signal.get() == 'am':
        amplt = vc * (1 + m * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)
        plt.plot(t, amplt, color='blue')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title("AM Signal")
        plt.axis([0, 1, min(amplt), max(amplt)])
    elif signal.get() == 'fm':
        fmplt = vc * np.cos(2 * np.pi * fc * t + m * np.sin(2 * np.pi * fm * t))
        plt.plot(t, fmplt, color='green')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title("FM Signal")
        plt.axis([0, 1, min(fmplt), max(fmplt)])
    else:
        #print error code
        print('uh oh')

    plt.grid(True)

    canvas.draw()
    

# Buttons
Plot_Btn = Button(main_page, text="Plot", bg='khaki', command=plot_response)
Plot_Btn.grid(row=6, column=0, columnspan=2, sticky=E + W, padx=10, pady=10)

main_page.mainloop()
