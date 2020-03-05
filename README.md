# Neural-Network-Activation-Function-Research
Investigating the performance implications of changing the activation functions in Deep Neural Networks.

## Operations.sh
Maintains the environment for running TensorFlow.  Including managing dependencies on all devices and starting environment when running code.

### --check
Check the computer for python3, pip3 and python 3 virtual environment.

### --setupEnv
Created Virtual Environment for running TensorFlow and updates all of the dependencies to the proper state.

### --runTest
Runs testing script.

### --tensorboard
Starts the tensorbard console with the file directory specified.
./operations.sh --tensorboard <log File Dir>

### --runPY
Runs a specific python function in the virtual environment.
./operations.sh --runPY file.py

### --update
Updates the environment based on the requirements.txt file

### --Requpdate
Updates requirements.txt based on the current configuration.
