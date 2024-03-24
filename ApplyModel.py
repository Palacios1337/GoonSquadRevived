
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model
import matplotlib.pylab as plt
import numpy as np
import cv2 as cv
import os
from PIL import Image
import serial
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

serialConnection = serial.Serial('COM4',115200)

model = keras.models.load_model('/Users/Juani/RowanHacksPictures/model'+".keras")

dir_path = '/Users/Juani/RowanHacksPictures/test'

while(1):
 for i in os.listdir(dir_path):
  for j in  os.listdir(dir_path+"/"+i):
    img = image.load_img(dir_path+"/"+i+"/"+j)
    newimg = img.resize((64,64))

    X = image.img_to_array(newimg)
    X = np.expand_dims(X,axis=0)
    images = np.vstack([X])
    val = model.predict(images)
    index_max = np.argmax(val)+1

    if (index_max == 1):
     index_max = 2
    elif(index_max == 2):
     index_max = 1

    print(index_max)  
    serialConnection.write(bytes(str.encode(str(index_max))))
    plt.imshow(newimg)
    plt.show()
    #serialConnection.write(bytes(str.encode('\n')))
    time.sleep(2)



'''
for i in os.listdir(dir_path):
  for j in  os.listdir(dir_path+"/"+i):
    img = image.load_img(dir_path+"/"+i+"/"+j)
    newimg = img.resize((64,64))
    #plt.imshow(newimg)
    #plt.show()

    X = image.img_to_array(newimg)
    X = np.expand_dims(X,axis=0)
    images = np.vstack([X])
    val = model.predict(images)
    print(val)
'''