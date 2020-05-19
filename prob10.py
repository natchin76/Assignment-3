#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:25:06 2020
Prob 10: Power spectrum and periodogram
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
fname='prob10.txt'
data=np.loadtxt(fname,usecols=0)
n=len(data)
x=np.arange(1,513)
plt.scatter(x,data)
plt.title('data')
plt.show()
dft=np.fft.fftshift(np.fft.fft(data,norm='ortho'))
karr=np.fft.fftfreq(n)
karr=np.fft.fftshift(karr)
plt.plot(karr,dft)
plt.title('dft of data')
plt.show()
P_k=(abs(dft))**2/n
plt.plot(karr,P_k)
plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Power spectrum')
plt.grid()
plt.show()
##Binning
l=10
m=int(n/l)
ndata=data[0:510].reshape([m,l])
Pk1=np.zeros([m,l])
knew=np.fft.fftfreq(m)
knew=np.fft.fftshift(knew)
for i in range(l):
    dft_temp=np.fft.fftshift(np.fft.fft(ndata[:,i],norm='ortho'))
    Pk1[:,i]=(abs(dft_temp))**2/m
Pk_n=np.zeros(m)
for i in range(m):
    Pk_n[i]=sum(Pk1[i,:])/l
plt.plot(knew,Pk_n)
plt.xlabel('k')
plt.ylabel('P(k)')
plt.title('Power spectrum by Bartlett method')
plt.show()
