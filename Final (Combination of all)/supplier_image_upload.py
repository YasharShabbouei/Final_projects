#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
Image_Directory = "/home/{}/supplier-data/images/"

for each_image in os.listdir(Image_Directory):
    if ".jpeg" in each_image:
        with open(Image_Directory + each_image, 'rb') as opened:
            r = requests.post(url, files={"file": opened})
