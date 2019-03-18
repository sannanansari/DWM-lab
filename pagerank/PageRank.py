# -*- coding: utf-8 -*-
import numpy as np

x = int(input('Enter the no. of len of input'))
d = 0.85
eps = 1.0e-8
print("\nPlease enter the adjacency matrix for network")
mat = []
for i in range(0,x):
    l = []
    for j in range(0,x):
        l.append(int(input('Enter the matrix'+str(i+1)+','+str((j+1))+' ')))
    mat.append(l)

        
outboundL = np.zeros((x,),dtype=int)
for i in range(0,x):
   for j in range(0,x):
       if(mat[i][j]==1):
           outboundL[i]+=1

M=np.zeros((x,x))
for i in range(0,x):
    for j in range(0,x):
        if(mat[j][i]==1):
            M[i][j]=1/outboundL[j]
col=np.ones((x,1))
onecolmat = np.matrix(np.ones((x,1),dtype=int))

r=np.full((x,1),1/x)           

while True:
    rnext = d*np.dot(M,r)+((1-d)/x)*onecolmat
    diff = np.subtract(rnext,r)
    if np.linalg.norm(diff)<eps:
        break
    r = rnext
                                                                                                                                    
    
    
