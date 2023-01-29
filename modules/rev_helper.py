import os
import pandas as pd
from Levenshtein import distance
from fuzzywuzzy import fuzz

def lavenshtein(str1, str2):
    '''
    Calculates the lavenshtein distance between two strings.
    It will find the minimum number of total insertions/deletions/edits
    to get from one string to another.
    '''
    return distance(str1, str2)

def address_lavenshtein(str1, str2):
    '''
    Will use the smaller string (likely str1) and use
    it as a sliding window along str2 to find the largest
    ratio (len(a)+len(b)-lavenshtein(a,b))/(len(a)+len(b))

    However, if the string is too short, it won't be an address
    so we want to return 0, no similarity
    '''
    if len(str1) < 10:
        return 0
    return fuzz.partial_ratio(str1, str2)

def amount_lavenshtein(str1, str2):
    '''
    Will use the smaller string (likely str1) and use
    it as a sliding window along str2 to find the largest
    ratio (len(a)+len(b)-lavenshtein(a,b))/(len(a)+len(b))

    However, if the string is too short, it won't be a cash amount
    so we want to return 0, no similarity
    '''
    if len(str2) < 3:
        return 0
    return fuzz.partial_ratio(str1, str2)

def find_date(str1, str2):
    '''
    Will use a similar partial ratio to amount_lavenshtein
    However, will attempt to use several date permutations.
    Will also turn all slashes to dashes for consistent formatting.
    '''
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


def custom_lavenshtein(value, text_main):
    '''
    takes in a row of user_data and text_main
    iterates through text_main and finds the maximum/minimum
    lavenshtein distance between the two valuese
    '''
    levan_name = text_main.apply(lavenshtein, str2=str(value["vendor_name"])).min()
    levan_date = text_main.apply(find_date, str2=str(value["date"])).max()
    levan_amount = text_main.apply(amount_lavenshtein, str2=str(value["amount"])).max()
    levan_address = text_main.apply(address_lavenshtein, str2=str(value["vendor_address"][:30])).max()
    return pd.Series({"pot_doc": value["documentid"],"pot_name": (levan_name),"pot_price": levan_amount
                 ,"pot_date": levan_date,"pot_address": levan_address})


def rev_helper(zip):
    '''
    takes in a zip that contains a filename and a dataframe of user data
    iterates through the user data to find the avenshtein distance between the two values
    retruns a list of the potential user ids that fit within the criteria
    '''
    filename, users_data = zip
    columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main"]
    ocrdir = 'data/interim/ocr/'
    ocr_temp = pd.read_csv(os.path.join(ocrdir, filename), header=None, names=columns)  
    text_col = (ocr_temp["Text_Main"])
    result = users_data.apply(custom_lavenshtein, text_main = text_col,axis=1)
    # if (1 in result['pot_date']):
    #     result = result[(result['pot_date'] == 1)]
    #     pot = result[(result['pot_name'] < 5) | (result['pot_address'] <80)]
    # else:
    pot = result[(result['pot_name'] < 5) | (result['pot_address'] > 80)]
    return [filename[:-4],pot["pot_doc"].tolist(),pot["pot_name"].tolist(), 
            pot["pot_price"].tolist(),pot["pot_date"].tolist(),
            pot["pot_address"].tolist()]