from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tensorflow as tf
from tensorflow import keras
import h5py
import time
import os

class FashionMNIST():

	PATH = 'networks/FashionMNIST/'

	def __init__(self):
		model = self.buildModel()
		model = self.compile(model,start = True)

	def getConfig(self):
		return {
			'path' : self.PATH,
			'epoch' : 5
		}

		
	def getDataSet(self):
		fashion_mnist = keras.datasets.fashion_mnist
		(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
		train_images = train_images / 255.0
		test_images = test_images / 255.0

		return ((train_images, train_labels), (test_images, test_labels))

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
			model.save_weights(self.PATH + 'unTrainedweights.h5')
		else:
			model.load_weights(self.PATH + 'unTrainedweights.h5')

		return model


