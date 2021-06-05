'''
Name: SFG_search.py
Desriptption: 
Email: yesunhuang@mail.ustc.edu.cn
OpenSource: https://github.com/yesunhuang
Msg: For super computer
Author: YesunHuang
Date: 2021-06-05 21:15:28
'''
#import area
from qutip import*
import numpy as np
from scipy import math

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.pyplot import MultipleLocator

import time

'''
@name: BuildOperator_Exact
@fuction: Helper function for mesolve
@param {float} Ea
@param {float} deltaB
@param {float} g
@return {qobj} operator 
'''
def BuildOperator_Exact(Ea:float,DeltaB:float,g:float):
    Na=int(max(math.ceil(Ea*Ea+6*Ea),4)); Nb=5*psi0_l[1]; Nc=Nb
    psi0=tensor(basis(Na,psi0_l[0]),basis(Nb,psi0_l[1]),basis(Nc,psi0_l[2]))
    a=tensor(destroy(Na),qeye(Nb),qeye(Nc))
    b=tensor(qeye(Na),destroy(Nb),qeye(Nc))
    c=tensor(qeye(Na),qeye(Nb),destroy(Nc))
    H=g*(a.dag()*b*c.dag()+a*b.dag()*c)+Ea*(a.dag()+a)+DeltaB*b.dag()*b
    c_ops=[]
    c_ops.append(np.sqrt(kappa_a)*a)
    c_ops.append(np.sqrt(kappa_b)*b)
    c_ops.append(np.sqrt(kappa_c)*c)
    operator={'Hamilton':H,'Collapse':c_ops,'Initial_state':psi0,'track':[b.dag()*b,\
                                                                          c.dag()*c,\
                                                                          a.dag()*a,\
                                                                          a.dag()*b.dag()*b*a,\
                                                                          a.dag()*c.dag()*c*a,\
                                                                          b.dag()*b.dag()*b*b,\
                                                                          c.dag()*c.dag()*c*c,\
                                                                          a.dag()*a.dag()*a*a]}
    return operator

'''
@name: SearchForMax
@fuction: Search for max
@param {list} array
@return {int} maxIndex
'''
def SearchForMax(array:list):
    max=0
    maxIndex=0
    for i in range(len(array)):
        if array[i]>max:
            max=array[i]
            maxIndex=i
    return maxIndex
#parameters
kappa_a=2;kappa_b=2;kappa_c=2
psi0_l=[0,1,0]
Ea=1
g=1
DeltaB=np.linspace(-4,4,40)
tlist=np.linspace(0,20,2000)

#data storage
data=np.zeros([np.size(DeltaB),9])

#solve for data
ts=time.time()
for j in range(0,np.size(DeltaB)):
    op=BuildOperator_Exact(Ea,DeltaB[j],g)
    output=mesolve(op['Hamilton'],op['Initial_state'],tlist,op['Collapse'],op['track'])
    maxIndex=SearchForMax(output.expect[1])
    data[j][0]=tlist[maxIndex]  #t
    data[j][1]=output.expect[0][maxIndex]   #Nb
    data[j][2]=output.expect[1][maxIndex]   #Nc
    data[j][3]=output.expect[2][maxIndex]   #Na
    data[j][4]=output.expect[3][maxIndex]/(data[j][1]*data[j][3]) #g2ab
    data[j][5]=output.expect[4][maxIndex]/(data[j][2]*data[j][3]) #g2ac
    data[j][6]=output.expect[5][maxIndex]/(data[j][1]*data[j][1]) #g2b
    data[j][7]=output.expect[6][maxIndex]/(data[j][2]*data[j][2]) #g2c
    data[j][8]=output.expect[7][maxIndex]/(data[j][3]*data[j][3]) #g2a
te=time.time()
print('Time cost:'+str(te-ts)+'s')

#save data
np.savetxt('Data/population_g_'+str(g)+'_Ea_'+str(Ea)+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.txt',data)
np.save('Data/population_g_'+str(g)+'_Ea_'+str(Ea)+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.npy',data)

#print population
fig, axes = plt.subplots(3,1 , figsize=(3,18))
axes[0].set_xlabel(r'$\Delta_b$')
axes[1].set_xlabel(r'$\Delta_b$')
axes[1].set_xlabel(r'$\Delta_b$')
axes[0].set_ylabel(r'$\langle b^{\dagger}b\rangle$')
axes[1].set_ylabel(r'$\langle c^{\dagger}c\rangle$')
axes[2].set_ylabel(r'$\langle a^{\dagger}a\rangle$')   
axes[0].plot(DeltaB,data[...,0],linestyle='-')
axes[1].plot(DeltaB,data[...,1],linestyle='-')
axes[2].plot(DeltaB,data[...,2],linestyle='-')
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

