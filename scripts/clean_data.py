import sys
sys.path.append("..")

import pandas as pd
import numpy as np
import os
from random import randint
from modules.lavenshtein import lavenshtein

# Cleaning OCR Data

directory = '../data/original/ocr/'
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
  ocr_temp.to_csv(os.path.join('../data/interim/ocr/', filename))


# Cleaning User Data
users_data = pd.read_csv("../data/original/Users.csv")


def laven_calc(cand_name, cand_lst, p_insert=1, p_delete=1, p_edit=1):
    laven_score = lavenshtein(cand_lst.iloc[0], cand_name, p_insert=p_insert, p_delete=p_delete, p_edit=p_edit)
    laven_score /= len(cand_name) # Normalize score based on string length
    return cand_lst[cand_lst == cand_name].index[0], laven_score


# Dates
date_series = []
temp_date_df = users_data["date"].copy()
temp_date_df = temp_date_df.str.split("-")
for date in temp_date_df:
    length_lst = np.array(list(map(lambda x: len(x), date))) # Get str lengths
    year = date[np.argmax(length_lst)]
    # Construct new year
    if int(year[-1]) in [6, 7, 8]:
        year = "201" + str(year[-1])
    else:
        year = "201" + str(randint(6,8))
    if int(date[1]) > 12: # Check where day and month are
        if int(date[2]) > 12:
            day = date[1]
            month = str(randint(1,12)) # There's few enough cases that this should be alright
        else:
            day = date[1]
            month = date[2]
    else:
        day = date[2]
        month = date[1]
    # Construct new day
    if int(day) > 31:
        day = str(randint(1,2)) + str(day[-1])
    # Construct new date and add to users_data
    new_date = year + "-" + month + "-" + day
    date_series.append(new_date)
users_data["date"] = pd.to_datetime(date_series)

# Cleaning Vendor Names
temp_vname_df = users_data["vendor_name"].copy() # Return List
candidate_list = users_data["vendor_name"].copy() # Iteration List
while len(candidate_list) > 0:
    temp_cand_array = candidate_list.copy()
    lavens = temp_cand_array.apply(laven_calc, cand_lst=temp_cand_array, p_insert=0.5, p_delete=0.5, p_edit=1)
    matches = list(filter(lambda x: x[1] < 0.4, lavens)) # Consider scores where less than 40% of word is edited
    matches = list(dict.fromkeys(matches)) # Remove weird duplicates
    replace_name = candidate_list.iloc[0] # Get name to replace matches with
    remove_idx = list(map(lambda x: x[0], matches))
    temp_vname_df.iloc[remove_idx,] = replace_name # Replace entries
    candidate_list = candidate_list.drop(remove_idx) # Remove matches from candidates
    candidate_list = candidate_list[~candidate_list.isin([replace_name])] # Remove matches from candidates
users_data["vendor_name"] = temp_vname_df

# Cleaning Vendor Addresses
temp_vadd_df = users_data["vendor_address"].copy() # Return List
candidate_list = users_data["vendor_address"].copy() # Iteration List
while len(candidate_list) > 0:
    temp_cand_array = candidate_list.copy()
    lavens = temp_cand_array.apply(laven_calc, cand_lst=temp_cand_array, p_insert=0.5, p_delete=0.5, p_edit=1)
    matches = list(filter(lambda x: x[1] < 0.1, lavens)) # Consider scores where less than 10% of str is different
    matches = list(dict.fromkeys(matches)) # Remove weird duplicates
    replace_name = candidate_list.iloc[0] # Get name to replace matches with
    remove_idx = list(map(lambda x: x[0], matches))
    temp_vname_df.iloc[remove_idx,] = replace_name # Replace entries
    candidate_list = candidate_list.drop(remove_idx) # Remove matches from candidates
    candidate_list = candidate_list[~candidate_list.isin([replace_name])] # Remove matches from candidates
users_data["vendor_address"] = temp_vadd_df

temp_vname_df = users_data["vendor_name"].copy() # Return List
candidate_list = users_data["vendor_name"].copy() # Iteration List
while len(candidate_list) > 0:
    temp_cand_array = candidate_list.copy()
    lavens = temp_cand_array.apply(laven_calc, cand_lst=temp_cand_array, p_insert=0.5, p_delete=0.5, p_edit=1)
    matches = list(filter(lambda x: x[1] < 0.4, lavens)) # Consider scores where less than 40% of word is edited
    matches = list(dict.fromkeys(matches)) # Remove weird duplicates
    replace_name = candidate_list.iloc[0] # Get name to replace matches with
    remove_idx = list(map(lambda x: x[0], matches))
    temp_vname_df.iloc[remove_idx,] = replace_name # Replace entries
    candidate_list = candidate_list.drop(remove_idx) # Remove matches from candidates
    candidate_list = candidate_list[~candidate_list.isin([replace_name])] # Remove matches from candidates
    print(len(candidate_list))
users_data["vendor_name"] = temp_vname_df

# Cleaning Vendor Addresses
temp_vadd_df = users_data["vendor_address"].copy() # Return List
candidate_list = users_data["vendor_address"].copy() # Iteration List
while len(candidate_list) > 0:
    temp_cand_array = candidate_list.copy()
    lavens = temp_cand_array.apply(laven_calc, cand_lst=temp_cand_array, p_insert=0.5, p_delete=0.5, p_edit=1)
    matches = list(filter(lambda x: x[1] < 0.1, lavens)) # Consider scores where less than 10% of str is different
    matches = list(dict.fromkeys(matches)) # Remove weird duplicates
    replace_name = candidate_list.iloc[0] # Get name to replace matches with
    remove_idx = list(map(lambda x: x[0], matches))
    temp_vname_df.iloc[remove_idx,] = replace_name # Replace entries
    candidate_list = candidate_list.drop(remove_idx) # Remove matches from candidates
    candidate_list = candidate_list[~candidate_list.isin([replace_name])] # Remove matches from candidates
    print(len(candidate_list))
users_data["vendor_address"] = temp_vadd_df

# Cleaning Amounts
temp_amount_df = users_data["amount"].copy() # Return List
# Impute mean of company's amounts into missing value
temp_amount_df.loc[temp_amount_df.isna()] = temp_amount_df.loc[users_data["vendor_name"] == users_data.loc[419,"vendor_name"]].mean()
users_data["amount"] = temp_amount_df

# Writing New User File
users_data.to_csv("../data/interim/Users.csv")
