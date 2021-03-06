#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# gar module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Jan 29, 2021 05:16:46 PM PST  platform: Windows NT
import os
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

import gar_support



def vp_start_gar():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gar_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gar_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def oooohkillem():
    sys.exit()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("312x129+797+264")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Running")
        top.configure(background="#0d4855")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TProgressbar1 = ttk.Progressbar(top)
        self.TProgressbar1.place(relx=0.128, rely=0.698, relwidth=0.769
                , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="240")
        self.TProgressbar1.configure(mode="indeterminate")

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.16, rely=0.0, height=41, width=225)
        self.TLabel1.configure(background="#0d4855")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {Segoe UI} -size 16")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Currently Running Bot''')

        self.TButton1 = ttk.Button(top, command= oooohkillem)
        self.TButton1.place(relx=0.385, rely=0.357, height=25, width=76)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Stop''')

if __name__ == '__main__':
    vp_start_gar()





