from PIL import Image, ImageDraw, ImageFilter
import numpy as np
def bits_reconstructor(bits):
    print(len(bits))
    matrix = np.zeros((1,353322))
    for i in range(len(bits)//8):
        temp = bits[i*8:(i+1)*8]
        temp = int(temp,2)
        matrix[0][i] = temp
    return matrix
    
    
reconsructed = np.zeros((486,727,3))
file_read = open('bits.txt','r')
data = file_read.readline()

recont_bits_red = data[:2826576]
recont_bits_green = data[2826576:5653152]
recont_bits_blue = data[5653152:8479728]

location = data[8479728:8479748]
event = data[8479748:]
print(len(data))
print(event)
recont_matrix_red = bits_reconstructor(recont_bits_red)
recont_matrix_red = recont_matrix_red.reshape(486,727)
recont_matrix_green = bits_reconstructor(recont_bits_green)
recont_matrix_green = recont_matrix_green.reshape(486,727)
recont_matrix_blue = bits_reconstructor(recont_bits_blue)
recont_matrix_blue = recont_matrix_blue.reshape(486,727)

image_array_r = np.zeros((486,727,3))
image_array_r[:,:,0] = recont_matrix_red
image_array_r[:,:,1] = recont_matrix_green
image_array_r[:,:,2] = recont_matrix_blue
 
image = Image.fromarray(image_array_r.astype('uint8'))
image.save('map.png')
situation = ''
if event == '00':
    situation = 'accident'
elif event == '01':
    situation = 'high traffic'
elif event == '10':
    situation = 'low traffic'
print(situation)
# im1 = Image.open('image.png')
Image.open('image.png').convert('RGB').save('new.jpeg')
im1=Image.open('new.jpeg')
if situation == 'accident':
    im2 = Image.open('accident.jpg')
elif situation == 'high traffic':
    im2 = Image.open('traffic.jpg')
else:
    im2 = Image.open('go.jpg')
im2=im2.resize((25,32))
back_im = im1.copy()
back_im.paste(im2, (235, 84))
back_im.save('update.jpg', quality=95)