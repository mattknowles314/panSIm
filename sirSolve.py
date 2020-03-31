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

#First we have the parameters for the model, these will be imported from the GUI 
#Pop Stats:
N = 1000 #This is the size of the population
I0 = 1 #Initial number of infected people
R0 = 0 #Initial number of removed people
S0 = N-I0-R0 #Susceptible population initially

#Virus Stats:
b = 0.4 #Rate of infection
c = 0.2 #Rate of recovery
per = 150 #Infection period 


#Now we can make the model using the SIR equations 
t = np.linspace(0,per,per) #Time grid

def sireqs(v,t,N,b,c):
    S,I,R = v #This puts the three values as a vector
    dSdt = -1*b*S*I/N
    dIdt = b*S*I/N - c*I 
    dRdt = c*I
    return dIdt,dRdt,dSdt

#Because in sireqs we gave v=S,I,R as a vector, we do so for initial conditions
v0 = S0,I0,R0 #Initial conditions we gave earlier but as a vector

sirInt = odeint(sireqs, v0,t,args=(N,b,c))
S,I,R = sirInt.T
plt.plot(t,S/1000, 'b')
plt.plot(t,I/1000, 'g')
plt.plot(t,R/1000, 'r')
plt.show()





