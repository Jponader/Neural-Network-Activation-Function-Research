import tensorflow as tf
from tensorflow import keras
from datetime import datetime
from tensorflow.keras.activations import relu, sigmoid, tanh, linear, elu, exponential, hard_sigmoid, softplus, softsign
import h5py
import time
import sys
import os

from networks import *

assert tf.test.is_built_with_cuda(), "Cudo Not Working"
assert tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None), "Not Using GPU"
# SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\extras\CUPTI\lib64;%PATH%


networks = [FashionMNIST, CNN_MNIST, CIFAR]

#Speed Test
#networks = [CIFAR]

activationfunctions = [relu, sigmoid, tanh, linear, elu, exponential]

for runs in range(5):
	for network in networks:
		net = network()
		config = net.getConfig()
		((xTrain,yTrain),(xTest, yTest)) = net.getDataSet()

		for func in activationfunctions:
			model = net.buildModel(activationFucntion = func)
			model = net.compile(model)

			log_dir = os.path.join(config['path'],"logs",func.__name__ , str(runs))
			tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0)

			model.fit(xTrain, yTrain, epochs= config['epoch'], batch_size = config['batch'],validation_data =(xTest, yTest), callbacks = [tensorboard_callback], use_multiprocessing=True)

			#Speed Train for Testin
			#model.fit(xTrain, yTrain, epochs= 5, batch_size = config['batch'],validation_data =(xTest, yTest), callbacks = [cp_callback, tensorboard_callback])

			del model