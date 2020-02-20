from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tensorflow as tf
from tensorflow import keras
import h5py
import time
import os

class template():

	PATH = 'networks/template/'

	def __init__(self):
		model = self.buildModel()
		model = self.compile(start = True)

	def getConfig(self):
		return {
			'path' : PATH,
			'epoch' : 5
		}

		
	def getDataSet(self):
		#get data and return readt to use

		#return ((train_images, train_labels), (test_images, test_labels))
		pass

	def buildModel(self, activationFucntion = tf.nn.relu):
		#build Model
		#return model
		pass

	def compile(self, model, start = False):
		model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

		if start:
			model.save_weights(PATH + 'unTrainedweights.h5')
		else:
			model.load_weights(PATH + 'unTrainedweights.h5')

		return model


