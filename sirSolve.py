"""
We recall the 'SIR' equations
    S' = -bSI/N -> succ
    I' =bSI/N-cI -> infec
    R' = cI -> rem

Where S is the susceptible population, I are those infected, and R is those removed (dead or recovered) and N is the total poulation. 
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def sireqs(y,t,N,b,c):
    S,I,R = y #This puts the three values as a vector
    dSdt = -b*S*I/N
    dIdt = b*S*I/N - c*I 
    dRdt = c*I
    return dSdt, dIdt, dRdt


def makePlot():
    #Because in sireqs we gave v=S,I,R as a vector, we do so for initial conditions
    y0 = S0,I0,R0 #Initial conditions we gave earlier but as a vector
    S,I,R = odeint(sireqs, y0,t,args=(N,b,c)).T

    plt.plot(t,S/1000, 'b', alpha=0.5, lw=2,label = 'Susceptible')
    plt.plot(t,I/1000, 'r', alpha=0.5, lw=2,label = 'Infected') 
    plt.plot(t,R/1000, 'g', alpha=0.5, lw=2,label = 'Removed')
    plt.xlabel('Time/days')
    plt.ylabel('Number of each parameter /1000s')
    legend =plt.legend()
    
    plt.savefig("figs/plot.png")
    #plt.show() This could be used to display the graph





