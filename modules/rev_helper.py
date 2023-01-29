import os
import pandas as pd
from Levenshtein import distance
from fuzzywuzzy import fuzz

def lavenshtein(str1, str2):
    return distance(str1, str2)

def partial_lavenshtein(str1, str2):
    return fuzz.partial_ratio(str1, str2)

def fuzz_lavenshtein(str1, str2):
    return fuzz.partial_ratio(str1, str2)

def custom_lavenshtein(value, text_main):
    levan_name = text_main.apply(lavenshtein, str2=str(value["vendor_name"])).min()
    levan_date = text_main.apply(partial_lavenshtein, str2=str(value["date"])).min()
    levan_amount = text_main.apply(lavenshtein, str2=str(value["amount"])).min()
    levan_address = text_main.apply(fuzz_lavenshtein, str2=str(value["vendor_address"])).max()
    return pd.Series({"pot_doc": value["documentid"],"pot_name": (levan_name),"pot_price": levan_amount
                 ,"pot_date": levan_date,"pot_address": levan_address})

def rev_helper(zip):
    filename, users_data = zip
    columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main"]
    ocrdir = 'data/interim/ocr/'
    ocr_temp = pd.read_csv(os.path.join(ocrdir, filename), header=None, names=columns)  
    text_col = (ocr_temp["Text_Main"])
    result = users_data.apply(custom_lavenshtein, text_main = text_col,axis=1)
    pot = result[(result['pot_name'] < 3) | (result['pot_address'] <80)]
    return [filename[:-4],pot["pot_doc"].tolist(),pot["pot_name"].tolist(), 
            pot["pot_price"].tolist(),pot["pot_date"].tolist(),
            pot["pot_address"].tolist()]