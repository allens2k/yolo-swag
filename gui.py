import os
import tkinter
import sys
from tkinter import *
from tkinter import messagebox

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

import gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
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
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def iquitlikeafag():
   root.destroy()

def startmainbitch():
   root.destroy()
   os.system('python main.py')

from cooldata import zoom

class Toplevel1:
    def __init__(self, top=None):
     for i in zoom:
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        style = ttk.Style()
        if sys.platform == "win32":
            style.theme_use('winnative')
        style.configure('.',background=_bgcolor)
        style.configure('.',foreground=_fgcolor)
        style.configure('.',font="TkDefaultFont")
        style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("919x454+569+230")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("Correct Zoom Info")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        Label1 = tk.Label(top)
        Label1.place(relx=0.012, rely=0.046, height=47, width=388)
        Label1.configure(activebackground="#f9f9f9")
        Label1.configure(activeforeground="#ffffff")
        Label1.configure(background="#ffffff")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font="-family {Swansea} -size 20 -weight bold -slant italic")
        Label1.configure(foreground="#000000")
        Label1.configure(highlightbackground="#d9d9d9")
        Label1.configure(highlightcolor="black")
        Label1.configure(text='''Check if Period 1 is Correct''')

        Label2_1_1 = tk.Label(top)
        Label2_1_1.place(relx=0.248, rely=0.183, height=30, width=107)
        Label2_1_1.configure(activebackground="#f9f9f9")
        Label2_1_1.configure(activeforeground="black")
        Label2_1_1.configure(background="#ffffff")
        Label2_1_1.configure(disabledforeground="#a3a3a3")
        Label2_1_1.configure(font="-family {Swansea} -size 16 -weight bold -slant italic")
        Label2_1_1.configure(foreground="#000000")
        Label2_1_1.configure(highlightbackground="#d9d9d9")
        Label2_1_1.configure(highlightcolor="black")
        Label2_1_1.configure(text='''Period 1''')

        Label2_1_1_1 = tk.Label(top)
        Label2_1_1_1.place(relx=0.104, rely=0.321, height=30, width=87)
        Label2_1_1_1.configure(activebackground="#f9f9f9")
        Label2_1_1_1.configure(activeforeground="black")
        Label2_1_1_1.configure(background="#ffffff")
        Label2_1_1_1.configure(disabledforeground="#a3a3a3")
        Label2_1_1_1.configure(font="-family {Swansea} -size 16 -weight bold -slant italic")
        Label2_1_1_1.configure(foreground="#000000")
        Label2_1_1_1.configure(highlightbackground="#d9d9d9")
        Label2_1_1_1.configure(highlightcolor="black")
        Label2_1_1_1.configure(text='''URL''')

        Label2_1_1_1_1 = tk.Label(top)
        Label2_1_1_1_1.place(relx=0.039, rely=0.436, height=30, width=113)
        Label2_1_1_1_1.configure(activebackground="#f9f9f9")
        Label2_1_1_1_1.configure(activeforeground="black")
        Label2_1_1_1_1.configure(background="#ffffff")
        Label2_1_1_1_1.configure(disabledforeground="#a3a3a3")
        Label2_1_1_1_1.configure(font="-family {Swansea} -size 16 -weight bold -slant italic")
        Label2_1_1_1_1.configure(foreground="#000000")
        Label2_1_1_1_1.configure(highlightbackground="#d9d9d9")
        Label2_1_1_1_1.configure(highlightcolor="black")
        Label2_1_1_1_1.configure(text='''Start Time''')

        Label2_1_1_1_2 = tk.Label(top)
        Label2_1_1_1_2.place(relx=0.039, rely=0.55, height=30, width=113)
        Label2_1_1_1_2.configure(activebackground="#f9f9f9")
        Label2_1_1_1_2.configure(activeforeground="black")
        Label2_1_1_1_2.configure(background="#ffffff")
        Label2_1_1_1_2.configure(disabledforeground="#a3a3a3")
        Label2_1_1_1_2.configure(font="-family {Swansea} -size 16 -weight bold -slant italic")
        Label2_1_1_1_2.configure(foreground="#000000")
        Label2_1_1_1_2.configure(highlightbackground="#d9d9d9")
        Label2_1_1_1_2.configure(highlightcolor="black")
        Label2_1_1_1_2.configure(text='''End Time''')

        Label2_1_1_1_2_1 = tk.Label(top)
        Label2_1_1_1_2_1.place(relx=-0.012, rely=0.665, height=30
                , width=165)
        Label2_1_1_1_2_1.configure(activebackground="#f9f9f9")
        Label2_1_1_1_2_1.configure(activeforeground="black")
        Label2_1_1_1_2_1.configure(background="#ffffff")
        Label2_1_1_1_2_1.configure(disabledforeground="#a3a3a3")
        Label2_1_1_1_2_1.configure(font="-family {Swansea} -size 12 -weight bold -slant italic")
        Label2_1_1_1_2_1.configure(foreground="#000000")
        Label2_1_1_1_2_1.configure(highlightbackground="#d9d9d9")
        Label2_1_1_1_2_1.configure(highlightcolor="black")
        Label2_1_1_1_2_1.configure(text='''Zoom Password''')

        Label2_1_1_1_2_1_1 = tk.Label(top)
        Label2_1_1_1_2_1_1.place(relx=0.0, rely=0.757, height=40, width=174)

        Label2_1_1_1_2_1_1.configure(activebackground="#f9f9f9")
        Label2_1_1_1_2_1_1.configure(activeforeground="black")
        Label2_1_1_1_2_1_1.configure(background="#ffffff")
        Label2_1_1_1_2_1_1.configure(disabledforeground="#a3a3a3")
        Label2_1_1_1_2_1_1.configure(font="-family {Swansea} -size 11 -weight bold -slant italic")
        Label2_1_1_1_2_1_1.configure(foreground="#000000")
        Label2_1_1_1_2_1_1.configure(highlightbackground="#d9d9d9")
        Label2_1_1_1_2_1_1.configure(highlightcolor="black")
        Label2_1_1_1_2_1_1.configure(text='''Message 5 Minutes''')

        Label2_1_1_1_2_1_1_1 = tk.Label(top)
        Label2_1_1_1_2_1_1_1.place(relx=0.0, rely=0.826, height=20
                , width=167)
        Label2_1_1_1_2_1_1_1.configure(activebackground="#f9f9f9")
        Label2_1_1_1_2_1_1_1.configure(activeforeground="black")
        Label2_1_1_1_2_1_1_1.configure(background="#ffffff")
        Label2_1_1_1_2_1_1_1.configure(disabledforeground="#a3a3a3")
        Label2_1_1_1_2_1_1_1.configure(font="-family {Swansea} -size 12 -weight bold -slant italic")
        Label2_1_1_1_2_1_1_1.configure(foreground="#000000")
        Label2_1_1_1_2_1_1_1.configure(highlightbackground="#d9d9d9")
        Label2_1_1_1_2_1_1_1.configure(highlightcolor="black")
        Label2_1_1_1_2_1_1_1.configure(text='''After Start Time''')

        menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = menubar)

        TLabel1 = ttk.Label(top)
        TLabel1.place(relx=0.775, rely=0.291, height=30, width=142)
        TLabel1.configure(background="#ffffff")
        TLabel1.configure(foreground="#000000")
        TLabel1.configure(font="-family {Segoe UI} -size 10")
        TLabel1.configure(borderwidth="3")
        TLabel1.configure(relief="flat")
        TLabel1.configure(anchor='center')
        TLabel1.configure(justify='left')

        TLabel1_1 = ttk.Label(top)
        TLabel1_1.place(relx=0.784, rely=0.424, height=30, width=63)
        TLabel1_1.configure(background="#ffffff")
        TLabel1_1.configure(foreground="#000000")
        TLabel1_1.configure(font="-family {Segoe UI} -size 10")
        TLabel1_1.configure(borderwidth="3")
        TLabel1_1.configure(relief="flat")
        TLabel1_1.configure(anchor='center')
        TLabel1_1.configure(justify='left')

        TLabel1_1_1 = ttk.Label(top)
        TLabel1_1_1.place(relx=0.784, rely=0.56, height=30, width=63)
        TLabel1_1_1.configure(background="#ffffff")
        TLabel1_1_1.configure(foreground="#000000")
        TLabel1_1_1.configure(font="-family {Segoe UI} -size 10")
        TLabel1_1_1.configure(borderwidth="3")
        TLabel1_1_1.configure(relief="flat")
        TLabel1_1_1.configure(anchor='center')
        TLabel1_1_1.configure(justify='left')

        TLabel1_1_2 = ttk.Label(top)
        TLabel1_1_2.place(relx=0.851, rely=0.424, height=30, width=74)
        TLabel1_1_2.configure(background="#ffffff")
        TLabel1_1_2.configure(foreground="#000000")
        TLabel1_1_2.configure(font="-family {Segoe UI} -size 10")
        TLabel1_1_2.configure(borderwidth="3")
        TLabel1_1_2.configure(relief="flat")
        TLabel1_1_2.configure(anchor='center')
        TLabel1_1_2.configure(justify='left')

        TLabel1_1_2_1 = ttk.Label(top)
        TLabel1_1_2_1.place(relx=0.851, rely=0.56, height=30, width=85)
        TLabel1_1_2_1.configure(background="#ffffff")
        TLabel1_1_2_1.configure(foreground="#000000")
        TLabel1_1_2_1.configure(font="-family {Segoe UI} -size 10")
        TLabel1_1_2_1.configure(borderwidth="3")
        TLabel1_1_2_1.configure(relief="flat")
        TLabel1_1_2_1.configure(anchor='center')
        TLabel1_1_2_1.configure(justify='left')

        TLabel1_1_1_1 = ttk.Label(top)
        TLabel1_1_1_1.place(relx=0.784, rely=0.695, height=30, width=63)
        TLabel1_1_1_1.configure(background="#ffffff")
        TLabel1_1_1_1.configure(foreground="#000000")
        TLabel1_1_1_1.configure(font="-family {Segoe UI} -size 10")
        TLabel1_1_1_1.configure(borderwidth="3")
        TLabel1_1_1_1.configure(relief="flat")
        TLabel1_1_1_1.configure(anchor='center')
        TLabel1_1_1_1.configure(justify='left')

        TLabel1_1_1_1_1 = ttk.Label(top)
        TLabel1_1_1_1_1.place(relx=0.794, rely=0.805, height=40, width=77)
        TLabel1_1_1_1_1.configure(background="#ffffff")
        TLabel1_1_1_1_1.configure(foreground="#000000")
        TLabel1_1_1_1_1.configure(font="-family {Segoe UI} -size 10")
        TLabel1_1_1_1_1.configure(borderwidth="3")
        TLabel1_1_1_1_1.configure(relief="flat")
        TLabel1_1_1_1_1.configure(anchor='center')
        TLabel1_1_1_1_1.configure(justify='left')

        TEntry1 = ttk.Entry(top)
        TEntry1.insert(0, (i[0]))
        TEntry1.place(relx=0.207, rely=0.321, relheight=0.071
                , relwidth=0.194)
        TEntry1.configure(font="-family {Arial} -size 10")
        TEntry1.configure(takefocus="")
        TEntry1.configure(cursor="ibeam")

        TEntry1_1 = ttk.Entry(top)
        TEntry1_1.insert(0, (i[1]))
        TEntry1_1.place(relx=0.207, rely=0.436, relheight=0.071
                , relwidth=0.194)
        TEntry1_1.configure(font="-family {Arial} -size 10")
        TEntry1_1.configure(takefocus="")
        TEntry1_1.configure(cursor="ibeam")

        TEntry1_2 = ttk.Entry(top)
        TEntry1_2.insert(0, (i[2]))
        TEntry1_2.place(relx=0.207, rely=0.55, relheight=0.071
                , relwidth=0.194)
        TEntry1_2.configure(font="-family {Arial} -size 10")
        TEntry1_2.configure(takefocus="")
        TEntry1_2.configure(cursor="ibeam")

        TEntry1_3 = ttk.Entry(top)
        TEntry1_3.insert(0, (i[3]))
        TEntry1_3.place(relx=0.207, rely=0.665, relheight=0.071
                , relwidth=0.194)
        TEntry1_3.configure(font="-family {Arial} -size 10")
        TEntry1_3.configure(takefocus="")
        TEntry1_3.configure(cursor="ibeam")

        TEntry1_4 = ttk.Entry(top)
        TEntry1_4.insert(0, (i[4]))
        TEntry1_4.place(relx=0.207, rely=0.78, relheight=0.071
                , relwidth=0.194)
        TEntry1_4.configure(font="-family {Arial} -size 10")
        TEntry1_4.configure(takefocus="")
        TEntry1_4.configure(cursor="ibeam")

        Label2_1_1_2 = tk.Label(top)
        Label2_1_1_2.place(relx=0.501, rely=0.022, height=32, width=431)
        Label2_1_1_2.configure(activebackground="#f9f9f9")
        Label2_1_1_2.configure(activeforeground="black")
        Label2_1_1_2.configure(background="#ffffff")
        Label2_1_1_2.configure(disabledforeground="#a3a3a3")
        Label2_1_1_2.configure(font="-family {Swansea} -size 16 -weight bold -slant italic")
        Label2_1_1_2.configure(foreground="#000000")
        Label2_1_1_2.configure(highlightbackground="#d9d9d9")
        Label2_1_1_2.configure(highlightcolor="black")
        Label2_1_1_2.configure(text='''Read before using (you will miss class)''')

        TLabel2_1 = ttk.Label(top)
        TLabel2_1.place(relx=0.468, rely=0.183, height=61, width=463)
        TLabel2_1.configure(background="#ffffff")
        TLabel2_1.configure(foreground="#000000")
        TLabel2_1.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_1.configure(relief="flat")
        TLabel2_1.configure(anchor='center')
        TLabel2_1.configure(justify='left')
        TLabel2_1.configure(wraplength="450")
        TLabel2_1.configure(
           text='''Make sure your logged into your student account in a browser you don't use like Internet Explorer to bypass picking an account during Zoom Login''')

        TLabel2_3 = ttk.Label(top)
        TLabel2_3.place(relx=0.446, rely=0.093, height=40, width=496)
        TLabel2_3.configure(background="#ffffff")
        TLabel2_3.configure(foreground="#000000")
        TLabel2_3.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_3.configure(relief="flat")
        TLabel2_3.configure(anchor='center')
        TLabel2_3.configure(justify='left')
        TLabel2_3.configure(wraplength="450")
        TLabel2_3.configure(
           text='''If your info isn't correct change the config file in the root directory using a text editor''')

        TLabel2 = ttk.Label(top)
        TLabel2.place(relx=0.522, rely=0.848, height=31, width=396)
        TLabel2.configure(background="#ffffff")
        TLabel2.configure(foreground="#000000")
        TLabel2.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2.configure(relief="flat")
        TLabel2.configure(anchor='center')
        TLabel2.configure(justify='left')
        TLabel2.configure(wraplength="340")
        TLabel2.configure(text='''Keyboard Shortcuts: Defaulted (Important)''')

        TLabel2_4 = ttk.Label(top)
        TLabel2_4.place(relx=0.577, rely=0.665, height=20, width=270)
        TLabel2_4.configure(background="#ffffff")
        TLabel2_4.configure(foreground="#000000")
        TLabel2_4.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_4.configure(relief="flat")
        TLabel2_4.configure(anchor='center')
        TLabel2_4.configure(justify='left')
        TLabel2_4.configure(wraplength="340")
        TLabel2_4.configure(text='''Zoom Settings (default otherwise)''')

        TLabel2_5 = ttk.Label(top)
        TLabel2_5.place(relx=0.566, rely=0.711, height=20, width=293)
        TLabel2_5.configure(background="#ffffff")
        TLabel2_5.configure(foreground="#000000")
        TLabel2_5.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_5.configure(relief="flat")
        TLabel2_5.configure(anchor='center')
        TLabel2_5.configure(justify='left')
        TLabel2_5.configure(wraplength="340")
        TLabel2_5.configure(text='''General: Uncheck Ask me to confirm....''')

        TLabel2_5_1 = ttk.Label(top)
        TLabel2_5_1.place(relx=0.555, rely=0.758, height=20, width=345)
        TLabel2_5_1.configure(background="#ffffff")
        TLabel2_5_1.configure(foreground="#000000")
        TLabel2_5_1.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_5_1.configure(relief="flat")
        TLabel2_5_1.configure(anchor='center')
        TLabel2_5_1.configure(justify='left')
        TLabel2_5_1.configure(wraplength="340")
        TLabel2_5_1.configure(text='''Audio: Check Automatically join audio...''')

        TLabel2_5_1_1 = ttk.Label(top)
        TLabel2_5_1_1.place(relx=0.609, rely=0.804, height=20, width=299)
        TLabel2_5_1_1.configure(background="#ffffff")
        TLabel2_5_1_1.configure(foreground="#000000")
        TLabel2_5_1_1.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_5_1_1.configure(relief="flat")
        TLabel2_5_1_1.configure(anchor='center')
        TLabel2_5_1_1.configure(justify='left')
        TLabel2_5_1_1.configure(wraplength="340")
        TLabel2_5_1_1.configure(text='''Check Mute my microphon when...''')

        TLabel2_2 = ttk.Label(top)
        TLabel2_2.place(relx=0.457, rely=0.308, height=40, width=473)
        TLabel2_2.configure(background="#ffffff")
        TLabel2_2.configure(foreground="#000000")
        TLabel2_2.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_2.configure(relief="flat")
        TLabel2_2.configure(anchor='center')
        TLabel2_2.configure(justify='left')
        TLabel2_2.configure(wraplength="450")
        TLabel2_2.configure(
           text='''Because bot uses Internet Explorer or if not then you can only use your school account in your primary browser''')

        TLabel2_2_1 = ttk.Label(top)
        TLabel2_2_1.place(relx=0.468, rely=0.396, height=61, width=463)
        TLabel2_2_1.configure(background="#ffffff")
        TLabel2_2_1.configure(foreground="#000000")
        TLabel2_2_1.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_2_1.configure(relief="flat")
        TLabel2_2_1.configure(anchor='center')
        TLabel2_2_1.configure(justify='left')
        TLabel2_2_1.configure(wraplength="450")
        TLabel2_2_1.configure(
           text='''This bot will run continuously and doesn't stop so if it does stop you have to change the config text file to your next period because it will only start on next period''')

        TLabel2_2_1_1 = ttk.Label(top)
        TLabel2_2_1_1.place(relx=0.468, rely=0.529, height=61, width=463)
        TLabel2_2_1_1.configure(background="#ffffff")
        TLabel2_2_1_1.configure(foreground="#000000")
        TLabel2_2_1_1.configure(font="-family {Lato Semibold} -size 11 -weight bold")
        TLabel2_2_1_1.configure(relief="flat")
        TLabel2_2_1_1.configure(anchor='center')
        TLabel2_2_1_1.configure(justify='left')
        TLabel2_2_1_1.configure(wraplength="450")
        TLabel2_2_1_1.configure(
           text='''If you are planning to run this overnight or go to sleep you must have your power settings to never go to sleep. So use turn off display only because it work on that or you can use Task Scheduler''')

        TButton1_1 = ttk.Button(top, command= iquitlikeafag)
        TButton1_1.place(relx=0.544, rely=0.925, height=25, width=126)
        TButton1_1.configure(takefocus="")
        TButton1_1.configure(text='''Close''')
        TButton1_1.configure(cursor="heart")

        TButton1_1_1 = ttk.Button(top, command= startmainbitch)
        TButton1_1_1.place(relx=0.794, rely=0.925, height=25, width=126)
        TButton1_1_1.configure(takefocus="")
        TButton1_1_1.configure(text='''Start''')
        TButton1_1_1.configure(cursor="heart")
        top.mainloop()

if __name__ == '__main__':
    vp_start_gui()





