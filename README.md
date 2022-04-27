# BIG-MAP_ROTI

The big aim of this project is to control the Rotavapor R-300 from BÜCHI with a PLC. The Rotavapor R-300 cannot be directly accessed via PLC, but with the I-300 Pro extension it is possible to communicate with the R-300 via RESTful API. It is required to enable "OpenInterface" on the I-300 first. 
BÜCHI offers a publicly available github page with instructions to do so:\
https://github.com/buchi-labortechnik-ag/openinterface_rotavapor.git

Now that OpenInterface is enabled, an interaction with python is possible. 
Büchi offers some python examples:\
https://github.com/buchi-labortechnik-ag/openinterface_examples_python.git

For our case, we need to change some parameters. Here are the python codes used for controlling the R-300:\
[Start](python_scripts/start.py)\
[Stop](python_scripts/stop.py)\
[Heating](python_scripts/heating.py)\
[Rotation](python_scripts/rotation.py)\
[Vacuum](python_scripts/vacuum.py)\
[Program](python_scripts/program.py)\
[Rotate](python_scripts/rotate.py)\
[Stop_Rotate](python_scripts/stop_rotate.py)\



<img src="https://user-images.githubusercontent.com/101114939/165475572-87ca0ed3-5abb-4c0a-9a87-396802d7a8af.jpg" width="35%">
