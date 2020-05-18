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
n=512
x=np.linspace(xmin,xmax,n)
dx=(xmax-xmin)/(n-1)
y=np.zeros(n)
for i in range(n):
    y[i]=f(x[i])
karr=2*np.pi*np.fft.fftfreq(n,d=dx)
karr=np.fft.fftshift(karr)
fctr=np.exp(-1j*karr*xmin)
ft=np.fft.fft(y,norm='ortho')
aft=dx*np.sqrt(n/(2*np.pi))*fctr*ft
gft=np.zeros(n)
for i in range(n):
    gft[i]=np.sqrt(2*np.pi)*aft[i]**2
dk=karr[1]-karr[0]
xarr=2*np.pi*np.fft.fftfreq(n,d=dk)
ift=np.fft.ifft(gft,norm='ortho')
fctrx=np.exp(-1j*xarr*xmin)
con=dk*np.sqrt(n/(2*np.pi))*fctrx*ift
plt.scatter(xarr,abs(con),label='Convolution')
x=np.linspace(-2,2,50)
y=np.zeros(50)
for i in range(50):
    y[i]=f(x[i])
plt.plot(x,y,label='Box function')
plt.legend()
