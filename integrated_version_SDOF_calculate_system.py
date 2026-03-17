import numpy as np 
from scipy.integrate import quad

#helikopterin çelik rotor blade'leri var'

p = 1.225
RPM = 150
D = 10
radius =  D / 2
A = np.pi * radius ** 2
Nb = 2
T = 10

alpha = 0.2

Cl = 0.3

b,h= 0.1,0.1

I = (b*h**3) / 12
E = 2 * (10**11)
L = 4.5

k = (3 * E * I) / (L**3)

m = 800

fBPF = Nb * (RPM / 60)

wr = 2 * np.pi * fBPF
wn =  np.sqrt(k / m)

Feff = alpha * 0.5 * p * A * Cl * ((((2*np.pi*RPM)/60)*radius)**2)

r = wr / wn

zeta = 0.1

f = Nb * (RPM / 60)

c = 2 * zeta * np.sqrt(k*m)
phi = np.arctan((2 * zeta * r) / (1 - r**2))

Xdamped = (Feff / k) / np.sqrt(((1 - r ** 2)**2) + ((2 * zeta * r)**2))

def x(t,s='function'):
    global Xdamped,wr,phi

    if s == 'integral':
        return (Xdamped * np.sin((wr * t + phi))) ** 2 
    else:
        return (Xdamped * np.sin((wr * t + phi)))
    
def v(t,s='function'):
    global Xdamped,wr,phi

    if s == 'integral':
        return (wr * Xdamped * np.cos((wr * t) + phi)) ** 2
    else:
        return (wr * Xdamped * np.cos((wr * t) + phi))
    
def a(t,s='function'):
    global Xdamped,wr,phi

    if s == 'integral':
        return ((-wr**2) * Xdamped * np.sin((wr * t) + phi))**2
    else:
        return ((-wr**2) * Xdamped * np.sin((wr * t) + phi))
    

integralX,errorX = quad(x,0,T,args=('integral'))
integralV,errorV = quad(v,0,T,args=('integral'))
integralA,errorA = quad(a,0,T,args=('integral'))

xRMS = np.sqrt((1 / T) * integralX) #yer değiştirme
vRMS = np.sqrt((1 / T) * integralV) #titreşim şiddeti
aRMS = np.sqrt((1 / T) * integralA) #ivme

print(f'yer değiştirme: {xRMS}')
print(f'titreşim şiddeti: {vRMS}')
print(f'ivme: {aRMS}')
