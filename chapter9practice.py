import sympy

#PARTIAL FRACTIONS, ROOTS, EXPANSION, ALGEBRAIC EQUATIONS
#Example 9.1 
    #Create Partial Fractions of the given rational function

x = sympy.symbols('x') #sets up sympy variables for use in equation

expr1 = sympy.apart((20*x**2+3)/(x**6 + 3*x**5 - 75*x**4 - 155*x**3 + 1194*x**2 + 1272*x - 2240)) #partial fractions to rational functions

print('\n{}'.format(expr1))

#Example 9.2
    #Expand and find roots of algebraic expressions

x, y = sympy.symbols('x, y') #set up sympy variables

expr1 = sympy.expand(2*x*(y-1) + 2*x*(x+y)) #expand equation

print('\nexpansion: {}'.format(expr1))

expr2 = sympy.solve(x**4 - 15*x**2 + 10*x + 24)#determine roots

print('\nroots: {}'.format(expr2))


#LIMITS
#Example 9.3
    #calculate the limit of the given functions

sympy.symbols('x')
#limit(expression, variable, limit to)
expr1 = sympy.limit(sympy.sin(5*x)/(6*x), x, 0)

print('\nlim1: {}'.format(expr1))

expr2 = sympy.limit((3*x**2 + 7*x + 8)/(6*x), x, 0)

print('\nlim2: {}'.format(expr2))

#DERIVATIVES
#Example 9.4
    #Calculate the first and second derivative of the given expression

x = sympy.symbols('x')

#diff(expression, variable, order
expr1 = sympy.diff(2*sympy.sin(x)*sympy.cos(6*x), x)

print("\nf': {}".format(expr1))

expr2 = sympy.diff(2*sympy.sin(x)*sympy.cos(6*x), x, 2)

print("\nf'': {}".format(expr2))

#INTEGRALS
    #integrate the two given functions

x = sympy.symbols('x')

#integrate(expression, variable, limits (if present))
#or
#integrage(expression, (variable, up limit, low limit), (second variable, up limit, low limit))

f1x = sympy.integrate(2*x**2 + sympy.cos(x), x)

print('\nf1(x) = {}'.format(f1x))

f2xy = sympy.integrate(2*x*y + 4*sympy.sin(x), (x, 0, 3), (y, 0, 2))

print('\nf2(x,y) = {}'.format(f2xy))

#ODEs
    #Determine the solution of the given differential equations

x,y = sympy.symbols('x, y')

#eq(equation derivative
#dsolve(Eq, func, hint)

f = sympy.Function('f')

eq = sympy.Eq(f(x).diff(x) + 3*f(x), 3)

f1 = sympy.dsolve(eq, f(x))

print('\nf1 = {}'.format(f1))

eq = sympy.Eq(f(x).diff(x, x) + f(x), 2)

f2 = sympy.dsolve(eq, f(x))

print('\nf2 = {}'.format(f2))

#EQUATION EVALUATION
    #Eval the values of the given equations at required points

#evalf(subs = {x: 1, y:2}

x,y = sympy.symbols('x, y')

f1 = 2*x**2 + sympy.cos(sympy.sin(3*x))

f1Soln = f1.evalf(subs = {x:2.34})

print('\nf1 = {}'.format(f1Soln))

f2 = (6*x*sympy.cosh(x) + 3*y*sympy.sin(x))/(2*x + 3*y)

f2Soln = f2.evalf(subs = {x:2.0, y:1.2})

print('\nf2 = {}'.format(f2Soln))
