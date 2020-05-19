#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:29:56 2020
Convolution of box function with itself
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
def f(x):
    if abs(x)>1:
        return(0)
    return(1)           
xmin=-5
xmax=5
n=256
x=np.linspace(xmin,xmax,n)
dx=(xmax-xmin)/(n-1)
y=np.zeros(n)
for i in range(n):
    y[i]=f(x[i])
ft=np.fft.fft(y,norm='ortho')
gt=ft**2
con=np.sqrt(n)*dx*np.fft.ifft(gt,norm='ortho')
con=np.fft.fftshift(con)
plt.scatter(x,con,label='Convolution')
x=np.linspace(-2,2,50)
y=np.zeros(50)
for i in range(50):
    y[i]=f(x[i])
plt.plot(x,y,label='Box function')
plt.legend()
