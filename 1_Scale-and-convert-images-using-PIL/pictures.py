#!/usr/bin/env python3
from PIL import Image
import os

#This assigns the string value "images/" to the variable directory, which represents the path to the directory where the original images are located.
directory = "images/"
#This assigns the string value "/opt/icons/" to the variable output_directory, which represents the path to the directory where the modified images will be saved.
output_directory = "/opt/icons/"

#This starts a for loop that iterates over each file in the directory using the os.listdir() function. 
#The filename variable will be assigned the name of each file in the directory, one at a time.
for filename in os.listdir(directory):
#This checks if the current filename is not equal to the string ".DS_Store". 
#This is used to exclude the ".DS_Store" file, which is typically present in macOS directories.
    if filename != ".DS_Store":
#This opens the image file by joining the directory and filename using os.path.join() function, and assigns the opened image to the variable im.
        im = Image.open(os.path.join(directory, filename))
#This rotates the image by -90 degrees counterclockwise using the rotate() method of the Image object and assigns the rotated image back to im.
        im = im.rotate(-90)
#This resizes the image to a width and height of 128 pixels using the resize() method of the Image object and assigns the resized image back to im.
        im = im.resize((128,128))
#This converts the image to the RGB color mode using the convert() method of the Image object and assigns the converted image back to im.
        im = im.convert("RGB")
#This saves the modified image as a JPEG file by joining the output_directory and filename with the extension ".jpeg" using os.path.join() function, 
#and calling the save() method of the Image object with the file path.
        im.save(os.path.join(output_directory, filename+".jpeg"))
