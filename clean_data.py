import os
import pandas as pd

directory = 'data/original/ocr/'
columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main", "Text2", "Text3",]
for filename in os.listdir(directory):
  print(filename)
  ocr_temp = pd.read_csv(os.path.join(directory, filename), header=None, names=columns)
  for textIdx in range(len(ocr_temp[["Text2"]])):
    if type(ocr_temp.iloc[textIdx, 9])==str:
      ocr_temp.iloc[textIdx, 8] += ocr_temp.iloc[textIdx, 9]
  ocr_temp = ocr_temp.drop(labels=["Text2","Text3"], axis=1)
  ocr_temp.to_csv(os.path.join('data/interim/ocr/', filename))