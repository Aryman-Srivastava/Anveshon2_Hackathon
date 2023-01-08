# %%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from time import perf_counter 
import os
from numba import jit, cuda

# %%
## Defining batch specfications
batch_size = 100
img_height = 250
img_width = 250

# %%
## loading training set
training_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'train',
    seed=42,
    image_size= (img_height, img_width),
    batch_size=batch_size
)
class_names = training_ds.class_names

# %%
testing_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'test',
    seed=42,
    image_size= (img_height, img_width),
    batch_size=batch_size
)

# %%
class_names

# %%
## Defining Cnn
MyCnn = tf.keras.models.Sequential([
    layers.BatchNormalization(),
    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(128, 3, activation='relu'),
    layers.MaxPooling2D(),
    # Add a dropout layer with a rate of 0.25
    layers.Dropout(0.25),
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dense(len(class_names), activation= 'softmax')
])

MyCnn.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# %%
## lets train our CNN
retVal = MyCnn.fit(training_ds, validation_data= testing_ds, epochs = 10)

# %%
## lets vizualize results on testing data
AccuracyVector = []
plt.figure(figsize=(30, 30))
for images, labels in testing_ds.take(1):
    predictions = MyCnn.predict(images)
    predlabel = []
    prdlbl = []
    
    for mem in predictions:
        predlabel.append(class_names[np.argmax(mem)])
        prdlbl.append(np.argmax(mem))
    
    AccuracyVector = np.array(prdlbl) == labels
    for i in range(40):
        ax = plt.subplot(10, 4, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title('Pred: '+ predlabel[i]+' actl:'+class_names[labels[i]] )
        plt.axis('off')
        plt.grid(True)

# %%
import pickle
pickle.dump(MyCnn, open('model.pkl','wb'))

# %%
# model = pickle.load(open('model.pkl','rb'))
# model.predict(testing_ds)
MyCnn.save('model.h5')

# %%
loaded_model = tf.keras.models.load_model('model.h5')
loaded_model.predict(testing_ds)

# %%
import cv2

# %%
def inputTransform(imgPath):
    image = cv2.imread(imgPath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert the image to Tensor
    img_to_tensor = tf.convert_to_tensor(image, dtype=tf.float32)
    img_re = tf.image.resize(img_to_tensor, [250, 250])
    new_image = tf.expand_dims(img_re, 0)    
    return new_image

# %%
@jit(target_backend='cuda')                         
def printLabel(image):
    testImage = inputTransform(image)
    loaded_model = tf.keras.models.load_model('model.h5')
    y_pred = loaded_model.predict(testImage)
    # print([class_names[y_pred.argmax(axis=0)] for y_pred in y_pred])
    return ([class_names[y_pred.argmax(axis=0)] for y_pred in y_pred])

# # %%
# testImage = inputTransform('frame_74.jpg')
# check = printLabel('frame_74.jpg')
# print(check)

# %%



