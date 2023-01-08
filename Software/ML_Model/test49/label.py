import cv2
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow')

def inputTransform(imgPath):
    image = cv2.imread(imgPath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert the image to Tensor
    img_to_tensor = tf.convert_to_tensor(image, dtype=tf.float32)
    img_re = tf.image.resize(img_to_tensor, [250, 250])
    new_image = tf.expand_dims(img_re, 0)    
    return new_image

def printLabel(image):
    testImage = inputTransform(image)
    loaded_model = tf.keras.models.load_model('model.h5')
    y_pred = loaded_model.predict(testImage)
    class_names = ['Accident', 'Non Accident', 'dense_traffic', 'sparse_traffic']
    # print([class_names[y_pred.argmax(axis=0)] for y_pred in y_pred])
    return ([class_names[y_pred.argmax(axis=0)] for y_pred in y_pred])

# check = printLabel('frame_74.jpg')
# print(check)