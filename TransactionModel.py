# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:58:05 2020

@author: Agung
"""

import pandas as pd
from dataclasses import dataclass
from AccountModel import Account
from BaseModel import BaseModel


target = 'Transaction.csv'
data = pd.read_csv(target)
instances = []

@dataclass
class Transaction(BaseModel):
    t_id: str
    date: str
    account: Account
    total: int
    
    def write(self):
        super().write(data, target)

def toObject(df):
    obj = []
    for index, row in df.iterrows():
        row['account'] = eval(row['account'])
        obj.append(Transaction(*list(row)))
    return obj

def getAll():
    global instances, data
    data = pd.read_csv(target)
    instances = []
    instances = toObject(data)
    return instances
getAll()
