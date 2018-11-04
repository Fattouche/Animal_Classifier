import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

TRAIN_DIR = '../media/train'

def flip_images(directory):

    directories = [x for x in os.walk(directory)]

    for directory in directories:
        for image in directory[2]:
            filename = os.path.join(directory[0], image)
            
            #im = np.flipud(plt.imread(filename))
            fnp = filename.split('.')
            
            new_filename = '..' + (fnp[-2] + 'r.' + fnp[-1]).replace('\\', '/')

            #print (new_filename)

            #with open(new_filename, 'wb') as new_file:
            #    im.tofile(new_file)


            image_obj = Image.open(filename)
            rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
            rotated_image.save(new_filename)


if __name__ == '__main__':
    flip_images(TRAIN_DIR)