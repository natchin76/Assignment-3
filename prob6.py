#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:33:06 2020
Prob6:Fourier transform of constant function
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
      
xmin=-20
xmax=20
n=50
x=np.linspace(xmin,xmax,n)
dx=(xmax-xmin)/(n-1)
y=np.zeros(n)
for i in range(n):
    y[i]=1
karr=2*np.pi*np.fft.fftfreq(n,d=dx)
fctr=np.exp(-1j*karr*xmin)
ft=np.fft.fft(y)
aft=dx*np.sqrt(n/(2*np.pi))*fctr*ft
plt.scatter(karr,aft)
plt.plot(karr,aft)
plt.show()



