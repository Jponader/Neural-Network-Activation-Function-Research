from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tensorflow as tf
from tensorflow import keras
import h5py
import time
import os

class CNN_MNIST():

	PATH = os.path.join('networks','CNN_MNIST')

	def __init__(self):
		model = self.buildModel()
		model = self.compile(model, start = True)
		del model

	def getConfig(self):
		return {
			'path' : self.PATH,
			'epoch' : 10,
			'batch' : 128
		}

		
	def getDataSet(self):
		mnist = keras.datasets.mnist
		(xTrain,yTrain),(xTest, yTest) = mnist.load_data()
		xTrain = xTrain.reshape(xTrain.shape[0], 28, 28, 1)
		xTest = xTest.reshape(xTest.shape[0], 28, 28, 1)
		xTrain = xTrain / 255.0
		xTest = xTest / 255.0
		num_category = 10
		yTrain = keras.utils.to_categorical(yTrain, num_category)
		yTest = keras.utils.to_categorical(yTest, num_category)
		return ((xTrain,yTrain),(xTest, yTest))

	def buildModel(self, activationFucntion = tf.nn.relu):
		inputs = keras.Input(shape=(28,28,1))
		x = keras.layers.Conv2D(32, kernel_size=(3, 3),activation=activationFucntion)(inputs)
		x = keras.layers.Conv2D(32, kernel_size=(3, 3), activation=activationFucntion)(x)
		x = keras.layers.Conv2D(64, kernel_size=(3, 3),activation=activationFucntion)(x)
		x = keras.layers.Flatten()(x)
		x = keras.layers.Dense(256, activation=activationFucntion)(x)
		output = keras.layers.Dense(10, activation='softmax')(x)
		model = keras.Model(inputs=inputs, outputs=output)

		return model


	def compile(self, model, start = False):
		model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

		if start:
			model.save_weights( os.path.join(self.PATH,'unTrainedweights.h5'))
		else:
			model.load_weights( os.path.join(self.PATH,'unTrainedweights.h5'))

		return model


# DEVELOPMENT TESTING

def main():
	# Change this line based on Network File
	net = CNN_MNIST()

	config = net.getConfig()
	((xTrain,yTrain),(xTest, yTest)) = net.getDataSet()
	model = net.buildModel()
	model = net.compile(model)
	model.fit(xTrain, yTrain, epochs= 1, batch_size = config['batch'])
		
	test_loss, test_acc = model.evaluate(xTest, yTest)
	print('Test accuracy:', test_acc)
	model.summary()

if __name__ == '__main__':
    main()

