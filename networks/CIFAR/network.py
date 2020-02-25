from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tensorflow as tf
from tensorflow import keras
import h5py
import time
import os

class CIFAR():

	PATH = 'networks/CIFAR/'

	def __init__(self):
		model = self.buildModel()
		model = self.compile(model, start = True)
		pass

	def getConfig(self):
		return {
			'path' : self.PATH,
			'epoch' : 5,
			'batch' : 128
		}

		
	def getDataSet(self):
		cifar10 = keras.datasets.cifar10
		(xTrain,yTrain),(xTest, yTest) = cifar10.load_data()

		num_category = 10
		yTrain = keras.utils.to_categorical(yTrain, num_category)
		yTest = keras.utils.to_categorical(yTest, num_category)
		return ((xTrain,yTrain),(xTest, yTest))

	def buildModel(self, activationFucntion = tf.nn.relu):
		inputs = keras.Input(shape=(32,32,3))
		x = keras.layers.Conv2D(64, kernel_size=(1, 1),activation=activationFucntion)(inputs)
		x = keras.layers.Conv2D(64, kernel_size=(1, 1), activation=activationFucntion)(x)
		x = keras.layers.MaxPooling2D(pool_size=(2, 2))(x)
		x = keras.layers.Conv2D(128, kernel_size=(1, 1),activation=activationFucntion)(x)
		x = keras.layers.Conv2D(128, kernel_size=(1, 1), activation=activationFucntion)(x)
		x = keras.layers.MaxPooling2D(pool_size=(2, 2))(x)
		x = keras.layers.Conv2D(256, kernel_size=(1, 1),activation=activationFucntion)(x)
		x = keras.layers.Conv2D(256, kernel_size=(1, 1), activation=activationFucntion)(x)
		x = keras.layers.Conv2D(256, kernel_size=(1, 1), activation=activationFucntion)(x)
		x = keras.layers.MaxPooling2D(pool_size=(2, 2))(x)
		x = keras.layers.Flatten()(x)
		x = keras.layers.Dense(256, activation=activationFucntion)(x)
		output = keras.layers.Dense(10, activation='softmax')(x)
		model = keras.Model(inputs=inputs, outputs=output)

		return model
		

	def compile(self, model, start = False):
		model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

		if start:
			model.save_weights(self.PATH + 'unTrainedweights.h5')
		else:
			model.load_weights(self.PATH + 'unTrainedweights.h5')

		return model




def main():
	# Change this line based on Network File
	net = CIFAR()

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