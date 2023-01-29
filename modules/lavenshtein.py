import numpy as np
import pandas as pd
import os

"""
Calculates the lavenshtein distance between two strings.
It will find the minimum number of total insertions/deletions/edits
to get from one string to another.

Uses a dynamic programming algorithm and can penalize insertions,
deletions, and edits differently

Credit to GeeksForGeeks.org for this algorithm that I modified
"""

def lavenshtein(str1, str2, p_insert=1, p_delete=1, p_edit=1):
    # Create a table to store results of subproblems
    dp = np.zeros((len(str1) + 1, len(str2) + 1))
 
    # Fill d[][] in bottom up manner
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
 
            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i,j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i,j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i,j] = dp[i-1,j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = min(dp[i,j-1] + p_insert,        # Insert
                                   dp[i-1,j] + p_delete,        # Remove
                                   dp[i-1,j-1] + p_edit)    # Replace
 
    return int(dp[-1,-1])

def get_laven(value):
    columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main"]
    # columns_labels = ["doc_id1","lv1","lp1","ld1","la1",
    #                         "doc_id2","lv2","lp2","ld2","la2",
    #                         "doc_id3","lv3","lp3","ld3","la3",
    #                         "doc_id4","lv4","lp4","ld4","la4",
    #                         "doc_id5","lv5","lp5","ld5","la5",
    #                         "doc_id6","lv6","lp6","ld6","la6",
    #                         "doc_id7","lv7","lp7","ld7","la7",
    #                         "doc_id8","lv8","lp8","ld8","la8",
    #                         "doc_id9","lv9","lp9","ld9","la9",
    #                         "doc_id10","lv10","lp10","ld10","la10",
    #                         "doc_id11","lv11","lp11","ld11","la11",
    #                         "doc_id12","lv12","lp12","ld12","la12",
    #                         "doc_id13","lv13","lp13","ld13","la13",
    #                         "doc_id14","lv14","lp14","ld14","la14",
    #                         "doc_id15","lv15","lp15","ld15","la15",
    #                         "doc_id16","lv16","lp16","ld16","la16",
    #                         "doc_id17","lv17","lp17","ld17","la17",
    #                         "doc_id18","lv18","lp18","ld18","la18",
    #                         "doc_id19","lv19","lp19","ld19","la19",
    #                         "doc_id20","lv20","lp20","ld20","la20"]
    columns_labels = ["doc_id","levan_name","levan_price","levan_date","levan_address",]
    ocrdir = 'data/interim/ocr/'
    levan_user = pd.DataFrame(columns=columns_labels)
    #filename = "00d0624439175.csv"
    #f = ["00d0624439175.csv"]
    for filename in os.listdir(ocrdir):
        ocr_temp = pd.read_csv(os.path.join(ocrdir, filename), header=None, names=columns)  
        text_col = ocr_temp["Text_Main"]
        levan_name = text_col.apply(lavenshtein, str2=value["vendor_name"]).min()
        levan_price = text_col.apply(lavenshtein, str2=str(value["amount"])).min()
        levan_date = text_col.apply(lavenshtein, str2=str(value["date"])).min()
        levan_address = text_col.apply(lavenshtein, str2=value["vendor_address"][:20]).min()
        levan_user.loc[levan_user.shape[0]]=[filename[:-4],levan_name,levan_price,levan_date,levan_address]

    pot = levan_user[levan_user['levan_name'] < 4]
    pot_doc = pot['doc_id'].values.tolist()
    pot_name = pot['levan_name'].values.tolist()
    pot_price = pot['levan_price'].values.tolist()
    pot_date = pot['levan_date'].values.tolist()
    pot_address = pot['levan_address'].values.tolist()
    
    #smallest = levan_user.nsmallest(20, columns=["levan_name","levan_price","levan_date"])
    result = pd.Series({"pot_doc": pot_doc,"pot_name": pot_name,"pot_price": pot_price
                ,"pot_date": pot_date,"pot_address": pot_address})
    print(result)
    return result

if __name__ == "__main__":
    print(lavenshtein("col", "cowbbell"))
    print(lavenshtein("", "cowbbell"))
    print(lavenshtein("erfwerfwerf", "wergwergwiyerugiywuiergijwher"))