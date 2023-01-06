from PIL import Image
import numpy as np
import random
# Array to bits
def bits_converter(array):
    print(array.shape)
    bits = ''
    for i in range(len(array[0])):
        temp = (bin(array[0][i]))
        temp = temp[2:]
        if(len(temp)<8):
            temp = '0'*(8-len(temp))+temp
        bits+=temp
    print(len(bits))
    return bits
def bits_converter_location(array):
    bits = ''
    for i in range(len(array)):
        temp = (bin(array[i]))
        temp = temp[2:]
        if(len(temp)<10):
            temp = '0'*(10-len(temp))+temp
        bits+=temp
    print(len(bits))
    return bits

events = ['accident','high traffic', 'low traffic']
event = random.choice(events)
print(event)
location = (254,84)
location_string = bits_converter_location(location)
# Open the image
image = Image.open('image.png')

# Convert the image to an RGB image
rgb_image = image.convert('RGB')

# Convert the image to a NumPy array
image_array = np.array(rgb_image)

red = image_array[:, :, 0]
green = image_array[:, :, 1]
blue = image_array[:, :, 2]
red = red.reshape(1,353322)
green = green.reshape(1,353322)
blue = blue.reshape(1,353322)
# print(red.shape)
# print(red)

bits_red = bits_converter(red)
bits_blue = bits_converter(blue)
bits_green = bits_converter(green)
extra_bit = ''
if event == 'accident':
    extra_bit = '00'
elif event == 'high traffic':
    extra_bit = '01'
elif event == 'low traffic':
    extra_bit = '10'
bits = bits_red+bits_green+bits_blue+location_string+extra_bit
print(extra_bit)
file = open('bits.txt','w')
file.write(bits)
print(len(bits))