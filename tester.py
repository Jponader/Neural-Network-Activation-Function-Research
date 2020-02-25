import tensorflow as tf
from tensorflow import keras
import h5py
import time
import sys
import os

from networks import *

networks = [FashionMNIST, CNN_MNIST, CIFAR]

activationfunctions = [tf.nn.relu]

for network in networks:
	net = network()
	config = net.getConfig()
	((xTrain,yTrain),(xTest, yTest)) = net.getDataSet()

	for func in activationfunctions:
		model = net.buildModel(activationFucntion = func)
		model = net.compile(model)

		#local train, get checkpoints and stats


		checkpoint_path = config['path'] + "training/" + func.__name__ + "/cp-{epoch:04d}.ckpt"
		checkpoint_dir = os.path.dirname(checkpoint_path)
		cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True, verbose=1)


		model.fit(xTrain, yTrain, epochs= config['epoch'], batch_size = config['batch'],callbacks = [cp_callback])
		
		test_loss, test_acc = model.evaluate(xTest, yTest)

		print('Test accuracy:', test_acc)
		model.summary()




		#measure accrucy

		#plot data
		#save data
