#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:50:47 2020
Prob4: Fourier transform of gaussian
@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
fname='prob4.txt'
ft_c=np.loadtxt(fname,usecols=0)
k_c=np.loadtxt(fname,usecols=1)
def f(k):
    return(1/np.sqrt(2)*np.exp(-k**2/4))
plt.scatter(k_c,ft_c)
k=np.linspace(-8,8,50)
plt.plot(k,f(k))
plt.show()
