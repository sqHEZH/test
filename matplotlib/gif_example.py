#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:52:40 2018

@author: hezhu
"""

import numpy as np     
from matplotlib import pyplot as plt     
from matplotlib import animation     
    
# first set up the figure, the axis, and the plot element we want to animate     
fig = plt.figure()   
ax1 = fig.add_subplot(2,1,1,xlim=(0, 2), ylim=(-4, 4))  
ax2 = fig.add_subplot(2,1,2,xlim=(0, 2), ylim=(-4, 4))  
line, = ax1.plot([], [], lw=2)    
line2, = ax2.plot([], [], lw=2)    
def init():    
    line.set_data([], [])    
    line2.set_data([], [])    
    return line,line2  
  
# animation function.  this is called sequentially     
def animate(i):  
  
    x = np.linspace(0, 2, 100)     
    y = np.sin(2 * np.pi * (x + 0.01 * i))    
    line.set_data(x, y)        
  
  
    x2 = np.linspace(0, 2, 100)     
    y2 = np.cos(2 * np.pi * (x2 - 0.01 * i))* np.sin(2 * np.pi * (x - 0.01 * i))    
    line2.set_data(x2, y2)     
    return line,line2  
  
anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=100, interval=100)    
Writer = animation.writers['imagemagick_file']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
anim1.save('im.gif', writer=writer)
plt.show()

