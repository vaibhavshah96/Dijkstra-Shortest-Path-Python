#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  24 17:48:08 2019

@author: vaibhav
"""

import numpy as np
import dijsktra as dj

val = input("Enter your value: ")
print("\n \n")

val_array = val.split()
numNodes = int(val_array.pop(0))
len(val_array)
Source_from = val_array.pop(len(val_array)-2)
Dest_to = val_array.pop(len(val_array)-1)
val = val_array
val = np.asarray(val)
val = val.reshape(-1,3)
val = val.tolist()

for i in range(len(val)):
    for j in range(len(val[i])):
        if(j == 2):
            val[i][j] = int(val[i][j])

graph = dj.Graph()
for edge in val:
    graph.add_edge(*edge)
print("Source \t Destination \t Distance Between Them \t Route")   
print(Source_from,"\t" ,Dest_to, "\t \t", end=" ")
dj.dijsktra(graph, Source_from, Dest_to)    