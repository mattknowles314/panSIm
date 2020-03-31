"""
We recall the 'SIR' equations
    S' = -BSI -> succ
    I' =BSI-cI -> infec
    R' = cI -> rem

Where S is the susceptible population, I are those infected, and R is those removed (dead or recovered)
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Constants, these will be imported from the GUI 

S = 100
I = 0
R = 0

B = 3.0
c = 0.2

# Solve the equations

def succ(S,I,R,B,c):
        dSdt = -1*B*S*I
        return dSdt

t = np.linspace(0,20)
S = odeint(succ, 100, t)

plt.plot(t,y)
plt.show()

