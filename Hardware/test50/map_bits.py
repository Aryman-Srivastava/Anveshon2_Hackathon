from PIL import Image
import numpy as np
import random

def bits_converter_location(array):
    bits = ''
    for i in range(len(array)):
        temp = (bin(array[i]))
        temp = temp[2:]
        if(len(temp)<10):
            temp = '0'*(10-len(temp))+temp
        bits+=temp
    return bits


events = ['accident','high traffic', 'low traffic']
event = random.choice(events)

location = (254,84)
location_string = bits_converter_location(location)

extra_bit = ''
if event == 'accident':
    extra_bit = '00'
elif event == 'high traffic':
    extra_bit = '01'
elif event == 'low traffic':
    extra_bit = '10'
bits = location_string+extra_bit
file = open('bits.txt','w')
file.write(bits)
# print(bits)