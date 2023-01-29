import pandas as pd
#from modules.lavenshtein import lavenshtein, get_laven
from Levenshtein import distance
import os
from multiprocessing import Pool
from tqdm import tqdm
from modules.rev_helper import rev_helper


def remove_element_at_position(value):
    if not value['position']:
        return pd.Series({'documentid':value['documentid'],'pot_doc':value['pot_doc'],'pot_name':value['pot_name'], 'pot_price':value['pot_price'],'pot_address':value['pot_address'],'pot_date':value['pot_date']})
    pot_doc = [value['pot_doc'][i] for i in value['position']]
    pot_name = [value['pot_name'][i] for i in value['position']]
    pot_price = [value['pot_price'][i] for i in value['position']]
    pot_address = [value['pot_address'][i] for i in value['position']]
    pot_date = [value['pot_date'][i] for i in value['position']]
    return pd.Series({'documentid':value['documentid'],'pot_doc':pot_doc,'pot_name':pot_name, 'pot_price':pot_price,'pot_address':pot_address,'pot_date':pot_date})


'''
iterates through all the ocr files an finds the Levenshtein distance between the file's 
text content and the provided user data.
outputs a dataframe with the documentid, a list of potential userids, and a list of their
corresponding Levenshtein distances
'''
columns = ["BB1", "BB2", "BB3", "BB4", "BB5", "BB6", "BB7", "BB8", "Text_Main"]
columns_labels = ["documentid","pot_doc","pot_name","pot_price","pot_date","pot_address",]
ocrdir = 'data/interim/ocr/'
levan_user = pd.DataFrame(columns=columns_labels)
#reads user data
users_data = pd.read_csv("data/interim/Users.csv")
#removes all files that are not present in the user file
file_names = [os.path.splitext(file)[0] for file in list(os.listdir(ocrdir))]
file_names = [x for x in file_names if x in users_data['documentid'].values]
file_names = [file_name + '.csv' for file_name in file_names]
#pools the function so that it runs in paralell
with Pool() as p:
    q = p.map(rev_helper, zip(file_names, [users_data for _ in range(len(os.listdir(ocrdir)))]))
for qq in q:
    levan_user.loc[len(levan_user)] = qq

df = levan_user
        
df['position'] = df['pot_date'].apply(lambda x: [i for i, x in enumerate(x) if x == 1])

df = df.apply(remove_element_at_position, axis=1)

df.to_csv(os.path.join('data/final/', "final.csv"))