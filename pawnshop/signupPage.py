import tkinter
from tkinter import *
from tkinter import messagebox
from functools import partial
from ttkbootstrap import Style
from tkinter import ttk
import db_conn

class Signup:
    def __init__(self, root1):
        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Signup Window")
        self.root.geometry("414x896")

        #textbox labels and labels
        self.firstnameLabel = ttk.Label(self.root, text="Firstname: ",).grid(row=0, column=0)
        self.firstname = StringVar()
        self.firstnameEntry = ttk.Entry(self.root, textvariable=self.firstname)
        self.firstnameEntry.grid(row=0, column=1)

        self.lastnameLabel = ttk.Label(self.root, text="Lastname: ",).grid(row=1, column=0)
        self.lastname = StringVar()
        self.lastnameEntry = ttk.Entry(self.root, textvariable=self.lastname)
        self.lastnameEntry.grid(row=1, column=1)

        self.emailLabel = ttk.Label(self.root, text="Email: ",).grid(row=2, column=0)
        self.email = StringVar()
        self.emailEntry = ttk.Entry(self.root, textvariable=self.email)
        self.emailEntry.grid(row=2, column=1)

        self.usernameLabel = ttk.Label(self.root, text="Username: ",).grid(row=3, column=0)
        self.username = StringVar()
        self.usernameEntry = ttk.Entry(self.root, textvariable=self.username)
        self.usernameEntry.grid(row=3, column=1)

        self.passwordLabel = ttk.Label(self.root, text="Password: ",).grid(row=4, column=0)
        self.password = StringVar()
        self.passwordEntry = ttk.Entry(self.root, textvariable=self.password)
        self.passwordEntry.grid(row=4, column=1)

        #signup button
        self.btn_signup = ttk.Button(self.root, text="Signup", width=10, command = self.insertNewuser)
        self.btn_signup.grid(row=5, column=1)

        self.root.mainloop()

    def insertNewuser(self):
        self.txt_username = self.username.get()
        self.txt_password = self.password.get()
        self.txt_firstname = self.firstname.get()
        self.txt_lastname = self.lastname.get()
        self.txt_email = self.email.get()

        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()

        self.sql = "INSERT INTO tbl_user_profile (firstname, lastname, email, username, password) VALUES (%s, %s, %s, %s, %s)"
        self.val = (self.txt_firstname, self.txt_lastname, self.txt_email, self.txt_username, self.txt_password)
        self.cur.execute(self.sql, self.val)

        self.conn.commit()
        print(self.cur.rowcount, "record inserted.")
        self.messagebox.showinfo("result", "User created")

