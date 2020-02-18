from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tensorflow as tf
from tensorflow import keras
import h5py
import time
import os



#checkpoint_path = "training_1/cp-{epoch:04d}.ckpt"
#checkpoint_dir = os.path.dirname(checkpoint_path)
#cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True, verbose=1)


# Data PreProcessing
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
							 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
test_length = 10000
train_images = train_images / 255.0
test_images = test_images / 255.0

# Load Model
# model= keras.models.load_model('model.h5')
# model.load_weights('weights.h5')

inputs = keras.Input(shape=(28,28))
x = keras.layers.Flatten()(inputs)
y = keras.layers.Dense(128, activation=tf.nn.relu)(x)
output = keras.layers.Dense(10, activation=tf.nn.softmax)(y)
model = keras.Model(inputs=inputs, outputs=output)

model.compile(optimizer='adam',
							loss='sparse_categorical_crossentropy',
							metrics=['accuracy'])

#model.save_weights('networks/FashionMNST/unTrainedweights.h5')
#model.load_weights('networks/FashionMNST/unTrainedweights.h5')


model.fit(train_images, train_labels, epochs=5)
#model.fit(train_images, train_labels, epochs=5, callbacks = [cp_callback])

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)
model.summary()

# model.save_weights('weights.h5')
# model.save('model.h5')