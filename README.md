 # Mesh_Network_Visualisation

Mesh network visualisaion formed through painlessMesh Library using python.

## Overview




I have made a Self-assembling mesh network using ESP8266. 1 ESP8266 works as a root node (bridge) between mqtt broker and other ESP8266s work as a node in the mesh. The mqtt broker receives messages from the root node and save it in the text file. Any message from the root node can be broadcast to all node as well as send to a single node. The mqtt broker can send or receive messages by subscribing or publishing a topic respectively. 

To view the mesh structrure i.e. connection between nodes, serially connect the root node (mqtt bridge) with your PC/Laptop via a USB cable. Upload the RootNode sktech from my another repository i.e. [here]([https://github.com/gshubham586/ESP8266MqttMESH_ADHOC](https://github.com/gshubham586/ESP8266MqttMESH_ADHOC)) and run the above python code with few changes as directed in the python program.

## Installations

#### 1. Install python from [here](https://www.python.org/downloads/).

#### 2. Install paho-mqtt
Now you have to install paho python client.This code provides a client class which enable applications to connect to an MQTT broker to publish messages, and to subscribe to topics and receive published messages. you can visit [here](https://pypi.org/project/paho-mqtt/) for installation instructions.

#### 3. Install matplotlib
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. you can visit [here](https://pypi.org/project/matplotlib/) for installation instructions.

#### 4. Install networkx
NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks. you can visit [here](https://pypi.org/project/networkx/) for installation instructions.

#### 5. Install numpy
NumPy is the fundamental package for array computing with Python. you can visit [here](https://pypi.org/project/numpy/) for installation instructions.






