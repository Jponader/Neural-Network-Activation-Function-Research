# Neural-Network-Activation-Function-Research
Investigating the performance implications of changing the activation fucntions in Deep Neural Networks.

## Operations.sh
Maintains the enviroment for running tensoflow.  Including managaing dependencies on all devices and starting enviroment when running code.

### --check
Check the computer for python3, pip3 and python 3 virtual enviroment.

### --setupEnv
Created Virtual Enviroment for running tensorflow and updates all of the dependicies to the proper state.

### --runTest
Runs testing script.

### --tensorboard
Starts the tensorbard console with the file directory specified.
./operations.sh --tensorboard <log File Dir>

### --runPY
Runs a specific python function in the virtual enviroment.
./operations.sh --runPY file.py

### --update
Updates the enviroment based on the requirements.txt file

### --Requpdate
Updates requirements.txt based on the current configuration.

