import tkinter as tk
import tkinter.messagebox
from bElements import *

class LoginFrame(tk.Frame):
    def __init__(self, parent=None, db=None, **config):
        tk.Frame.__init__(self, parent, config)

        def handleLogin():
            result = db.checkLogin(userField.get(), pwField.get())

            if not result:
                tkinter.messagebox.showerror(title="", message="Incorrect username or password!\nIf you have not yet created an account, press create one below.")
            else:
                userDb = result
                tkinter.messagebox.showinfo(title="", message="Logged in successfully!")
            
            userField.delete(0, 'end')
            pwField.delete(0, 'end')

        def handleCreate():
            result = db.createLogin(userField.get(), pwField.get())
            if not result:
                tkinter.messagebox.showerror(title="", message="That username is already taken. Please choose another.")
            else:
                tkinter.messagebox.showinfo(title="", message="Account created successfully!\nPlease press login.")

        # Element creation.
        userLabel = tk.Label(self, text="Username")
        userField = bEntry(self)

        pwLabel = tk.Label(self, text="Password")
        pwField = bEntry(self, show="*")

        loginButton = bButton(self, text="Login", command=handleLogin)
        createButton = bButton(self, text="Create an account", command=handleCreate)

        # Placement.
        userLabel.grid(row=0, column=0, pady=2)
        userField.grid(row=0, column=1, pady=2)
        pwLabel.grid(row=1, column=0, pady=2)
        pwField.grid(row=1, column=1, pady=2)
        loginButton.grid(row=3, column=0, columnspan=2, pady=2, sticky="ew")
        createButton.grid(row=4, column=0, columnspan=2, pady=2, sticky="ew")