import os
from multiprocessing import Pool
from cvread import read_reciept

if __name__ == "__main__":
    existing_ocrs = os.listdir("data/interim/ocr")
    imgs = []
    for o in os.listdir("data/original/img"):
        if o[:-4]+".csv" not in existing_ocrs: imgs.append(o)
    print(imgs)
    with Pool() as p:
        p.map(read_reciept, imgs)
