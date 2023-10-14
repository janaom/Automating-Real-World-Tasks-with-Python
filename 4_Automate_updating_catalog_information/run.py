import os
import requests

fruits = {}
keys = ["name", "weight", "description", "image_name"]
path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"

for file in os.listdir(path):
    with open(os.path.join(path, file)) as f:
        for line in f:
            line = line.strip()
            if "lbs" in line:
                weight = int(line.split()[0])
                fruits["weight"] = weight
            else:
                try:
                    fruits[keys[len(fruits)]] = line
                except IndexError:
                    fruits[keys[2]] = line

        split_filename = file.split(".")
        image_name = split_filename[0] + ".jpeg"
        for image_file in os.listdir(img_path):
            if image_file == image_name:
                fruits["image_name"] = image_name

        response = requests.post("http://<External_IP>/fruits/", json=fruits)
        fruits.clear()
