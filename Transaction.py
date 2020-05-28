# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:58:05 2020

@author: Agung
"""

import pandas as pd
import uuid

transaksi = pd.read_csv('Transaction.csv')
detail = pd.read_csv('Detail.csv')

def newTransaction(t_id,tanggal,pelanggan,total):
    df = pd.DataFrame([[uuid.uuid4().int, tanggal, pelanggan, total]], 
                       columns=list(transaksi.columns.values))
    transaksi.to_csv('Transaction.csv', index=False)
