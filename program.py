import tkinter as tk
import csv
from random import randint
from bFrames import *

userDb = None

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

csvIO = dbIO('db/data.csv')

root = tk.Tk()
root.geometry("600x400")

loginFrame = LoginFrame(root, csvIO)
loginFrame.place(relx=0.5, rely=0.5, anchor="c")

root.mainloop()