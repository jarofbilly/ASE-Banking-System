import tkinter as tk
from bFrames import *

userDb = None

csvIO = dbIO('db/data.csv')

root = tk.Tk()
root.geometry("600x400")


loginFrame = LoginFrame(root, csvIO)
loginFrame.place(relx=0.5, rely=0.5, anchor="c")
root.wait_window(loginFrame)
userDb = loginFrame.userDb

homeFrame = HomeFrame(root, userDb)
homeFrame.place(relx=0.5, rely=0.5, anchor="c")
root.wait_window(homeFrame)

root.mainloop()