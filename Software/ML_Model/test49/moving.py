
from PIL import Image
from PIL import Image
import numpy as np
import random
from PIL import Image, ImageDraw, ImageFilter
import label
import warnings

# Ignore the tensorflow warnings
warnings.filterwarnings("ignore", category=UserWarning, module='tensorflow')

# Your code that generates the warnings

def map_update(bits):
    data = bits

    location = data[:20]
    event = data[20:]
    
    location_x = int(location[:10],2)
    location_y = int(location[10:],2)
    situation = ''
    if event == '00':
        situation = 'accident'
    elif event == '01':
        situation = 'high traffic'
    elif event == '10':
        situation = 'low traffic'
    print(situation)

    Image.open('google_map.jpg').convert('RGB').save('new.jpeg')
    im1=Image.open('update.jpg')
    if situation == 'accident':
        im2 = Image.open('accident.jpg')
    elif situation == 'high traffic':
        im2 = Image.open('traffic.jpg')
    else:
        im2 = Image.open('go.jpg')
    im2=im2.resize((25,32))
    back_im = im1.copy()
    back_im.paste(im2, (location_x, location_y))
    back_im.save('update.jpg', quality=95)
    up=Image.open('update.jpg')
    return up

def bits_converter_location(array):
    bits = ''
    for i in range(len(array)):
        temp = (bin(array[i]))
        temp = temp[2:]
        if(len(temp)<10):
            temp = '0'*(10-len(temp))+temp
        bits+=temp
    return bits

def map_bits(location):
    
    testImage = label.printLabel("frame_74.jpg")
    event = testImage[0]
    if event == 'dense_traffic':
        event = 'high traffic'
    elif event == 'sparse_traffic':
        event = 'low traffic'
    elif event == 'Accident':
        event = 'accident'
    print(event)
    location_string = bits_converter_location(location)
    print(len(location_string))
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
    return bits
    

im = Image.open("car.png")

# Resize the image
im_resized = im.resize((20, 20))
# Save the resized image
im_resized.save("car.png")
import pygame

# Initialize Pygame
pygame.init()

# Set the window size
size = (800, 600)

# Create the window
screen = pygame.display.set_mode(size)

# Load the image
image = pygame.image.load("car.png")

back = pygame.image.load("update.jpg")

# Set the image's starting position
x, y = 283, 450

# Set the frame rate
fps = 10

# Run the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the image's position
    x -= 1
    y -= 2.5
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the image at its new position
    screen.blit(back, (0, 0))
    if((x<190) or (y<220)):
        quit()
    elif((x==235 and y==330.0)):
        bits = map_bits((x,int(y)))
        map_update(bits)
        back = pygame.image.load("update.jpg")
        screen.blit(back, (0, 0))
    elif((x==275 and y==430.0)):
        bits = map_bits((x,int(y)))
        map_update(bits)
        back = pygame.image.load("update.jpg")
        screen.blit(back, (0, 0))
    screen.blit(image, (x, y))
    # Update the display
    pygame.display.flip()

    # Delay to achieve the desired frame rate. 
    pygame.time.delay(1000 // fps)

# Quit Pygame
pygame.quit()
