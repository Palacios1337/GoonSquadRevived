
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model
import matplotlib.pylab as plt
import numpy as np
import cv2 as cv
import os
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

print("Monkey")

batch_size = 32
img_height = 64
img_width = 64
num_classes = 3
epochs = 10

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, num_classes)),
    #tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.AveragePooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    #tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.AveragePooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    #tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.AveragePooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

train = ImageDataGenerator(rescale=1./255)
validation = ImageDataGenerator(rescale=1./255)

print(os.listdir("/Users/Juani/RowanHacksPictures"))

train_set = train.flow_from_directory(
    '/Users/Juani/RowanHacksPictures/train',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)
validation_set = validation.flow_from_directory(
    '/Users/Juani/RowanHacksPictures/validation',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)
train_set.class_indices
model_fit = model.fit(train_set,
                      steps_per_epoch=6,
                      epochs = 50,
                      validation_data = validation_set)

dir_path = '/Users/Juani/RowanHacksPictures/test'

for i in os.listdir(dir_path):
  for j in  os.listdir(dir_path+"/"+i):
    img = image.load_img(dir_path+"/"+i+"/"+j)
    newimg = img.resize((64,64))
    plt.imshow(newimg)
    plt.show()

    X = image.img_to_array(newimg)
    X = np.expand_dims(X,axis=0)
    images = np.vstack([X])
    val = model.predict(images)
    print(val)

model.save('/Users/Juani/RowanHacksPictures/model'+".keras")