from math import*
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu k�lje pikkus => '))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu �mberm��t", round(P,1))
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristk�liku karakteristikud")
b=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S=b*c
print("Ristk�liku pindala", round(S,1))
P=2*(b+c)
print("Ristk�liku �mberm��t", P)
di=sqrt(b**2+c**2)
print("Ristk�liku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus =>"))
d=2*r
print("Ringi l�bim��t", round(d,1))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))


import math
from random import *
#7
a1=randint(1,50)
a2=randint(1,50)
a3=randint(1,50)
a4=randint(1,50)
a5=randint(1,50)
keskmine=(a1+a2+a3+a4+a5)/5
print("Arvud:",a1,a2,a3,a4,a5,"Nende keskmine on",keskmine)



#8
print("@..@".center(10,))
print("(----)".center(10,))
print("( \__/ )".center(10,))
print(" ^^ "" ^^ ".center(10,))
