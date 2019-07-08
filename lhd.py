import re
import numpy as np
from matplotlib import pyplot as plt
import pylab as pylab

def plotfn(f):
    f = f.replace("^", "**")
    f = f.replace("cos", "np.cos")
    f = f.replace("sin", "np.sin")
    f = f.replace("tan", "np.tan")
    
    x = np.linspace(-15,15,100)
    y = eval(f)

    pylab.plot(x,y)
    pylab.show()


def term(d):
    if d.isdigit():
        print(0)

    else:
        r = re.match(r'(.*)x\^(.*)', d)

        coeff = float(r.group(1))
        power = float(r.group(2))

        derive = str(coeff*power) + 'x^' + str(power-1)

        if (power-1) == 1.0:
            derive = str(coeff*power) + 'x'
        
        elif (power-1) == 0.0:
            derive = str(coeff*power)

        
        print(derive)

def ln(o):

        q = re.match(r'(.*)x\^(.*)', o)
        
        coeff = float(q.group(1))
        power = float(q.group(2))
        
        fx = '(' + str(coeff) + 'x^' + str(power) + ')'
        fprimex = '(' + str(coeff*power) + 'x^' + str(power-1) + ')'
        
        derive = fprimex + '/' + fx 
        print(derive)

def arcsin(a):
        
        asin = re.match(r'(.*)x\^(.*)', a)

        coeff = float(asin.group(1))
        power = float(asin.group(2))

        p1 = '( 1-' + '(' + str(coeff) + 'x^' + str(power) + ')' + '^2' + ')^0.5'
        p2 = '(' + str(coeff*power) + 'x^' + str(power-1) + ')'

        derive = p2 + '/' + p1
        print(derive)

def arctan(t):

        atan = re.match(r'(.*)x\^(.*)', t)

        coeff = float(atan.group(1))
        power = float(atan.group(2))

        p1 = '( 1+' + '(' + str(coeff) + 'x^' + str(power) + ')' + '^2' + ')'
        p2 = '(' + str(coeff*power) + 'x^' + str(power-1) + ')'
    
        derive = p2 + '/' + p1
        print(derive)

