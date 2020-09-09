import sympy as sp
from sympy import Eq,solve,symbols
import math 
[a,b,c]=[-1,-5,-10]
l,x,y,z=symbols('l,x,y,z')
[x,y,z]=[2+3*l,-1+4*l,2+2*l]
r=solve(Eq(x-y+z-5,0),l)
[x,y,z]=[2+3*r[0],-1+4*r[0],2+2*r[0]]
d=math.sqrt(pow(x-a,2)+pow(y-b,2)+pow(z-c,2))
print('Distance between point of intersection of line and plane with given point',d)
