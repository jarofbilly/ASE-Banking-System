import tkinter as tk
import tkinter.messagebox
from bUtilities import *

class LoginFrame(tk.Frame):
    def __init__(self, parent=None, db=None, **config):
        tk.Frame.__init__(self, parent, config)
        self.userDb = None

        def handleLogin():
            result = db.checkLogin(userField.get(), pwField.get())

            if not result:
                userField.delete(0, 'end')
                pwField.delete(0, 'end')
                tkinter.messagebox.showerror(title="", message="Incorrect username or password!\nIf you have not yet created an account, press create one below.")
            else:
                self.userDb = result
                tkinter.messagebox.showinfo(title="", message="Logged in successfully!")
                self.destroy()

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

class HomeFrame(tk.Frame):
    def __init__(self, parent=None, userDb=None, **config):
        tk.Frame.__init__(self, parent, config)
        self.userDb = userDb
        self.switchTo = None

        def handleDeposit():
            self.switchTo = "deposit"
            self.destroy()

        def handleWithdraw():
            self.switchTo = "withdraw"
            self.destroy()

        def handleLogout():
            self.switchTo = "logout"
            self.destroy()

        # Element creation.
        depositButton = bButton(self, text="Deposit", command=handleDeposit)
        withdrawButton = bButton(self, text="Withdraw", command=handleWithdraw)
        transferButton = bButton(self, text="Transfer", command=handleDeposit)
        detailsButton = bButton(self, text="View summary", command=handleDeposit)
        logoutButton = bButton(self, text="Log out", command=handleLogout)

        # Placement.
        depositButton.grid(row=0, column=0, columnspan=2, pady=2, sticky='ew')
        withdrawButton.grid(row=1, column=0, columnspan=2, pady=2, sticky='ew')
        transferButton.grid(row=2, column=0, columnspan=2, pady=2, sticky='ew')
        detailsButton.grid(row=3, column=0, columnspan=2, pady=2, sticky='ew')
        logoutButton.grid(row=4, column=0, columnspan=2, pady=2, sticky='ew')

class DepositFrame(tk.Frame):
    def __init__(self, parent=None, db=None, **config):
        tk.Frame.__init__(self, parent, config)
        self.userDb = db
        self.switchTo = None

        def handleDeposit():
            success = self.userDb.addBalance(float(depositField.get()))
            if success:
                tkinter.messagebox.showinfo(title="", message="Task completed successfully!")
                strBalance = "{:.2f}".format(self.userDb.balance)
                balLabel.configure(text=f"Current Balance: £{strBalance}")
            else:
                tkinter.messagebox.showerror(title="", message="Failed to deposit!")
            depositField.delete(0, 'end')

        def handleBack():
            self.switchTo = 'main'
            self.destroy()

        # Element creation.
        strBalance = "{:.2f}".format(self.userDb.balance)
        balLabel = tk.Label(self, text=f"Current Balance: £{strBalance}")
        depositField = bEntry(self)

        depositButton = bButton(self, text="Deposit", command=handleDeposit)
        backButton = bButton(self, text="Back to home", command=handleBack)

        # Placement.
        balLabel.grid(row=0, column=0, columnspan=2, pady=2)
        depositField.grid(row=1, column=0, columnspan=2, pady=2)
        depositButton.grid(row=3, column=0, columnspan=2, pady=2, sticky='ew')
        backButton.grid(row=4, column=0, columnspan=2, pady=2, sticky='ew')

class WithdrawFrame(tk.Frame):
    def __init__(self, parent=None, db=None, **config):
        tk.Frame.__init__(self, parent, config)
        self.userDb = db
        self.switchTo = None

        def handleWithdraw():
            success = self.userDb.subBalance(float(withdrawField.get()))
            if success:
                tkinter.messagebox.showinfo(title="", message="Task completed successfully!")
                strBalance = "{:.2f}".format(self.userDb.balance)
                balLabel.configure(text=f"Current Balance: £{strBalance}")
            else:
                tkinter.messagebox.showerror(title="", message="Failed to withdraw!")
            withdrawField.delete(0, 'end')

        def handleBack():
            self.switchTo = 'main'
            self.destroy()

        # Element creation.
        strBalance = "{:.2f}".format(self.userDb.balance)
        balLabel = tk.Label(self, text=f"Current Balance: £{strBalance}")
        withdrawField = bEntry(self)

        withdrawButton = bButton(self, text="Withdraw", command=handleWithdraw)
        backButton = bButton(self, text="Back to home", command=handleBack)

        # Placement.
        balLabel.grid(row=0, column=0, columnspan=2, pady=2)
        withdrawField.grid(row=1, column=0, columnspan=2, pady=2)
        withdrawButton.grid(row=3, column=0, columnspan=2, pady=2, sticky='ew')
        backButton.grid(row=4, column=0, columnspan=2, pady=2, sticky='ew')