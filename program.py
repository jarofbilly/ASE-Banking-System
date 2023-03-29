import tkinter as tk
from bFrames import *

csvIO = dbIO('db/data.csv')

root = tk.Tk()
root.geometry("600x400")

# Login screen.
def Login():
    userDb = None
    loginFrame = LoginFrame(root, csvIO)
    loginFrame.place(relx=0.5, rely=0.5, anchor="c")
    root.wait_window(loginFrame)
    try:
        userDb = loginFrame.userDb
    except:
        pass
    if userDb:
        HomeLoop(userDb)

# Main function switching.
def HomeLoop(userDb):
    switchFrame = None
    homeFrame = HomeFrame(root, userDb)
    homeFrame.place(relx=0.5, rely=0.5, anchor="c")
    root.wait_window(homeFrame)

    if homeFrame.switchTo == 'logout':
        Login()
    elif homeFrame.switchTo is not None:
        match homeFrame.switchTo:
            case 'deposit':
                switchFrame = DepositFrame(root, userDb)
            case 'withdraw':
                pass
            case 'transfer':
                pass
            case 'details':
                pass
        
        switchFrame.place(relx=0.5, rely=0.5, anchor="c")
        root.wait_window(switchFrame)

        if switchFrame.switchTo is not None:
            userDb = switchFrame.userDb
            HomeLoop(userDb)
    else:
        pass

root.after(1, Login)
root.mainloop()