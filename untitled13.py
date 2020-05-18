#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:41:11 2020

@author: krishnendu
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
y=np.loadtxt('prob10.txt',usecols=0)
n=len(y)
print(n)
y1=y[0:510].reshape(10,51)

print(y1)
f=np.zeros(n)

for i in range(n):
    
        f[i]=sum(y[:n-i]*y[i:])/n
 
    
fk=np.fft.fft(f)
fk=np.fft.fftshift(fk)
k=np.fft.fftfreq(n,1)
k=np.fft.fftshift(k)

fk1=np.fft.fft(y,norm="ortho")
fk1=(abs(fk1))**2/n
f2=np.zeros(510).reshape(10,51)
fk2=np.zeros(510).reshape(10,51)

for j in range(10):
    for i in range(51):
         f2[j][i]=sum(y1[j][:51-i]*y1[j][i:])/51
         
    fk2[j]=np.fft.fft(f2[j])
    fk2[j]=np.fft.fftshift(fk2[j])   
    
fk2=sum(fk2[:,])/10

k2=np.fft.fftfreq(51,1)
k2=np.fft.fftshift(k2)

    
fs=1
fp,pxx_den=signal.periodogram(y,fs,scaling="spectrum",return_onesided=False )
plt.plot(fp,abs(pxx_den))
plt.show()

plt.plot(k,abs(fk))
plt.show()
plt.plot(k,fk1)
plt.show()
plt.plot(k2,abs(fk2))
plt.show()