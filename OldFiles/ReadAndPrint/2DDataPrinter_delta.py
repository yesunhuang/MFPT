import numpy as np
from scipy import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.pyplot import MultipleLocator

import time

#load data
g=1
Ea=1
DeltaB_s=-4.0;DeltaB_e=4.0
data=np.load('Data/population_g_'+str(g)+'_Ea_'+str(Ea)+'_DeltaB_'+str(DeltaB_s)+'-'+str(DeltaB_e)+'.npy')
DeltaB=np.linspace(DeltaB_s,DeltaB_e,np.size(data,0))

#print population
fig, axes = plt.subplots(3,1 , figsize=(3,18))
axes[0].set_xlabel(r'$\Delta_b$')
axes[1].set_xlabel(r'$\Delta_b$')
axes[1].set_xlabel(r'$\Delta_b$')
axes[0].set_ylabel(r'$\langle b^{\dagger}b\rangle$')
axes[1].set_ylabel(r'$\langle c^{\dagger}c\rangle$')
axes[2].set_ylabel(r'$\langle a^{\dagger}a\rangle$')   
axes[0].plot(DeltaB,data[...,1],linestyle='-')
axes[1].plot(DeltaB,data[...,2],linestyle='-')
axes[2].plot(DeltaB,data[...,3],linestyle='-')
fig.savefig('imgs/population_g_'+str(g)+'_Ea_'+str(Ea)+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.svg',dpi=600,format='svg',bbox_inches='tight')

#print other data
fig, axes = plt.subplots(3,2,figsize=(12,18))
axes[0,0].set_xlabel(r'$\Delta_b$')
axes[0,1].set_xlabel(r'$\Delta_b$')
axes[1,0].set_xlabel(r'$\Delta_b$')
axes[1,1].set_xlabel(r'$\Delta_b$')
axes[2,0].set_xlabel(r'$\Delta_b$')
axes[2,1].set_xlabel(r'$\Delta_b$')
#axes[0,1].set_ylim(0,5)
#axes[1,0].set_ylim(0,2)
#axes[1,1].set_ylim(0,2)
#axes[2,0].set_ylim(0,2)
axes[0,0].plot(DeltaB,data[...,4],linestyle='-.')
axes[0,1].plot(DeltaB,data[...,5],linestyle='-.')
axes[1,0].plot(DeltaB,data[...,8],linestyle='-.')
axes[1,1].plot(DeltaB,data[...,6],linestyle='-.')
axes[2,0].plot(DeltaB,data[...,7],linestyle='-.')
axes[2,1].plot(DeltaB,data[...,0],linestyle='-.')
axes[0,0].set_ylabel(r'$g_2ab$')
axes[0,1].set_ylabel(r'$g_2ac$')
axes[1,0].set_ylabel(r'$g_2a$')
axes[1,1].set_ylabel(r'$g_2b$')
axes[2,0].set_ylabel(r'$g_2c$')
axes[2,1].set_ylabel(r'$t_max$')
fig.savefig('imgs/otherData_g_'+str(g)+'_Ea_'+str(Ea)+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.svg',dpi=600,format='svg',bbox_inches='tight')