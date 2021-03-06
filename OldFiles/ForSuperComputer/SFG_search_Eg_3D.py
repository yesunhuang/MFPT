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
    Na=int(max(math.ceil(Ea*Ea+6*Ea),4)); Nb=2*psi0_l[1]; Nc=Nb
    psi0=tensor(basis(Na,psi0_l[0]),basis(Nb,psi0_l[1]),basis(Nc,psi0_l[2]))
    a=tensor(destroy(Na),qeye(Nb),qeye(Nc))
    b=tensor(qeye(Na),destroy(Nb),qeye(Nc))
    c=tensor(qeye(Na),qeye(Nb),destroy(Nc))
    H=g*(a.dag()*b*c.dag()+a*b.dag()*c)+Ea*(a.dag()+a)+DeltaB*b.dag()*b
    c_ops=[]
    c_ops.append(np.sqrt(kappa_a)*a)
    c_ops.append(np.sqrt(kappa_b)*b)
    c_ops.append(np.sqrt(kappa_c)*c)
    psiIdeal=tensor(qeye(Na),basis(Nb,psi0_l[2]),basis(Nc,psi0_l[1]))
    idealState=psiIdeal*psiIdeal.dag()
    operator={'Hamilton':H,'Collapse':c_ops,'Initial_state':psi0,'Ideal_state':idealState,'track':[b.dag()*b,\
                                                                                                   c.dag()*c,\
                                                                                                   a.dag()*a,\
                                                                                                   b.dag()*b.dag()*b*b,\
                                                                                                   c.dag()*c.dag()*c*c,\
                                                                                                   b.dag()*c.dag()*b*c,\
                                                                                                   idealState]}
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
psi0_l=[0,3,0]
Ea=np.linspace(1,10,20)
g=np.linspace(0.1,4,20)
DeltaB=0
Ntraj=2000
tlist=np.linspace(0,10,1000)
opts=Options()
opts.store_states=False
#opts.rhs_reuse=True

#data storage
data=np.zeros([np.size(Ea),np.size(g),9])

#solve for data
if __name__=="__main__":
    for i in range(0,np.size(Ea)):
        for j in range(0,np.size(g)):
            op=BuildOperator_Exact(Ea[i],DeltaB,g[j])
            output=mcsolve(op['Hamilton'],op['Initial_state'],tlist,op['Collapse'],op['track'],ntraj=Ntraj,options=opts)
            print(str(Ea[i])+'-'+str(g[j]))
            maxIndex=SearchForMax(output.expect[1])
            data[i][j][0]=tlist[maxIndex]  #t
            data[i][j][1]=output.expect[0][maxIndex]   #Nb
            data[i][j][2]=output.expect[1][maxIndex]   #Nc
            data[i][j][3]=output.expect[2][maxIndex]   #Na
            '''
            rho=output.states[0][maxIndex]*output.states[0][maxIndex].dag()
            for k in range(1,Ntraj):
                rho+=output.states[k][maxIndex]*output.states[k][maxIndex].dag()
            rho=1/Ntraj*rho
            rho_bc=rho.ptrace([1,2])
            data[i][j][4]=entropy_vn(rho_bc) #(A,BC) Entanglement
            '''
            data[i][j][5]=output.expect[6][maxIndex] #Fidelity
            data[i][j][6]=output.expect[3][maxIndex]/(data[i][j][1]*data[i][j][1]) #g2b
            data[i][j][7]=output.expect[4][maxIndex]/(data[i][j][2]*data[i][j][2]) #g2c
            data[i][j][8]=output.expect[5][maxIndex]/(data[i][j][1]*data[i][j][2]) #g2bc

#save data
#np.savetxt('Data/population_g_'+str(g)+'_Ea_'+str(Ea[0])+'-'+str(Ea[-1])+'_DeltaB_'+str(DeltaB[0])+'-'+str(DeltaB[-1])+'.txt',data)
np.save('Data/EgData3D_DeltaB_'+str(DeltaB)+'_Ea_'+str(Ea[0])+'-'+str(Ea[-1])+'_g_'+str(g[0])+'-'+str(g[-1])+'.npy',data)

