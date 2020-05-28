#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    May 27, 2020 08:53:33 PM +07  platform: Windows NT

import sys
import Transaction as t
import Detail as d

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
    global combobox
    combobox = tk.StringVar()

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

def new(pelanggan):
    destroy_window()
    d.new_transaction(pelanggan)

if __name__ == '__main__':
    import PilihPelanggan
    PilihPelanggan.vp_start_gui()




