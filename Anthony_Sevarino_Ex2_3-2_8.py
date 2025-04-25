#3.4, 3.6, 3.8, 3.9

#3.4
    #user enter r values as list, ask if series or parallel, ensure all are positive

val = 0
parVal = 0
closeVal = 0
nCheck = False
while closeVal == 0:
    r = [int(x) for x in input('Enter resistor values as a list seperated by commas: ').split(',')]
    for g in range(len(r)):
        if r[g] < 1:
            nCheck = True
    choice = input("Are the resistors in series, or parallel?")
    if choice == 'series' and nCheck == False:
        closeVal = 1;
        for t in range(len(r)):
            val += r[t]
    elif choice == 'parallel' and nCheck == False:
        closeVal = 1;
        for t in range(len(r)):
            parVal += 1/r[t]
        val = 1/parVal
    elif nCheck == True:
        closeVal = 0
        nCheck = False
        print("Resistors must all be positive values, try again.")
    else:
        closeVal=0
        print('Incorrect input, please try again')
print(val)

#3.6

from math import cos, sin, sqrt
x = [float(m) for m in input("Enter some values, seperated by commas, for which the equation will be evaluated: ").split(',')]
for i in range(len(x)):
    fx = {i: (2*cos(i)+5*sin(cos(5*x)))/(sqrt(abs(sin(4*x)))) for i in range(len(x))}
print(fx)

