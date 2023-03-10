import cv2
import pytesseract as pts
import os
import pandas as pd

def cvread(filename):
    print(filename)
    confs, data = [], []
    ocrdir = '../data/interim/ocr/'
    imgdir = '../data/original/img/'
    img = cv2.imread(os.path.join(imgdir, filename[:-4]+".jpg"))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (9,9), 1)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 15)
    imgdata = pd.read_csv(os.path.join(ocrdir, filename))
    for row in imgdata.iterrows():
        slc = img[max(int(row[1]['BB2'])-5, 0):min(int(row[1]['BB6'])+5, img.shape[0]-1), 
            max(int(row[1]['BB1'])-5,0):min(int(row[1]['BB3'])+5, img.shape[1]-1)]
        text = pts.image_to_data(slc, output_type='data.frame', config="--psm 7")
        text = text[text['text'].notna()]
        [data.append(float(c)) for c in list(text['conf'])]
    return data

def read_reciept(filename) -> pd.DataFrame:
    '''
    Takes in an image filename in data/original/img and creates its
    corresponding OCR using Google's Tesseract. This function will 
    blur and threshold the image to make the OCR more accurate.

    Returns a dataframe and saves it as a csv file in data/interim/ocrs
    '''
    print("Creating ocr for ", filename)
    dir = "../data/original/img"
    if dir[-1] != '/': dir = dir + '/'
    img = cv2.imread(dir + filename)

    # Prepare image for model
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (9,9), 1)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 15)

    # Implement model
    text = pts.image_to_data(img, output_type='data.frame', config="--psm 3")

    text = text[text['text'].notna()]
    rst = ""
    confs = []
    conf_series = []
    lines = []
    
    # Create bounding boxes
    tops, lefts, bottoms, rights = [], [], [], []
    for row in text.iterrows():
        if int(row[1]['word_num']) == 1:
            if len(confs) > 0 and sum(confs)/len(confs) > 30:
                conf_series.append(sum(confs)/len(confs))
                lines.append(rst.upper())
            elif len(confs) > 0 and sum(confs)/len(confs) < 30:
                tops.pop()
                lefts.pop()
                rights.pop()
                bottoms.pop()
            tops.append(row[1]['top'])
            lefts.append(row[1]['left'])
            rights.append(row[1]['left']+row[1]['width'])
            bottoms.append(row[1]['top']+row[1]['height'])
            rst = ""
            confs = []
        else:
            rst += ' '
            tops[-1] = min(tops[-1], row[1]['top'])
            bottoms[-1] = max(bottoms[-1], row[1]['top']+row[1]['height'])
            rights[-1] = max(rights[-1], row[1]['left']+row[1]['width'])
        rst += row[1]['text']
        confs.append(float(row[1]['conf']))
    conf_series.append(sum(confs)/len(confs))
    lines.append(rst.upper())
    res = {"BB1":lefts, "BB2":tops, "BB3":rights, "BB4":tops, 
        "BB5":rights, "BB6":bottoms, "BB7":lefts, "BB8":bottoms, "Text_main":lines}
    res = pd.DataFrame(res)

    #Load csv into data/interim/ocr
    res.to_csv(f"../data/interim/ocr/{filename[:-4]}.csv")

    return res