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

* [Start](python_scripts/start.py)
* [Stop](python_scripts/stop.py)
* [Heating](python_scripts/heating.py)
* [Rotation](python_scripts/rotation.py)
* [Vacuum](python_scripts/vacuum.py)
* [Program](python_scripts/program.py)
* [Rotate](python_scripts/rotate.py)
* [Stop_Rotate](python_scripts/stop_rotate.py)

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

The red "Filter" node receives the input "true" or "false". 
* When "true", output 1 is "true" and output 2 is nothing.
* When "false", output 1 is nothing and output 2 is "false".

The yellow block changes the output message, everytime the state changes from true to false or in reverse. In this case the output string is "Dry" or "Manual" for choosing a program. 

<img src="https://user-images.githubusercontent.com/101114939/165498857-3e6aa23b-5360-4f69-812a-0da2c728fb3d.png" width="100%">

Node-RED can be set in auto-start with running the command:

```python
sudo systemctl enable nodered.service
```

## Programmable Logic Controller

A Siemens PLC is being used in this project. It is a SIMATIC ET 200SP. The power supply is a SITOP PSU100S. The needed input is AC 120/230 V and the given output is DC 24 V/5 A. The programming of the PLC is taking place in TIA Portal V15.1.

<img src="https://user-images.githubusercontent.com/101114939/165723514-2be1792b-7a0d-4e0f-89c0-0bbf47b50346.jpg" width="50%">

## Communication

This diagram shows the flow process of the communication. The dots signalize the wireless connections, whereas the solid lines signalize the cable connections. It all starts with a manual input in the HMI (Human Machine Interface). The PLC is sending this data to Node-RED with being in the same network. Node-RED is then processing this data and runs the different python scripts with the given inputs. The R-300 receives these commands and can be controlled like that. 

<img src="https://user-images.githubusercontent.com/101114939/165900971-f0ee3757-d655-4a68-8be3-8a27d537c39f.PNG" width="50%">

## Fastening mechanism

Thus far, the Roti is able to be controlled via PLC. For making it more autonomous, the process of fastening and releasing the flask must be automated as well. This requires some form of external effect, since the Combi-Clip (the part made for connecting the flask to the Roti) was originally designed to be opened manually. The decision was made for a linear electromagnet, with the ability to stroke. The actuator is extending and pressing against the Combi-Clip. The friction is holding the Combi-Clip in place, while the Roti is rotating for a few rounds. This movement is fastening the flask in a reliable way without changing the Combi-Clip or any other part at all. 

## Result

This is how the final state of the project looks like thus far.

<img src="https://user-images.githubusercontent.com/101114939/165906712-f8065374-8a99-4a05-9146-cfcd33a2eac9.jpg" width="50%">
