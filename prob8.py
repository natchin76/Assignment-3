#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:44:03 2020
2d FT
@author: chintan
"""
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
def f(x,y):
    return(np.exp(-(x**2+y**2)))
def fk_ext(kx,ky):
     kx,ky=np.meshgrid(kx,ky)
     return np.exp(-(kx**2+ky**2)/4)/2   
xmin=-25
xmax=25
ymin=-25
ymax=25
n=128
a=np.zeros([n,2])
dx=(xmax-xmin)/(n-1)
dy=(ymax-ymin)/(n-1)
xarr=np.linspace(xmin,xmax,n)
yarr=np.linspace(ymin,ymax,n)
X, Y = np.meshgrid(xarr, yarr)
f_x=f(X,Y)
f_q=np.fft.fft2(f_x,norm='ortho')
kxarr=2*np.pi*np.fft.fftfreq(n,d=dx)
kyarr=2*np.pi*np.fft.fftfreq(n,d=dy)
fctrx=np.exp(-1j*kxarr*xmin)
fctry=np.exp(-1j*kyarr*ymin)
aft=(dx*dy*(n/(2.0*np.pi))*fctrx*fctry*f_q)
Kx, Ky=np.meshgrid(kxarr,kyarr)

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.gca(projection='3d')
ax.set_xlabel("kx")
ax.set_ylabel("ky")
surf = ax.contour3D(Kx, Ky, abs(aft),100)
plt.title('Using FFT2')
plt.show()

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.gca(projection='3d')
ax.set_xlabel("kx")
ax.set_ylabel("ky")
surf2 = ax.contour3D(Kx, Ky, fk_ext(kxarr,kyarr),100)
plt.title('Analytical')
plt.show()
