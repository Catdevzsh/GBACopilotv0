## 
print("Welcome to GBAPY 1.0X")

## please make a gba emulator like no$gba
import socket
import sys
import time
import os
import threading
import time
import random
## please make the framework for the gui and make it look like a gba emulator with the width and height of 800x800
import pygame
from pygame.locals import *
pygame.init()
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from tkinter.colorchooser import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
## make a client gui
class Client(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x803")
        self.title("GBAPY 1.0X")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        #self.update()
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        ## with pygame make a gui resmebling a gba
        def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x803")
        self.title("GBAPY 1.0X")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        #self.update()
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        ## with pygame make a gui resmebling a gba
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a toolbar
        toolbar = Frame(self, bg="black")
        toolbar.pack(side=TOP, fill=X)
        ## make a frame for the buttons
        frame = Frame(self)
        frame.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame2 = Frame(self)
        frame2.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame4 = Frame(self)
        frame4.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame5 = Frame(self)
        frame5.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame6 = Frame(self)
        frame6.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame7 = Frame(self)
        frame7.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame8 = Frame(self)
        frame8.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame9 = Frame(self)
        frame9.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame10 = Frame(self)
        frame10.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame11 = Frame(self)
        frame11.pack(fill=BOTH, expand=YES)
        ## make a frame for the buttons
        frame12 = Frame(self)
        frame

=======

def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x803")
        self.title("GBAPY 1.0X")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        #self.update()
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        ## with pygame make a gui resmebling a gba
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a frame
        self.frame = Frame(self, width=800, height=800)
        self.frame.pack(side=TOP)
        ## make a canvas
        self.canvas = Canvas(self.frame, width=800, height=800, bg="black")
        self.canvas.pack(side=TOP)
        ## make a frame
        self.frame2 = Frame(self, width=800, height=800)
        self.frame2.pack(side=BOTTOM)
        ## make a canvas
        self.canvas2 = Canvas(self.frame2, width=800, height=800, bg="black")
        self.canvas2.pack(side=TOP)
        ## make a frame
        self.frame3 = Frame(self, width=800, height=800)
        self.frame3.pack(side=BOTTOM)
        ## make a canvas
        self.canvas3 = Canvas(self.frame3, width=800, height=800, bg="black")
        self.canvas3.pack(side=TOP)
        ## make a frame
        self.frame4 = Frame(self, width=800, height=800)
        self.frame4.pack(side=BOTTOM)
        ## make a canvas
        self.canvas4 = Canvas(self.frame4, width=800, height=800, bg="black")
        self.canvas4.pack(side=TOP)
        ## make a frame
        self.frame5 = Frame(self, width=800, height=800)
        self.frame5.pack(side=BOTTOM)
        ## make a canvas
        self.canvas5 = Canvas(self.frame5, width=800, height=800, bg="black")

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        self.update()
        ## make a top frame
        self.top_frame = Frame(self)
        self.top_frame.pack(side=TOP, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a left frame
        self.left_frame = Frame(self)
        self.left_frame.pack(side=LEFT, fill=Y)
        ## make a right frame
        self.right_frame = Frame(self)
        self.right_frame.pack(side=RIGHT, fill=Y)
        ## make a middle frame
        self.middle_frame = Frame(self)
        self.middle_frame.pack(side=TOP, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill

=======

def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x803")
        self.title("GBAPY 1.0X")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        #self.update()
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        ## with pygame make a gui resmebling a gba
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a frame for the gui
        self.mainframe = Frame(self)
        self.mainframe.pack(fill=BOTH, expand=1)
        ## make a frame for the gui
        self.frame = Frame(self.mainframe)
        self.frame.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="GBAPY 1.0X")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label = Label(self.frame, text="")
        self.label.pack(fill=BOTH, expand=1)
        ## make a label for the gui
        self.label

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a frame
        self.frame = Frame(self)
        self.frame.pack(side=TOP, fill=BOTH, expand=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_propagate(0)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        ## make a canvas
        self.canvas = Canvas(self.frame)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        self.canvas.config(width=800, height=800)
        self.canvas.create_rectangle(0,0,800,800, fill="white")
        self.canvas.bind("<Button-1>", self.leftclick)
        self.canvas.bind("<Button-2>", self.rightclick)
        self.canvas.bind("<Button-3>", self.rightclick)
        self.canvas.bind("<B1-Motion>", self.leftclick)
        self.canvas.bind("<B2-Motion>", self.rightclick)
        self.canvas.bind("<B3-Motion>", self.rightclick)
        self.canvas.bind("<ButtonRelease-1>", self.leftclick)
        self.canvas.bind("<ButtonRelease-2>", self.rightclick)
        self.canvas.bind("<ButtonRelease-3>", self.rightclick)
        self.canvas.bind("<Key>", self.key)
        self.canvas.bind("<KeyRelease>

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a canvas to draw on
        self.canvas = Canvas(self, width=800, height=800, bg="black")
        self.canvas.pack(fill=BOTH, expand=YES)
        ## make a scrollbar
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        ## make a frame
        self.frame = Frame(self.canvas)
        self.frame.pack()
        ## make a canvas scrollable with scrollbar
        self.canvas.create_window((0,0), window=self.frame, anchor=NW)
        self.frame.bind("<Configure>", self.onFrameConfigure)
        ## make a button
        self.button = Button(self.frame, text="Click me!", command=self.donothing)
        self.button.pack()
        ## make a label
        self.label = Label(self.frame, text="Hello, World!")
        self.label.pack()
        ## make a listbox
        self.listbox = Listbox(self.frame)
        self.listbox.pack()
        ## make a textbox
        self.textbox = Text(self.frame)
        self.textbox.pack()
        ## make a canvas
        self.canvas = Canvas(self.frame, width=800, height=800, bg="black")
        self.canvas.pack()
        ## make a scrollbar
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a toolbar
        toolbar = Frame(self, bg="black")
        toolbar.pack(side=TOP, fill=X)
        ## make a frame
        self.frame = Frame(self, bg="black")
        self.frame.pack(side=TOP, fill=X)
        ## make a canvas
        self.canvas = Canvas(self.frame, bg="black", width=800, height=800)
        self.canvas.pack(fill=X)
        ## make a textbox
        self.textbox = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=25)
        self.textbox.pack(side=TOP, fill=X)
        ## make a textbox
        self.textbox2 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
        self.textbox2.pack(side=TOP, fill=X)
        ## make a textbox
        self.textbox3 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
        self.textbox3.pack(side=TOP, fill=X)
        ## make a textbox
        self.textbox4 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
        self.textbox4.pack(side=TOP, fill=X)
        ## make a textbox
        self.textbox5 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
        self.textbox5.pack(

=======

                helpmenu.add_command(label="About", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a toolbar
        toolbar = Frame(self, bg="grey")
        toolbar.pack(side=TOP, fill=X)
        ## make a frame for the buttons
        frame = Frame(self)
        frame.pack(side=TOP)
        ## make a frame for the buttons
        button_frame = Frame(self)
        button_frame.pack(side=TOP)
        ## make a frame for the buttons
        button_frame2 = Frame(self)
        button_frame2.pack(side=TOP)
        ## make a frame for the buttons
        button_frame3 = Frame(self)
        button_frame3.pack(side=TOP)
        ## make a frame for the buttons
        button_frame4 = Frame(self)
        button_frame4.pack(side=TOP)
        ## make a frame for the buttons
        button_frame5 = Frame(self)
        button_frame5.pack(side=TOP)
        ## make a frame for the buttons
        button_frame6 = Frame(self)
        button_frame6.pack(side=TOP)
        ## make a frame for the buttons
        button_frame7 = Frame(self)
        button_frame7.pack(side=TOP)
        ## make a frame for the buttons
        button_frame8 = Frame(self)
        button_frame8.pack(side=TOP)
        ## make a frame for the buttons
        button_frame9 = Frame(self)
        button_frame9.pack(side=TOP)
        ## make a frame for the buttons
        button_frame10 = Frame(self)
        button_frame10.pack(side=TOP)
        ## make a frame for the buttons
        button_frame11 = Frame(self)
        button_frame11.pack(side=TOP)
        ## make a frame for the buttons
        button_frame12 = Frame(self)
        button_frame12.

=======

def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x803")
        self.title("GBAPY 1.0X")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        #self.update()
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        ## with pygame make a gui resmebling a gba
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a frame
        self.frame = Frame(self, width=800, height=800)
        self.frame.pack(side=TOP)
        ## make a canvas
        self.canvas = Canvas(self.frame, width=800, height=800, bg="black")
        self.canvas.pack(side=TOP)
        ## make a frame
        self.frame2 = Frame(self, width=800, height=800)
        self.frame2.pack(side=BOTTOM)
        ## make a canvas
        self.canvas2 = Canvas(self.frame2, width=800, height=800, bg="black")
        self.canvas2.pack(side=TOP)
        ## make a frame
        self.frame3 = Frame(self, width=800, height=800)
        self.frame3.pack(side=BOTTOM)
        ## make a canvas
        self.canvas3 = Canvas(self.frame3, width=800, height=800, bg="black")
        self.canvas3.pack(side=TOP)
        ## make a frame
        self.frame4 = Frame(self, width=800, height=800)
        self.frame4.pack(side=BOTTOM)
        ## make a canvas
        self.canvas4 = Canvas(self.frame4, width=800, height=800, bg="black")
        self.canvas4.pack(side=TOP)
        ## make a frame
        self.frame5 = Frame(self, width=800, height=800)
        self.frame5.pack(side=BOTTOM)
        ## make a canvas
        self.canvas5 = Canvas(self.frame5, width=800, height=800, bg="black")

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.iconbitmap(r'GBAPY.ico')
        self.update()
        ## make a top frame
        self.top_frame = Frame(self)
        self.top_frame.pack(side=TOP, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a left frame
        self.left_frame = Frame(self)
        self.left_frame.pack(side=LEFT, fill=Y)
        ## make a right frame
        self.right_frame = Frame(self)
        self.right_frame.pack(side=RIGHT, fill=Y)
        ## make a middle frame
        self.middle_frame = Frame(self)
        self.middle_frame.pack(side=TOP, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        ## make a bottom frame
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(side=BOTTOM, fill

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a menu bar
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.on_closing)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a canvas to draw on
        self.canvas = Canvas(self, width=800, height=800, bg="black")
        self.canvas.pack(fill=BOTH, expand=YES)
        ## make a scrollbar
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        ## make a frame
        self.frame = Frame(self.canvas)
        self.frame.pack()
        ## make a canvas scrollable with scrollbar
        self.canvas.create_window((0,0), window=self.frame, anchor=NW)
        self.frame.bind("<Configure>", self.onFrameConfigure)
        ## make a button
        self.button = Button(self.frame, text="Click me!", command=self.donothing)
        self.button.pack()
        ## make a label
        self.label = Label(self.frame, text="Hello, World!")
        self.label.pack()
        ## make a listbox
        self.listbox = Listbox(self.frame)
        self.listbox.pack()
        ## make a textbox
        self.textbox = Text(self.frame)
        self.textbox.pack()
        ## make a canvas
        self.canvas = Canvas(self.frame, width=800, height=800, bg="black")
        self.canvas.pack()
        ## make a scrollbar
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.

=======

                helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.config(menu=menubar)
        ## make a toolbar
        toolbar = Frame(self, bg="black")
        toolbar.pack(side=TOP, fill=X)
        ## make a frame
        self.frame = Frame(self, bg="black")
        self.frame.pack(side=TOP, fill=X)
        ## make a canvas
        self.canvas = Canvas(self.frame, bg="black", width=800, height=800)
        self.canvas.pack(fill=X)
        ## make a textbox
        self.textbox = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
        self.textbox.pack(side=TOP, fill=X)
        ## make a textbox
self.textbox2 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
 self.textbox2.pack(side=TOP, fill=X)
        ## make a textbox
self.textbox3 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
 self.textbox3.pack(side=TOP, fill=X)
        ## make a textbo
self.textbox4 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
self.textbox4.pack(side=TOP, fill=X)
        ## make a textbox
self.textbox5 = Text(self.frame, bg="black", fg="white", font="Helvetica 10", width=80, height=20)
self.textbox5.pack(
