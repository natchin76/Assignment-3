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
xmin=-15
xmax=15
ymin=-15
ymax=15
n=64
a=np.zeros([n,2])
dx=(xmax-xmin)/(n-1)
dy=(ymax-ymin)/(n-1)
a[:,0]=np.linspace(xmin,xmax,n)
a[:,1]=np.linspace(ymin,ymax,n)
f_x=np.zeros([n,n])
for i in range(n):
    for j in range(n):
        f_x[i,j]=f(a[i,0],a[j,1])
f_q=np.fft.fft2(f_x,norm='ortho')
kxarr=2*np.pi*np.fft.fftfreq(n,d=dx)
kyarr=2*np.pi*np.fft.fftfreq(n,d=dy)
fctrx=np.exp(-1j*kxarr*xmin)
fctry=np.exp(-1j*kyarr*ymin)
aft=np.zeros([n,n])
for i in range(n):
    for j in range(n):
        aft[i][j]=dx*dy*n/(2*np.pi)*fctrx[i]*fctry[j]*f_q[i,j]

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(kxarr, kyarr, aft)
plt.show()

