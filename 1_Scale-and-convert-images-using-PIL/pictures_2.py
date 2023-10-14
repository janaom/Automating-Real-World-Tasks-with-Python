#alternative code achieves the same result as the original code
from PIL import Image
import os

directory = "images/"
output_directory = "/opt/icons/"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(directory):
    if filename != ".DS_Store":
        with Image.open(os.path.join(directory, filename)) as im:
            im = im.rotate(-90).resize((128, 128)).convert("RGB")
            output_filename = os.path.splitext(filename)[0] + ".jpeg"
            output_path = os.path.join(output_directory, output_filename)
            im.save(output_path)

#It uses the os.makedirs function to create the output directory if it doesn't already exist. This eliminates the need for a separate check and ensures that the directory is created if necessary.

#The with statement is used to open the image file. This ensures that the file is properly closed after processing, even if an exception occurs.

#The image transformations (rotate, resize, convert) are chained together in a single line, making the code more concise.

#The output filename is generated by replacing the extension of the original filename with ".jpeg" using the os.path.splitext function.

#The full output path is constructed using os.path.join to join the output directory and the output filename.