# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:58:05 2020

@author: Agung
"""

import pandas as pd
from dataclasses import dataclass
from datetime import datetime
from AccountModel import Account
from BaseModel import BaseModel

target = 'Transaction.csv'
data = pd.read_csv(target)

@dataclass
class Transaction(BaseModel):
    t_id: str
    date: str
    account: Account
    total: int
    
    def write(self):
        return super().write(data)
    
   
'''    
ac = Account('234', 'Karyawan', 'agung', 'agung@gmail.com', 'agung')   
date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
t = Transaction('123', date, ac, 10000)
attr = list(vars(t).keys())

df = pd.DataFrame([[t.t_id,t.date,t.account,t.total]], 
                   columns=attr)
'''

instances = []
def getInstances():
    for index, row in data.iterrows():
        instances.append(Transaction(*list(row)))
        



