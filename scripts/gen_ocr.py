'''
Generates all OCRs that don't already exist in data/interim/ocrs
This script should be executed after clean_data.py, which cleans given ocrs
After these scripts are executed, each receipt should have a corresponding
OCR that can be fed into the mapping algorithm.
'''

import sys
sys.path.append("..")

import os
from multiprocessing import Pool
from modules.cvread import read_reciept

existing_ocrs = os.listdir("../data/interim/ocr")

# Create a list of non-existing OCR paths
imgs = []
for o in os.listdir("../data/original/img"):
    if o[:-4]+".csv" not in existing_ocrs and o[:-7]+".csv": imgs.append(o)

# Read all receipts in parallel
with Pool() as p:
    p.map(read_reciept, imgs) 
