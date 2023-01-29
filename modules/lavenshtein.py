import numpy as np
import pandas as pd
import os
from fuzzywuzzy import fuzz
from Levenshtein import distance

"""
Calculates the lavenshtein distance between two strings.
It will find the minimum number of total insertions/deletions/edits
to get from one string to another.

Uses a dynamic programming algorithm and can penalize insertions,
deletions, and edits differently

Credit to GeeksForGeeks.org for this algorithm that I modified
"""

def fuzz_ratio(str1, str2):
    return fuzz.ratio(str1, str2)

def partial_lavenshtein(str1, str2):
    return fuzz.partial_ratio(str1, str2)

def lavenshtein(str1, str2):
    return distance(str1, str2)

def find_date(str1, str2):
    if len(str1) < 5:
        return 0
    str1 = str1.replace('/','-')
    res = max(
        fuzz.partial_ratio(str1, str2),
        fuzz.partial_ratio(str1, str2[5:7]+'-'+str2[-2:]+'-'+str2[:4]),
        fuzz.partial_ratio(str1, str2[-2:]+'-'+str2[5:7]+'-'+str2[:4]),
        fuzz.partial_ratio(str1, str2[5:7]+'-'+str2[-2:]+'-'+str2[2:4]),
        fuzz.partial_ratio(str1, str2[-2:]+'-'+str2[5:7]+'-'+str2[2:4]),
    )
    return int(res == 100)

def get_laven(value):
    '''
    Gets the appropriate lavenshtein distances and ratios for each field.
    Returns a pandas series of those metrics to be added to a larger dataframe
    
    '''
    columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main"]
    columns_labels = ["doc_id","levan_name","levan_price","levan_date","levan_address",]
    ocrdir = 'data/interim/ocr/'
    levan_user = pd.DataFrame(columns=columns_labels)
    for filename in os.listdir(ocrdir):
        ocr_temp = pd.read_csv(os.path.join(ocrdir, filename), header=None, names=columns)  
        text_col = ocr_temp["Text_Main"]
        levan_name = text_col.apply(lavenshtein, str2=value["vendor_name"]).min()
        levan_price = text_col.apply(partial_lavenshtein, str2=str(value["amount"])).max()
        levan_date = text_col.apply(find_date, str2=str(value["date"])[:10]).max()
        levan_address = text_col.apply(fuzz_ratio, str2=value["vendor_address"][:30]).max()
        levan_user.loc[levan_user.shape[0]]=[filename[:-4],levan_name,levan_price,levan_date,levan_address]
    pot = levan_user[(levan_user['levan_name'] < 5) | (levan_user['levan_address'] > 80)]
    pot_doc = pot['doc_id'].values.tolist()
    pot_name = pot['levan_name'].values.tolist()
    pot_price = pot['levan_price'].values.tolist()
    pot_date = pot['levan_date'].values.tolist()
    pot_address = pot['levan_address'].values.tolist()
    
    result = pd.Series({"pot_doc": pot_doc,"pot_name": pot_name,"pot_price": pot_price
                ,"pot_date": pot_date,"pot_address": pot_address})
    return result

if __name__ == "__main__":
    print(lavenshtein("col", "cowbbell"))
    print(lavenshtein("", "cowbbell"))
    print(lavenshtein("erfwerfwerf", "wergwergwiyerugiywuiergijwher"))