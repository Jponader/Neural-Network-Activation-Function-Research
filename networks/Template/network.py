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
		model = self.compile(model, start = True)

	def getConfig(self):
		return {
			'path' : self.PATH,
			'epoch' : 5,
			'batch' : 32
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
		model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

		if start:
			model.save_weights(self.PATH + 'unTrainedweights.h5')
		else:
			model.load_weights(self.PATH + 'unTrainedweights.h5')

		return model


def main():
	# Change this line based on Network File
	net = template()

	config = net.getConfig()
	((xTrain,yTrain),(xTest, yTest)) = net.getDataSet()
	model = net.buildModel()
	model = net.compile(model)
	model.fit(xTrain, yTrain, epochs= 2, batch_size = config['batch'])
		
	test_loss, test_acc = model.evaluate(xTest, yTest)
	print('Test accuracy:', test_acc)
	model.summary()

if __name__ == '__main__':
    main()