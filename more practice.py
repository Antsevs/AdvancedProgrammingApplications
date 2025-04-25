import numpy as np
import matplotlib.pyplot as plt

V = float(input('Please input the peak voltage of the circuit: '))
f0 = float(input('Please input the fundamental frequency of the circuit (Hz): '))
k = int(input('Please input the number of harmonics to calculate: '))

# Calculate the time period
T = 1 / f0

# Generate time values over two periods (2T)
x = np.linspace(0, 2 * T, 1000)

# Initialize the output waveform as an array of zeros
v0t = (V / np.pi) + (V / 2) * np.sin(2 * np.pi * f0 * x)

# Loop over the harmonics and accumulate the result
for n in range(1, k + 1):
    v0t -= (2 * V / np.pi) * (np.cos(2 * n * np.pi * f0 * x) / (4 * n**2 - 1))

# Remove negative half cycles (half-wave rectification)
v0t = np.maximum(v0t, 0)

# Plot the waveform
plt.plot(x, v0t)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Rectified Output Waveform (Two Time Periods, No Negative Half-Cycle)')
plt.grid(True)
plt.show()
