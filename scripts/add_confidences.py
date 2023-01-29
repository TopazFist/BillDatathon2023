import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import pytesseract as pts
from tqdm import tqdm

ocrdir = 'data/interim/ocr/'
imgdir = 'data/original/img/'

data = []

for filename in tqdm(os.listdir(ocrdir)[:20]):
    img = cv2.imread(os.path.join(imgdir, filename[:-4]+".jpg"))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (9,9), 1)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 15)
    imgdata = pd.read_csv(os.path.join(ocrdir, filename))
    confs = []
    for row in imgdata.iterrows():
        slc = img[max(int(row[1]['BB2'])-5, 0):min(int(row[1]['BB6'])+5, img.shape[0]-1), 
            max(int(row[1]['BB1'])-5,0):min(int(row[1]['BB3'])+5, img.shape[1]-1)]
        text = pts.image_to_data(slc, output_type='data.frame', config="--psm 7")
        text = text[text['text'].notna()]
        confs.append(str(list(zip(text['text'],text['conf']))))
        data.append(int(c) for c in text['conf'])

print(confs)
print(data)

