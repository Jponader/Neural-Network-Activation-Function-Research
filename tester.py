import tensorflow as tf
from tensorflow import keras
import h5py
import time
import sys
import os

from networks import *

networks = [FashionMNIST]

activationfunctions = [tf.nn.relu]

for network in networks:
	net = network()
	config = net.getConfig()
	((xTrain,yTrain),(xTest, yTest)) = net.getDataSet()

	for func in activationfunctions:
		model = net.buildModel(activationFucntion = func)
		model = net.compile(model)

		#local train, get checkpoints and stats


		checkpoint_path = config['path'] + "training/" + func + "/cp-{epoch:04d}.ckpt"
		checkpoint_dir = os.path.dirname(checkpoint_path)
		cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True, verbose=1)


		model.fit(xTrain, yTrain, epochs= config['epoch'], callbacks = [cp_callback])

		test_loss, test_acc = model.evaluate(test_images, test_labels)

		print('Test accuracy:', test_acc)
		model.summary()




		#measure accrucy

		#plot data
		#save data
