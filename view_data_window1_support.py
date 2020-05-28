#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Mar 06, 2020 11:25:00 AM IST  platform: Windows NT

import sys

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
    global Ecombobox1, Ecombobox2, Ecombobox3, Wcombobox1, Wcombobox2, Wcombobox3, Gcombobox1, Gcombobox2, Gcombobox3, Wscombox
    Ecombobox1 = tk.StringVar(None,"All")
    Ecombobox2 = tk.StringVar(None,"All")
    Ecombobox3 = tk.StringVar(None,"All")

    Wcombobox1 = tk.StringVar(None,"All")
    Wcombobox2 = tk.StringVar(None,"All")
    Wcombobox3 = tk.StringVar(None,"All")

    Gcombobox1 = tk.StringVar(None,"All")
    Gcombobox2 = tk.StringVar(None,"All")
    Gcombobox3 = tk.StringVar(None,"By Month")

    Wscombox = tk.StringVar(None, "All")

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

if __name__ == '__main__':
    import view_data_window1
    view_data_window1.vp_start_gui()




