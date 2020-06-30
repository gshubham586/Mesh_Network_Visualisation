# This program gives the mesh structure in network form with the nodeId.
import serial
import time
import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Check your ESP8266 module COM port and write below. 

serialArduino = serial.Serial('COM5', 115200)        

def recursive_node_mapping(obj, currentNodeId, graph):
        # if the object is a dictionary, then it contains a "nodeId", and its "subs" subconnection list
    if isinstance(obj, dict):
        # direct neighbour of the current_node
        neighbourNodeId = obj["nodeId"]

        print (neighbourNodeId)
        graph.add_edge(currentNodeId, neighbourNodeId)

        # go into the node's subconnections
        for item in obj["subs"]:
            recursive_node_mapping(item, neighbourNodeId, graph)

    # if the object is a list, then it is a list of dictionaries
    elif isinstance(obj, list):
        for item in obj:
            recursive_node_mapping(item, currentNodeId, graph)
            
old_mesh_Topo = """[]"""
new_mesh_Topo = """[]"""
while True:
        while (serialArduino.inWaiting() == 0):
            pass
        valueRead =(serialArduino.readline())
        valueRead = valueRead.decode("utf-8")
        print(valueRead)                                 #Print Serial data
        if valueRead.startswith('{'):
            mesh = valueRead.replace('"root":true,','')
            mesh_split = mesh.split('{')
            for x in range(0,len(mesh_split)):
                if ('subs' not in  mesh_split[x]):
                    find = mesh_split[x].find('}')
                    if (find !=-1):
                        mesh_split[x] = mesh_split[x][ : find] + ""","subs":[]""" + mesh_split[x][find : ]
            new_mesh_Topo = "[" + '{'.join(mesh_split) + "]"
            print(new_mesh_Topo)
        if (old_mesh_Topo != new_mesh_Topo):
            plt.clf()
            jsonString = json.loads(new_mesh_Topo)
            graph = nx.Graph()
            recursive_node_mapping(jsonString, 11111, graph)          # Here 11111 node id is showing connection with Raspberrypi/PC, only for refernece.
            pos = nx.random_layout(graph, center=(1,1))
            nx.draw(graph, with_labels=True, node_size=400, node_color="skyblue", node_shape="o", alpha=0.6, linewidths=1)
            plt.show()
            old_mesh_Topo = new_mesh_Topo
            
         







            
    
