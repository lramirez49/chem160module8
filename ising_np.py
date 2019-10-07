def neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+n//2,axis=0),shift=-y+n//2,axis=1)
    return arr[:n,:n]
from random import choice,random
import numpy as np
from math import exp
Temp=0 # Temperature
n=20
zone=3
n2=n*n
nlist=list(range(n))
ntrials=200000
nequil=100000
while Temp<10.:
    Temp+=0.2
    # Initialize sums for averages
    E_sum=0.0
    E2_sum=0.0
    spins=np.full((n,n),1)
    for trial in range(1,(ntrials+nequil+1)):
        # Randomly pick a site
        i=choice(nlist)
        j=choice(nlist)
        deltaE=2*spins[i][j]*(neighbors(spins,i,j,zone).sum()-spins[i][j])
        if exp(-deltaE/Temp)>random():
            spins[i][j]=-spins[i][j]
        else:
            deltaE=0.0
            if trial == nequil:
                energy=0.0
                for i in range(n):
                    for j in range(n):
                        energy-=spins[i][j]*(neighbors(spins,i,j,zone).sum()
                                            -spins[i][j])
                energy/=n2
            if trial > nequil:
                energy+=2*deltaE/n2
                E_sum+=energy
                E2_sum+=energy*energy
    E_ave=E_sum/ntrials
    E2_ave=E2_sum/ntrials
    Cv=1./(Temp**2)*(E2_ave-E_ave*E_ave)
    print('%8.4f %10.6f %10.6f'%(Temp, E_ave, Cv))