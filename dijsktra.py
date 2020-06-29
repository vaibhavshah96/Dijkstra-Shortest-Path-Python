#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  24 17:52:17 2019

@author: vaibhav
"""

from collections import defaultdict

class Graph():
    def __init__(self):
        
        self.edges = defaultdict(list)
        self.distances = {}
    
    def add_edge(self, from_node, to_node, distance):
       
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


    
def dijsktra(graph, source, destination):

    path_least = {source: (None, 0)}
    processnode = source
    processednode = set()
    total_cost = 0
    while processnode != destination:
        processednode.add(processnode)
        destinations = graph.edges[processnode]
        distanceto_processnode = path_least[processnode][1]

        for next_node in destinations:

            distance = graph.distances[(processnode, next_node)] + distanceto_processnode
            if next_node not in path_least:
                path_least[next_node] = (processnode, distance)
            else:
                least_len_curr = path_least[next_node][1]
                if least_len_curr > distance:
                    total_cost = distance
                    path_least[next_node] = (processnode, distance)
        next_destinations = {node: path_least[node] for node in path_least if node not in processednode}

        processnode = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while processnode is not None:
        path.append(processnode)
        next_node = path_least[processnode][0]
        processnode = next_node
    print(total_cost,"\t \t \t", end =" "),
    print(source + " -->", end =" "),
    for i in range(1,len(path)-1):
        print(path[i] + " -->", end =" "),
    print(destination)