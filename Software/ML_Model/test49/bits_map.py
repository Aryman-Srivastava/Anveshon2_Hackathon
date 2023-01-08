from PIL import Image, ImageDraw, ImageFilter
import numpy as np
file_read = open('bits.txt','r')
data = file_read.readline()

location = data[:20]
event = data[20:]
print(len(data))
print(event)

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

Image.open('Software\\ML_Model\\map.png').convert('RGB').save('new.jpeg')
im1=Image.open('new.jpeg')
if situation == 'accident':
    im2 = Image.open('Software\ML_Model\\accident.jpg')
elif situation == 'high traffic':
    im2 = Image.open('Software\ML_Model\\traffic.jpg')
else:
    im2 = Image.open('Software\\ML_Model\\go.jpg')
im2=im2.resize((25,32))
back_im = im1.copy()
back_im.paste(im2, (location_x, location_y))
back_im.save('update.jpg', quality=95)