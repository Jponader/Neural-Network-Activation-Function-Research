from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tensorflow as tf
from tensorflow import keras
import h5py
import time
import os

class FashionMNIST():

	PATH = os.path.join('networks','FashionMNIST')


	def __init__(self):
		model = self.buildModel()
		model = self.compile(model,start = True)

	def getConfig(self):
		return {
			'path' : self.PATH,
			'epoch' : 5,
			'batch' : 32
		}

		
	def getDataSet(self):
		fashion_mnist = keras.datasets.fashion_mnist
		(xTrain,yTrain),(xTest, yTest) = fashion_mnist.load_data()
		xTrain = xTrain / 255.0
		xTest = xTest / 255.0
		return ((xTrain,yTrain),(xTest, yTest))

	def buildModel(self, activationFucntion = tf.nn.relu):
		inputs = keras.Input(shape=(28,28))
		x = keras.layers.Flatten()(inputs)
		y = keras.layers.Dense(128, activation=activationFucntion)(x)
		output = keras.layers.Dense(10, activation=tf.nn.softmax)(y)
		model = keras.Model(inputs=inputs, outputs=output)
		return model

	def compile(self, model, start = False):
		model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

		if start:
			model.save_weights( os.path.join(self.PATH,'unTrainedweights.h5'))
		else:
			model.load_weights( os.path.join(self.PATH,'unTrainedweights.h5'))

		return model


# DEVELOPMENT TESTING

def main():
	# Change this line based on Network File
	net = FashionMNIST()

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