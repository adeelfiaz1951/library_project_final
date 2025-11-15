from auth import AuthDB
import tkinter as tk
from tkinter import messagebox

class LoginGui:
    # tkinter login and registration GUI

    def __init__(self):
        self.auth = AuthDB()
        self.root = tk.Tk()
        self.title("Library Login")
        self.root.geometry('350x250')

        self.show_login()

        self.root.mainloop()

    # Login window

    def show_login(self):
        self.clear_window()
        root = self.root

        tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text='Username').pack()
        self.login_username = tk.Entry(root)
        self.login_username.pack()

        tk.Label(root, text='Password').pack()
        self.login_password = tk.Entry(root)
        self.login_password.pack()

        tk.Button(root, text='Login', command=self.login_action).pack(pady=10)
        tk.Button(root, text='Register', command=self.show_register).pack()
