import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
import math
#
#   Simulates a geometric Brownian motion with M time steps. Produces 100 paths and creates a
#   plot of fifty of them.
#
#   Each time step is one day. Assumes 250 trading days per year. 
#
#   Adapted from Yves Hilpisch (see bibliography)
#
sigma=0.1        # Volatility
r=0.05           # Interest rate
S0=100.0         # Initial index value
T=10             # Number of years
I=100            # Number of simulated paths
M=250*T          # Number of time steps
dt=1/250         # Length of timeinterval
#
S=np.zeros((M+1,I))   # Two dimensional NumPy array of index levels. Note the use of a tuple!
S[0]=S0
#
#   The loop below is partly parallelised with I random numbers generated at each increment.
#
for t in range(1,M+1):
    S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*npr.standard_normal(I))
#
plt.figure(figsize=(10,6))
plt.plot(S[:,:50],lw=1.5)
plt.title('Geometic Brownian Motion Simulation',fontweight='bold',fontsize=16)
plt.xlabel('Time step',fontweight='bold',fontsize=12)
plt.ylabel('Index level',fontweight='bold',fontsize=12)
plt.xticks(np.arange(0,2750,250))
plt.show()
                       
