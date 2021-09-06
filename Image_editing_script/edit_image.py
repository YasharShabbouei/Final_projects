#!/usr/bin/env python3
import glob
from PIL import Image

for image in glob.glob("ic_*"):
   target_image=Image.open(image).convert("RGB")
   target_image.rotate(270).resize((128,128)).save("/opt/icons/" + image,"JPEG")
