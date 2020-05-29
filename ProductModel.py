# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:58:05 2020

@author: Agung
"""

import pandas as pd
from dataclasses import dataclass
from AccountModel import Account
from BaseModel import BaseModel

target = 'Product.csv'
data = pd.read_csv(target)
instances = []

@dataclass
class Product(BaseModel):
    p_id: str
    name: str
    price: int
    
    def write(self):
        super().write(data, target)
        instances.append(self)

def getData(df=data):
    global instances
    instances = []
    for index, row in df.iterrows():
        instances.append(Product(*list(row)))
        
def getAll():
    return instances

getData()

