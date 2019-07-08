#file path: C:\Users\amber\OneDrive\Desktop\Programming\pythonPractice

import numpy as np
from sympy import *
import math
#ix,iy,iz,bx,by,bz,Ttx,Tty,Ttz,k = symbols('ix iy iz bx by bz Ttx Tty Ttz k')
#init_printing(use_unicode=True)

#magnetic field inputs: each dimension in
# def torque(bx,by,bz):
#
# #Magnetic Field Components (Input)
#     b = np.array([[bx,by,bz]])
#
# #Current Components
#     ix_max = 0.16/5
#     iy_max = 0.16/5
#     iz_max = 0.23/5
#
# #Moment Dipole Components
#     mx = (0.3/0.032) * ix_max
#     my = (0.3/0.032) * iy_max
#     mz = (0.3/0.032) * iz_max
#
#     m = np.array([[mx,my,mz]])
#     t = np.cross(m,b)
#     return t

###FIX THIS INTO SYMBOLIC REPRESENTATION USING sympy
# k = 0.3/0.032
# E1 = k*iy*bz-k*iz*by-Ttx
# E2 = -k*iz*bx+k*ix*bz-Tty
# E3 = k*ix*by-k*iy*bx-Ttz
# M = Matrix([[E1],[E2],[E3]])

#print(solve([E1, E2, E3],[ix,iy,iz]))
#print(solve(M,freevar=False))


def current_required(bx,by,bz,Tmx,Tmy,Tmz):
    ##Define constant 0.3 and 0.032
    ##Output iz
    ## max nomial magnetic dipole strength in x and y and z = 0.3 Am^2
    ## max power consumption of x and y magnetorquer coils @ 5V and 160mW --> i=P/V --> max current of 0.0032
    ## max power consumption of z magnetorquer coil @ 5V and 230mW --> i=P/V --> max current of 0.0046
    mi_ratio_xy = 0.3/0.032
    mi_ratio_z = 0.3/0.046

    #iz = 0.5
    #ix = ((Tbz)/mi_ratio) + bx*((((Tbx)/mi_ratio)+(iz*by))/(bz))/(by)
    #iy = (((Tbx)/mi_ratio)+(iz*by))/(bz)
    #iz is a free variable : iz = (bz*(bx*((((Ttx)/k)+(iz*by))/(bz))/(by)) - ((Ttx)/k))/(bx)
    iz = 0.046 # <-- arbitrary as free variable (max current for Z magnetorquer)
    ix = ((Tmx)+(mi_ratio_z*iz*by))/(mi_ratio_xy*bz)
    iy = ((Tmy)+(mi_ratio_z*iz*bx))/(mi_ratio_xy*bz)

    mx = mi_ratio_xy*ix
    my = mi_ratio_xy*iy
    mz = mi_ratio_z*iz

    Tm = np.array([[Tmx,Tmy,Tmz]])
    b = np.array([[bx,by,bz]])
    m = np.array([[mx,my,mz]])
    Treq = np.cross(m,b)

#Compare the matricies to check for equivalence
    if np.all(Treq == Tb):
        print("true")
        print(ix,iy,iz)
    else:
        print("false")
        print(ix)

# ##Rotation Matrix
# def rotation(thetaX,thetaY,thetaZ):
#     rotx = np.array([[1,0,0],[0,cos(math.radians(thetaX)),sin(math.radians(thetaX))],[0,-sin(math.radians(thetaX)),cos(math.radians(thetaX))]])
#     roty = np.array([[cos(math.radians(thetaY)),0,sin(math.radians(thetaY))],[0,1,0],[-sin(math.radians(thetaY)),0,cos(math.radians(thetaY))]])
#     rotz = np.array([[cos(math.radians(thetaZ)),-sin(math.radians(thetaZ)),0],[sin(math.radians(thetaZ)),cos(math.radians(thetaZ)),0],[0,0,1]])
#     print(rotx)
#     print(roty)
#     print(rotz)

#Later this is constant input
while(1):
    current_required(int(input("bx: ")),int(input("by: ")),int(input("bz: ")),int(input("Ttx: ")),int(input("Tty: ")),int(input("Ttz: ")))
    # rotation(int(input("thetaX: ")),int(input("thetaY: ")),int(input("thetaZ: ")))


#Want to rotate some angle per second
#Using rate at what we want to rotate and magnetic field vectors find the current required to do so

##SN: z = 103.3 OHM , x = 163, y=168

#Need magnetic field vector

#Utilize 1 or both magnetorquers that are orthogonal to magnetic field to rotate desired angle

#Determine which one to turn on and how much current to apply





# #{%Variables and Constants
#
# %Earth magnetic field components
# Bx = - (0 + (2*power(10,-7)) .*rand(1))
# By = - (0 + (2*power(10,-7)) .*rand(1))
# Bz = - (0 + (2*power(10,-7)) .*rand(1))
#
# %Earth magnetic field vector
# B = [Bx;By;Bz]
#
# %Current components (for each magnetorquer)
# ix_max = (0.13/5) + (0.16/5 - 0.13/5) .*rand(1)
# iy_max = (0.13/5) + (0.16/5 - 0.13/5) .*rand(1)
# iz_max = (0.20/5) + (0.23/5 - 0.20/5) .*rand(1)
#
# %Moment dipole components
# Mx = (0.3/0.032) * ix_max
# My = (0.3/0.032) * iy_max
# Mz = (0.3/0.032) * iz_max
#
# %Moment dipole vector
# M = [Mx;My;Mz]
#
#
# %Computations
#
# %Torque
# cross(M,B)
