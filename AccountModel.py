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
instances = []

@dataclass
class Account(BaseModel):
    u_id: str
    tipe: str
    username: str
    email: str
    password: str 
    
    def write(self):
        super().write(data, target)
    

def toObject(df):
    obj = []
    for index, row in df.iterrows():
        obj.append(Account(*list(row)))
    return obj

def getAll():
    global instances, data
    data = pd.read_csv(target)
    instances = []
    instances = toObject(data)
    return instances
getAll()


def findAccount(username,password):
    getAll()
    for i in instances:
        if (i.username == username) & (i.password==password):
            return i

def getClient():
    getAll()
    client = []
    for i in instances:
        if(i.tipe == 'Pelanggan'):
            client.append(i)
    return client

