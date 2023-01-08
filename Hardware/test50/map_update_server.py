
from PIL import Image
import numpy as np


def map_update(bits, i):
    data = bits
    location = data[:20]
    event = data[20:22]
    event =int(event,2)
    print(event)
    location_x = int(location[:10],2)
    location_y = int(location[10:],2)
    situation = ''
    if event == 0:
        situation = 'accident'
    elif event == 1:
        situation = 'high traffic'
    elif event == 2:
        situation = 'low traffic'
    print(situation,0)

    Image.open('google_map.jpg').convert('RGB').save('new.jpeg')
    if(i==0):
        im1=Image.open('new.jpeg')
    else:
        im1=Image.open('update1.jpg')
    if situation == 'accident':
        im2 = Image.open('accident.jpg')
    elif situation == 'high traffic':
        im2 = Image.open('traffic.jpg')
    else:
        im2 = Image.open('go.jpg')
    im2=im2.resize((25,32))
    back_im = im1.copy()
    back_im.paste(im2, (location_x, location_y))
    back_im.save('update1.jpg', quality=95)
    up=Image.open('update1.jpg')
    return up


def main():
    file_read = open("C:\\Users\\arjun\\OneDrive\\Desktop\\Anveshon2_Hackathon-1\\Software\\ML_Model\\rec.txt",'r')
    count = 0
    for i in range(2):
        data = file_read.readline()
        print(data)
        map_update(data, count)
        count+=1   
main()