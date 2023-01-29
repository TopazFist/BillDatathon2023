import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import optuna

def compute_accuracy(x, y, z,a):
    results = []
    for row in X_train_df.iterrows():
        if (len(eval(row[1]['pot_doc']))==0):
            continue
        dists = []
        
        for idx in range(len(eval(row[1]['pot_doc']))):
            dists.append((x*(100-eval(row[1]['pot_price'])[idx])/100)**2 
            + (y*(1-eval(row[1]['pot_date'])[idx]))**2)
            
        dists = np.array(dists)
        results.append(eval(row[1]['pot_doc'])[dists.argmin()])
    results = np.array(results)
    return np.sum(results == np.array(y_train_df['documentid']))/len(X_train_df)
    
def compute_accuracy2(x, y, z, a):
    results = []
    for row in X_test_df.iterrows():
        if (len(eval(row[1]['pot_doc']))==0):
            continue
        dists = []
        
        for idx in range(len(eval(row[1]['pot_doc']))):
            dists.append((x*(100-eval(row[1]['pot_price'])[idx])/100)**2 
            + (y*(1-eval(row[1]['pot_date'])[idx]))**2
            + (z*(100-eval(row[1]['pot_address'])[idx])/100)**2
            #+ (a*eval(row[1]['pot_name'])[idx])**2
            )
        dists = np.array(dists)
        results.append(eval(row[1]['pot_doc'])[dists.argmin()])
    results = np.array(results)
    return results

def objective(trial):
    x = trial.suggest_float('x', 0, 10)
    y = trial.suggest_float('y', 0, 10)
    #z = trial.suggest_float('z', 0, 1)
    #a = trial.suggest_float('a', 0, 10)
    return 1-compute_accuracy(x,y,1,0)

def calculate_percentage(list_a, list_b):
    common_elements = set(list_a) & set(list_b)
    percentage = (len(common_elements) / len(list_a)) * 100
    return percentage

df = pd.read_csv("data/final/final.csv")
df = df[df['pot_doc'] != '[]']

y = np.array(df['documentid'])
X = np.array(df)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
x_column = list(df.columns)
x_column.remove('documentid')

X_train_df = pd.DataFrame(data = X_train, columns = df.columns)
X_test_df = pd.DataFrame(data = X_test, columns = df.columns)
y_train_df = pd.DataFrame(data = y_train, columns = ['documentid'])
y_test_df = pd.DataFrame(data = y_test, columns = ['documentid'])

X_train_df= X_train_df.drop(columns="documentid").drop(columns="Unnamed: 0")
X_test_df= X_test_df.drop(columns="documentid").drop(columns="Unnamed: 0")

study = optuna.create_study()
study.optimize(objective, n_trials=100)

study.best_params  # E.g. {'x': 2.002108042}

res = compute_accuracy2(study.best_params['x'], 1, study.best_params['y'], 0)

real = list(y_test_df['documentid'])

print(len(res), len(real))
print(calculate_percentage(res,real))

c = 0
for i in range(len(res)):
    if res[i] != real[i] and real[i] in eval(X_train_df['pot_doc'][i]):
        print(res[i], real[i])
        c += 1
print(c, 'mismatches')