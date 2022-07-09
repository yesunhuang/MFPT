import numpy as np
from scipy import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.pyplot import MultipleLocator

import time

g=2
DeltaB_s=-4.0;DeltaB_e=4.0
Ea_s=0.1;Ea_e=1.0
data=np.load('Data/population_g_'+str(g)+'_Ea_'+str(Ea_s)+'-'+str(Ea_e)+'_DeltaB_'+str(DeltaB_s)+'-'+str(DeltaB_e)+'.npy')
DeltaB=np.linspace(DeltaB_s,DeltaB_e,np.size(data,1))
Ea=np.linspace(Ea_s,Ea_e,np.size(data,0))

#print population
fig = plt.figure(figsize=(6,18))
axes=[]
axes.append(fig.add_subplot(3, 1, 1))
axes.append(fig.add_subplot(3, 1, 2))
axes.append(fig.add_subplot(3, 1, 3))
ax0=axes[0].contourf(DeltaB,Ea,data[:,:,0],cmap=cm.coolwarm)
ax1=axes[1].contourf(DeltaB,Ea,data[:,:,1],cmap=cm.coolwarm)
ax3=axes[2].contourf(DeltaB,Ea,data[:,:,2],cmap=cm.coolwarm)
ax00=axes[0].contour(DeltaB,Ea,data[:,:,0],ax0.levels)
ax11=axes[1].contour(DeltaB,Ea,data[:,:,1],ax1.levels)
ax11=axes[2].contour(DeltaB,Ea,data[:,:,2],ax1.levels)
#fmt = '%1.2f '
axes[0].clabel(ax00, ax00.levels, inline=True)
axes[1].clabel(ax11, ax11.levels, inline=True)
axes[2].clabel(ax11, ax11.levels, inline=True)
axes[0].set_xlabel(r'$\Delta_b$');axes[1].set_xlabel(r'$\Delta_b$');axes[2].set_xlabel(r'$\Delta_b$')
axes[0].set_ylabel(r'$E_a$');axes[1].set_ylabel(r'$E_a$');axes[2].set_ylabel(r'$E_a$')
bar1=fig.colorbar(ax0,ax=axes[0],pad=0.1)
bar2=fig.colorbar(ax1,ax=axes[1],pad=0.1)
bar2=fig.colorbar(ax1,ax=axes[2],pad=0.1)
fig.savefig('imgs/population_g_'+str(g)+'_Ea_'+str(Ea[0])+'-'+str(Ea[-1])+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.svg',dpi=600,format='svg',bbox_inches='tight')

#print other data
fig = plt.figure(figsize=(12,18))
axes=[]
for i in range(0,6):
    axes.append(fig.add_subplot(3, 2, i+1))
    ax_s=axes[i].contourf(DeltaB,Ea,data[:,:,(i+4)%9],cmap=cm.coolwarm)
    ax_ss=axes[i].contour(DeltaB,Ea,data[:,:,(i+4)%9],ax_s.levels)
    axes[i].clabel(ax_ss, ax_ss.levels, inline=True)
    axes[i].set_xlabel(r'$\Delta_b$')
    axes[0].set_ylabel(r'$E_a$')
    fig.colorbar(ax_s,ax=axes[i],pad=0.1)
axes[0].set_ylabel(r'$[g_2ab]E_a$')
axes[1].set_ylabel(r'$[g_2ac]E_a$')
axes[2].set_ylabel(r'$[g_2a]E_a$')
axes[3].set_ylabel(r'$[g_2b]E_a$')
axes[4].set_ylabel(r'$[g_2c]E_a$')
axes[5].set_ylabel(r'$[t_max]E_a$')
fig.savefig('imgs/otherData_g_'+str(g)+'_Ea_'+str(Ea[0])+'-'+str(Ea[-1])+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.svg',dpi=600,format='svg',bbox_inches='tight')

