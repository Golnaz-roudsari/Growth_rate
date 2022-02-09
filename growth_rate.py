#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:10:21 2021

@author: roudasri
"""
import os
import numpy as np 
import matplotlib.pyplot as plt 
plt.rcParams["font.family"] = "Arial"



#%%%

path = "/home/roudasri/Python_codes/Growthrate_Cubic_Hexagonal/growthrate_data/"
# Change the directory
rates=os.listdir(path)
ang=['62','30','45','70','32','73'] 
wt=[15000,3100,-100,14100, 35000,14000]
#boxlocx= [40,12.5,25,13,25.5,13] 
#boxlocy= [42500,7250,2670,15100,56900,15000] 
for i in range(6):
    dataArray=np.loadtxt(path+rates[i])
    plt.figure(figsize=(4,2.5), dpi=100)
    plt.plot(dataArray[:,0], dataArray[:,1],'r',label='$I_c$',linewidth=2, markersize=4)
    plt.plot(dataArray[:,0], dataArray[:,2],'b',label='$I_h$',linewidth=2, markersize=4)
    plt.plot(dataArray[:,0], dataArray[:,2]+dataArray[:,1],'k',label='$I_c+I_h$',linewidth=2, markersize=4)
    plt.axhline(y=wt[i], color='g', label='wedge top', linestyle='--',linewidth=2, markersize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylim(-10)
#    plt.text(boxlocx[i], boxlocy[i], ang[i]+'$^\circ$', size=15, ha="right", va="top", bbox=dict(boxstyle="square", alpha=0.5, ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),) )
    plt.ylabel('Number of Ice Molecules',fontsize=14)
    plt.xlabel('Time (ns)',fontsize=14)
#    plt.legend(loc='upper center',ncol=4, shadow= True, bbox_to_anchor=(0.5,1.15),borderpad=0.2, prop={'size':8})
    plt.grid()

    plt.savefig('growth'+ang[i], bbox_inches='tight')
    plt.show()

      



