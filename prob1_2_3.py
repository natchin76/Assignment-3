#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:09:14 2020
Prob1: Fourier transform of sinc function
I imported the results from C file here to plot
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return(np.sin(x)/x)
def ft_ext(k):
    if abs(k)>1:
        return(0)
    return(np.sqrt((np.pi)/2))        
xmin=-50
xmax=50
n=256
x=np.linspace(xmin,xmax,n)
dx=(xmax-xmin)/(n-1)
y=f(x)
karr=2*np.pi*np.fft.fftfreq(n,d=dx)
fctr=np.exp(-1j*karr*xmin)
ft=np.fft.fft(y,norm='ortho')
aft=dx*np.sqrt(n/(2*np.pi))*fctr*ft
plt.scatter(karr,aft,label='using dft')
k=np.linspace(-2,2,50)
ft=[]
for i in range(50):
    ft.append(ft_ext(k[i]))
plt.plot(k,ft,label='analytical')
plt.legend()
plt.show()
#data imported from FFTW file
fname='prob2.txt'
ft_c_2=np.loadtxt(fname,usecols=0)
k_c_2=np.loadtxt(fname,usecols=1)
#data imported from gsl file
fname='prob3.txt'
ft_c_3=np.loadtxt(fname,usecols=0)
plt.scatter(karr,aft,label='using dft')
plt.scatter(k_c_2,ft_c_2,label='using FFTW')
plt.scatter(k_c_2,ft_c_3,label='using GSL')
plt.legend()
plt.show()
plt.scatter(k_c_2,ft_c_2,label='using FFTW')
plt.legend()
plt.show()
plt.scatter(k_c_2,ft_c_3,label='using GSL')
plt.legend()
plt.show()



