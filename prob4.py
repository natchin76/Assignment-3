import numpy as np
from matplotlib import pyplot as plt
fname='prob4.txt'
ft_c=np.loadtxt(fname,usecols=0)
k_c=np.loadtxt(fname,usecols=1)
def f(k):
    return(1/np.sqrt(2)*np.exp(-k**2/4))
plt.scatter(k_c,ft_c,label='using FFTW')
k=np.linspace(-8,8,50)
plt.plot(k,f(k),label='Analytical')
plt.legend()
plt.show()
