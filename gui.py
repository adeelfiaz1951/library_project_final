from auth import AuthDB
import tkinter as tk
from tkinter import messagebox
from menu import start_menu

class LoginGui:
    # tkinter login and registration GUI

    def __init__(self):
        self.auth = AuthDB()
        self.root = tk.Tk()
        self.root.title("Library Login")
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
        self.login_password = tk.Entry(root, show='*')
        self.login_password.pack()

        tk.Button(root, text='Login', command=self.login_action).pack(pady=10)
        tk.Button(root, text='Register', command=self.show_register).pack()

    # Registration Window

    def show_register(self):
        self.clear_window()
        root = self.root

        tk.Label(root, text='Register', font=('Arial', 16)).pack(pady=10)

        tk.Label(root, text='Username').pack()
        self.reg_username = tk.Entry(root)
        self.reg_username.pack()

        tk.Label(root, text='Email').pack()
        self.reg_email = tk.Entry(root)
        self.reg_email.pack()

        tk.Label(root,text='Password').pack()
        self.reg_password = tk.Entry(root, show='*')
        self.reg_password.pack()

        tk.Label(root,text='Confirm Password').pack()
        self.reg_confirm = tk.Entry(root, show='*')
        self.reg_confirm.pack()

        tk.Button(root, text="Create Account", command=self.register_action).pack(pady=10)
        tk.Button(root, text="Back to Login", command=self.show_login).pack

        # Login and Registration Action

    def login_action(self):
        username = self.login_username.get()
        password = self.login_password.get()

        if self.auth.validate_user(username, password):
            messagebox.showinfo('Success', "LoginSucceful!")
            self.root.destroy()
            print("Login succeful")

            # call here menu.py
            start_menu()
        else:
            messagebox.showerror("Error", 'Incorrect username or password')

    def register_action(self):
        username = self.reg_username.get()
        email = self.reg_email.get()
        pwd = self.reg_password.get()
        confirm = self.reg_confirm.get()

        if pwd != confirm:
            messagebox.showerror("Error", "Password do not match")
            return
        success = self.auth.register_user(username, email, pwd)

        if success:
            messagebox.showinfo("Success", "Account created now you can login")
            self.show_login()
        else:
            messagebox.showerror('Error', 'Username already exists')
            
        # utility

    def clear_window(self):
        '''Remove all widgets from window '''
        for widget in self.root.winfo_children():
            widget.destroy()

# Run GUI

if __name__ == '__main__':
    LoginGui()