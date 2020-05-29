# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:01:54 2020

@author: Agung
"""
import pandas as pd
import uuid
class BaseModel:
    def write(self, data, target):
        values = list(vars(self).values())
        attr = list(vars(self).keys())
        df = pd.DataFrame([values], 
                          columns=attr)
        data = pd.concat([data,df])
        data.to_csv(target, index=False) 
