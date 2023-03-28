import tkinter as tk
import tkinter.messagebox
from tkinter import font as tkFont
import csv
from random import randint

userDb = None

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

root = tk.Tk()
root.geometry("600x400")

loginFrame = tk.Frame(root)

userLabel = tk.Label(loginFrame, text="Username")
userField = bEntry(loginFrame)

pwLabel = tk.Label(loginFrame, text="Password")
pwField = bEntry(loginFrame, show="*")

def checkLogin(username, password):
    with open('db/data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username:
                if row['password'] == password:
                    return userDbEntry(row)
        return False

def createLogin(username, password):
    with open('db/data.csv', newline='') as csvfile:
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
    with open('db/data.csv', 'a') as csvfile:
        writer_object = csv.writer(csvfile)
        writer_object.writerow(newUserData)
    
    return True

def handleLogin():
    result = checkLogin(userField.get(), pwField.get())

    if not result:
        tkinter.messagebox.showerror(title="", message="Incorrect username or password!\nIf you have not yet created an account, press create one below.")
    else:
        userDb = result
        tkinter.messagebox.showinfo(title="", message="Logged in successfully!")
    
    userField.delete(0, 'end')
    pwField.delete(0, 'end')

def handleCreate():
    result = createLogin(userField.get(), pwField.get())
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