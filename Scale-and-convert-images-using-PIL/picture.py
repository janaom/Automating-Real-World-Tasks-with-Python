#!/usr/bin/env python3
from PIL import Image
import os

directory = "images/"
output_directory = "/opt/icons/"

#Rotate the image 90° clockwise
#Resize the image from 192x192 to 128x128
#Save the image to a new folder in .jpeg format
for filename in os.listdir(directory):
    if filename != ".DS_Store":
        im = Image.open(os.path.join(directory, filename))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(output_directory, filename+".jpeg"))
