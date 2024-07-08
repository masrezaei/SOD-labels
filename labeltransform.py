import json
from PIL import Image
import csv
import cv2
import numpy as np
from skimage.draw import polygon2mask
import matplotlib.pyplot as plt
import pandas as pd
import os

file=open('./Label transform/jsonfile.json')
json_label=json.load(file)
file.close()

obj=json.dumps(json_label,)
with open('./Label transform/jsonfile_new.json', 'w') as file:
    file.write(obj)




for i in range(len(json_label)):
    
    outj={"categories":[],
          "info":{"year":2024,
                  "version":"1.0",
                  "contributor": "Label Studio"}}
    
    sample_name=json_label[i]['data']['image'].split('/')[-1]
    for ii in range(len(json_label[1]['annotations'][0]['result'])):
        if json_label[i]['annotations'][0]['result'][ii]['value']['closed']:
            points= json_label[1]['annotations'][0]['result'][0]['value']['points']
            print(points)




file=open('./Label transform/COCO/result.json')
coco_label=json.load(file)
file.close()

file=open('./Label transform/csvfile.csv')
csv_label=csv.DictReader(file)
file.close()


csv_label2 = pd.read_csv('./Label transform/csvfile.csv')


labelfiles=os.listdir('./Label transform/YOLO/labels/')
for i in labelfiles:
    path=os.path.join('./Label transform/YOLO/labels/', i)
    file=open(path)
    yolo_label=file.readlines()
    file.close()