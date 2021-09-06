#!/usr/bin/env python3
import os
import requests

File_path="/data/feedback"
MyFiles=os.listdir(File_path)
TargetURL="http://34.133.250.211/feedback/"

for each_file in MyFiles:
    print(each_file)
    with open(File_path+"/"+each_file) as RawData:
         Splitted_Data=RawData.read().split("\n")
         MyJsonDictionary={"title":Splitted_Data[0],"name":Splitted_Data[1],"date":Splitted_Data[2], "feedback":Splitted_$
    response=requests.post(TargetURL,json=MyJsonDictionary)

print(response.status_code)
