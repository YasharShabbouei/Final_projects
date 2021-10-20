#!/usr/bin/env python3
import os
import requests
import json

Desc_Directory = "/home/{}/supplier-data/descriptions/"
Image_Directory = "/home/{}/supplier-data/images/"
#Desc_Directory = "/home/yashar/Desktop/All_Of_Them/descriptions/"
#Image_Directory = "/home/yashar/Desktop/All_Of_Them/images/"
ImageFiles=os.listdir(Image_Directory)
DescFiles=os.listdir(Desc_Directory)
TargetURL="http://localhost/fruits/"

MyJsonDictionary= {}
#MyJsonDictionary_list= []

for each_Desc_file in DescFiles:
#    print(each_Desc_file)
    with open(Desc_Directory+each_Desc_file) as RawData:
        description = ""
        All_lines = RawData.readlines()
        for i in range(2,len(All_lines)):
            description = description+All_lines[i].replace("\n"," ")
        MyJsonDictionary={"name":All_lines[0].strip("\n"),
                          "weight":int(All_lines[1].strip("lbs \n")),
                          "description":description ,
                          "image_name":(each_Desc_file.strip('.txt'))+'.jpeg'}
#    print(MyJsonDictionary)
# lines 30-33
    response=requests.post(TargetURL,json=MyJsonDictionary)
    if response.status_code != 201:
        raise Exception ("POST error status = {}".format(response.status_code))
    print("Created feedback ID: {}".format(response.json()["id"]))

# or lines 36-41
#for each_item in MyJsonDictionary:
#    response=requests.post(TargetURL,json=each_item)
#    if response.status_code != 201:
#        raise Exception ("POST error status = {}".format(response.status_code))
#    print("Created feedback ID: {}".format(response.json()["id"]))
