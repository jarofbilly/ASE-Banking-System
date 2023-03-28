import tkinter as tk
from tkinter import font as tkFont

class bButton(tk.Button):
    def __init__(self, parent=None, **config):
        helv36 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
        tk.Button.__init__(self, parent, config)
        self.config(font=helv36)

class bEntry(tk.Entry):
    def __init__(self, parent=None, **config):
        tk.Entry.__init__(self, parent, config)

class userDbEntry:
    def __init__(self, row):
        self.id = row['id']
        self.username = row['username']
        self.password = row['password']
        self.balance = float(row['balance'])