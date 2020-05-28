# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:55:12 2020

@author: Agung
"""

import pandas as pd
from dataclasses import dataclass
from BaseModel import BaseModel

target = 'Account.csv'
data = pd.read_csv(target)
@dataclass
class Account(BaseModel):
    u_id: str
    tipe: str
    username: str
    email: str
    password: str 
    
    def write(self):
        super().write(data, target)

instances = []
def getInstances():
    for index, row in data.iterrows():
        instances.append(Account(*list(row)))
    return instances

