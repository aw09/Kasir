# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:51:00 2020

@author: Agung
"""
import pandas as pd
from dataclasses import dataclass
from BaseModel import BaseModel
from TransactionModel import Transaction
from ProductModel import Product
from AccountModel import *
import TransactionModel


target = 'Cart.csv'
data = pd.read_csv(target)
instances = []

@dataclass
class Cart(BaseModel):
    c_id: str
    transaction: Transaction
    product: Product
    qty: int
    
    def write(self):
        super().write(data, target)


def toObject(df):
    obj = []
    for index, row in df.iterrows():
        row[1] = eval(row[1])
        row[2] = eval(row[2])
        obj.append(Cart(*list(row)))
    return obj

def getAll():
    global instances, data
    data = pd.read_csv(target)
    instances = []
    instances = toObject(data)
    return instances
getAll()

def get(transaction):
    data = getAll()
    result = []
    for i in data:
        if i.transaction == transaction:
            result.append(i)
    return result

def getTotal():
    cart = getAll()
    transaction = TransactionModel.getAll()
    total = [0] * len(transaction)
    for i in range(len(transaction)):
        for n in range(0,len(cart)):
            if cart[n].transaction == transaction[i]:
                total[i] = total[i] + (cart[n].product.price * cart[n].qty)
    return total

t = getTotal()