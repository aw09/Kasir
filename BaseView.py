# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:15:56 2020

@author: Agung
"""

import sys
import uuid
from tkinter.messagebox import showinfo
from datetime import datetime

from AccountModel import *
from TransactionModel import *
from CartModel import *
import AccountModel, TransactionModel, CartModel
import Login, TransactionList, Detail, PickClient, OrderConfirmation


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global type
    type = tk.StringVar()
    #global username
    #username = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None   

def genId():
    return str(uuid.uuid4())

def getDate():
    return datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

def redirect(view, *args):
    destroy_window()
    view.start(*args)
    
def register(tipe, username, email, password, c_password):
    if password == c_password:
        user = Account(genId(), tipe, username, email, password)
        user.write()
        showinfo("","Register Succeded !")
        redirect(Login)
    else:
        showinfo("","Check Password !!!")
        
def login(username, password):
    user = AccountModel.findAccount(username, password)
    if user.tipe == 'Karyawan':
        redirect(TransactionList, user)
    else:
        moreTransaction(user)

def newTransaction():
    transaction = Transaction(genId(), getDate(), None, 0)
    redirect(PickClient, transaction)

def viewCart(client, transaction):
    transaction.account = client
    redirect(Detail, transaction)
    
def addProduct(transaction, product, qty):
    cart = Cart(genId(), transaction, product, qty)
    cart.write()
    redirect(Detail, transaction)
    
def confirmation(transaction):
    transaction.write()
    redirect(OrderConfirmation, transaction.account)

def moreTransaction(user):
    transaction = Transaction(genId(), getDate(), user, 0)
    redirect(Detail, transaction)

def cancel(transaction):
    redirect(Detail, transaction)
