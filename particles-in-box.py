#!/usr/bin/env python3

# For Python 3.5.2, Numpy 1.14.3
# Author: Michal Marszalek
# Script generates system of moving particles (points) confined in a box of a chosen size. When points reach (defined) vicinity of other ones, they form aggregates and continue moving together. Results are stored in xyz file.

import numpy as np
from itertools import combinations

#Parameters

n_mol = 10 #Number of molecules
n_step = 1000 #Number of steps
boundaries = [0.0,30.0]
rad = 2 #Radius of interactions (not recommended to use value lower than 1.75)

#Simulation

origin = np.around(np.random.uniform(boundaries[0],boundaries[1],size=(n_mol,3)), 2)

originlist = origin.tolist()
xyz = open('coordinates.xyz','a+')
xyz.write("%d \nOrigin\n" % n_mol)
for n in range(n_mol):
    xyz.write("H%d %.2f %.2f %.2f\n" % (n+1,originlist[n][0], originlist[n][1], originlist[n][2]))

path = origin
pstep = 0 #Present step

while pstep < n_step - 1: 
    pstep += 1
    
    #Section of interactions

    dictionary = {} #dictionary consisting of positions and coordinates
    step = np.empty(shape=(0,3), dtype=float)

    for x,y in combinations(path, 2):

        if np.linalg.norm(x-y) <= rad: 
            
            pair = []    
            pair.append(np.argwhere(origin == x)[0][0])
            pair.append(np.argwhere(origin == y)[0][0])

            for i in pair:
                if i not in dictionary:
                    vector = np.around(np.random.uniform(-0.5,0.5,size=(1,3)), 2)
                    dictionary.update( { pair[0] : vector } )
                    dictionary.update( { pair[1] : vector } )
                      
                else:
                    dictionary.update( { pair[0] : dictionary[i] } )
                    dictionary.update( { pair[1] : dictionary[i] } )

    #Addition points to dictionary and setting setting final form of particular step (coordinates)
    
    for i in range(n_mol):
        if i not in dictionary:
            addpoint = np.around(np.random.uniform(-0.5,0.5,size=(1,3)), 2)
            dictionary.update( {i : addpoint } )
          
    for key, value in sorted(dictionary.items()):
        step = np.append(step,np.array(value), axis=0)
    path += step    
    
    #Section of points close to boundaries of box
    
    for cord in np.nditer(path, op_flags=['readwrite']):
        if cord > boundaries[1]:
                cord[...] = cord-0.5
        if cord < boundaries[0]:            
                cord[...] = cord+0.5
               
    pathlist = path.tolist()
    xyz.write("%d \nStep number %d\n" % (n_mol, pstep+1))
    for n in range(n_mol):
        xyz.write("H%d %.2f %.2f %.2f\n" % (n+1,pathlist[n][0], pathlist[n][1], pathlist[n][2]))

    if pstep % 100 == 0:
        print('Current step:', pstep)

xyz.close()

