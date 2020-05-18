#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:00:20 2020
DFT using direct method and fft
@author: chintan
"""
import numpy as np
import time
from matplotlib import pyplot as plt
def dft(x):
    n=len(x)
    w=[]
    for i in range(n):
        w.append(0+0j)
    for i in range(n):
        s=0+0j
        for k in range(n):
            s+=1/np.sqrt(n)*x[k]*np.exp(-2j*np.pi*k*i/n)
        w[i]=s
    return(w)
t_dft=[]
t_fft=[]
for n in range(4,20):
    x=np.random.uniform(size=n)
    y=np.random.uniform(size=n)
    z=np.zeros(n)
    for i in range(n):
        z[i]=x[i]+1j*y[i]
    st=time.time()
    d1=dft(z)
    ed=time.time()
    t_dft.append(ed-st)
    st=time.time()
    d2=np.fft.fft(z)
    ed=time.time()
    t_fft.append(ed-st)
n=range(4,20)
plt.plot(n,t_dft,label='Direct method')
plt.plot(n,t_fft,label='FFT method')
plt.legend()
plt.show()        
            
    