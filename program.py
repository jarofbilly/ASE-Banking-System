import tkinter as tk
import tkinter.messagebox
import csv
from random import randint
from bElements import *

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

loginFrame = tk.Frame(root)

userLabel = tk.Label(loginFrame, text="Username")
userField = bEntry(loginFrame)

pwLabel = tk.Label(loginFrame, text="Password")
pwField = bEntry(loginFrame, show="*")

def handleLogin():
    result = csvIO.checkLogin(userField.get(), pwField.get())

    if not result:
        tkinter.messagebox.showerror(title="", message="Incorrect username or password!\nIf you have not yet created an account, press create one below.")
    else:
        userDb = result
        tkinter.messagebox.showinfo(title="", message="Logged in successfully!")
    
    userField.delete(0, 'end')
    pwField.delete(0, 'end')

def handleCreate():
    result = csvIO.createLogin(userField.get(), pwField.get())
    if not result:
        tkinter.messagebox.showerror(title="", message="That username is already taken. Please choose another.")
    else:
        tkinter.messagebox.showinfo(title="", message="Account created successfully!\nPlease press login.")

loginButton = bButton(loginFrame, text="Login", command=handleLogin)
createButton = bButton(loginFrame, text="Create an account", command=handleCreate)

userLabel.grid(row=0, column=0, pady=2)
userField.grid(row=0, column=1, pady=2)

pwLabel.grid(row=1, column=0, pady=2)
pwField.grid(row=1, column=1, pady=2)

loginButton.grid(row=3, column=0, columnspan=2, pady=2, sticky="ew")
createButton.grid(row=4, column=0, columnspan=2, pady=2, sticky="ew")

loginFrame.place(relx=0.5, rely=0.5, anchor="c")
root.mainloop()