# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:51:00 2020

@author: Agung
"""

@dataclass
class Cart(BaseModel):
    t_id: str
    date: str
    account: Account
    total: int
    
    def write(self):
        return super().write(data)