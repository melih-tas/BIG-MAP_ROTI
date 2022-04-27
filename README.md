# BIG-MAP_ROTI

The big aim of this project is to control the Rotavapor R-300 from BÜCHI with a PLC. The Rotavapor R-300 cannot be directly accessed via PLC, but with the I-300 Pro extension it is possible to communicate with the R-300 via RESTful API. It is required to enable "OpenInterface" on the I-300 first. 
BÜCHI offers a publicly available github page with instructions to do so:\
https://github.com/buchi-labortechnik-ag/openinterface_rotavapor.git

Now that OpenInterface is enabled, an interaction with python is possible. 
Büchi offers some python examples:\
https://github.com/buchi-labortechnik-ag/openinterface_examples_python.git

The implemented possibilities of the OpenInterface can be found on this Website:\
https://developer.buchi.digital/rotavapor/openinterface/doc/multi.html
## Python

For our case, we need to change some parameters. Here are the python codes used for controlling the R-300:

[Start](python_scripts/start.py)\
[Stop](python_scripts/stop.py)\
[Heating](python_scripts/heating.py)\
[Rotation](python_scripts/rotation.py)\
[Vacuum](python_scripts/vacuum.py)\
[Program](python_scripts/program.py)\
[Rotate](python_scripts/rotate.py)\
[Stop_Rotate](python_scripts/stop_rotate.py)

With an Ethernet connection between Raspberry Pi and R-300, we can now run the python scripts and change the parameters by hand in the code. 

## Node-RED

Node-RED is used for creating a connection between PLC and Raspberry Pi. It is either preinstalled on your Raspberry Pi or can be downloaded from the command line. In Node-RED there are some downloadable contents, which are necessary before a connection can be enabled. These are:
* node-red-contrib-boolean-logic-ultimate
* node-red-contrib-pythonshell
* node-red-contrib-s7
* node-red-dashboard

Node-RED is a visual tool, consisting of function blocks (nodes) and connections. The function blocks receive data, which are then processed and sent to the next block. In this case the tool makes it possible to connect the PLC to the Raspberry Pi.\
The first block (light blue) is the "s7 in" block. This is the block responsible for getting an input from the PLC. The output from "s7 in" leads to the "json" block, automatically transforming a JSON String to a JavaScript Object or the other way around. The next block is "pythonshell in", which can execute python scripts. The last node is "debug", for showing the debug messages.\
For every parameter, a new python script is required, since we cannot insert multiple different inputs from Node-RED in one python script. That is why the same principle is used several times.

<img src="https://user-images.githubusercontent.com/101114939/165498857-3e6aa23b-5360-4f69-812a-0da2c728fb3d.png" width="100%">

Node-RED can be set in auto-start with running the command:

```python
sudo systemctl enable nodered.service
```

## Programmable Logic Controller
