#!/usr/bin/env python3
import os
import sys
from PIL import Image

Image_Directory = "/home/{}/supplier-data/images/"
#Image_Directory = "/home/yashar/Desktop/All_Of_Them/images/"
for image in os.listdir(Image_Directory):
    target_image=Image.open(Image_Directory+image).convert("RGB")
    target_image.resize((600,400)).save(Image_Directory + image.split(".")[0] + ".jpeg","JPEG")
    target_image.close()
