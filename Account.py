# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:55:12 2020

@author: Agung
"""
import pandas as pd
import uuid 

target = 'Account.csv'
df = pd.read_csv(target)

def register(tipe, username, email, password):
    global df
    df2 = pd.DataFrame([[uuid.uuid4(), tipe, username, email, password]], 
                       columns=list(df.columns.values))
    df = pd.concat([df,df2])
    df.to_csv(target, index=False)

def login(username, password):
    global df
    result = df[(df['username']==username) & (df['password']==password)]
    return result
 
def listPelanggan():
    result = df.copy()
    result = result.groupby('username')['username'].sum().reset_index(drop=True).values.tolist()
    return result
    
#register('Pelanggan', 'tes', 'tes', 'tes')
tes = listPelanggan()
