import tkinter as tk
from tkinter import font as tkFont
from random import randint
import csv
from tempfile import NamedTemporaryFile
import shutil

class bButton(tk.Button):
    def __init__(self, parent=None, **config):
        helv36 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
        tk.Button.__init__(self, parent, config)
        self.config(font=helv36)

class bEntry(tk.Entry):
    def __init__(self, parent=None, **config):
        tk.Entry.__init__(self, parent, config)

class userDbEntry:
    def __init__(self, db, row):
        self.id = row['id']
        self.username = row['username']
        self.password = row['password']
        self.balance = float(row['balance'])
        self.db = db

    def addBalance(self, value):
        if value >= 0:
            updatedBal = self.db.updateBalance(self.username, self.password, value)
            if updatedBal:
                self.balance = updatedBal
                return True
        return False
    
    def subBalance(self, value):
        if value >= 0:
            updatedBal = self.db.updateBalance(self.username, self.password, -abs(value))
            if updatedBal:
                self.balance = updatedBal
                return True
        return False

class dbIO:
    def __init__(self, csvPath):
        self.csvPath = csvPath
    
    def checkLogin(self, username, password):
        with open(self.csvPath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['username'] == username:
                    if row['password'] == password:
                        return userDbEntry(row)
            return False

    def createLogin(self, username, password):
        with open(self.csvPath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            newId = None

            uniqueIdFound = False
            while not uniqueIdFound:
                newId = randint(10000000, 99999999)

                isUnique = True
                for row in reader:
                    if row['username'] == username:
                        return False
                    if row['id'] == newId:
                        isUnique = False
                        break
                
                if isUnique:
                    uniqueIdFound = True

        newUserData = [newId, username, password, 0]
        with open(self.csvPath, 'a') as csvfile:
            writer_object = csv.writer(csvfile)
            writer_object.writerow(newUserData)
        
        return True
    
    def updateBalance(self, username, password, value):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        updated = False

        with open(self.csvPath, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile)
            writer = csv.DictWriter(tempfile)

            for row in reader:
                if row['username'] == username and row['password'] == password:
                    row['balance'] == int(row['balance']) + value
                    updated = int(row['balance'])
                    row = {'id': row['id'], 'username': row['username'], 'password': row['password'], 'balance': row['balance']}
                writer.writerow(row)
        
        shutil.move(tempfile.name, self.csvPath)
        return updated
