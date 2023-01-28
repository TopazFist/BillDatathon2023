import os
import pandas as pd

# Cleaning OCR Data

directory = 'data/original/ocr/'
columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main", "Text2", "Text3","Text4"]
for filename in os.listdir(directory):
  try:
    ocr_temp = pd.read_csv(os.path.join(directory, filename), header=None, names=columns)
  except:
    continue
  if filename == ".DS_Store":
    continue
  ocr_temp = pd.read_csv(os.path.join(directory, filename), header=None, names=columns)

  ocr_temp["Text_Main"] = ocr_temp["Text_Main"].fillna('').astype(str)+ocr_temp["Text2"].fillna('').astype(str)+ocr_temp["Text3"].fillna('').astype(str)+ocr_temp["Text4"].fillna('').astype(str)

  ocr_temp["Text_Main"].replace("\'",'')
  ocr_temp["Text_Main"].replace("\"",'')
  ocr_temp = ocr_temp.drop(labels=["Text2","Text3","Text4"], axis=1)
  ocr_temp.to_csv(os.path.join('data/interim/ocr/', filename))