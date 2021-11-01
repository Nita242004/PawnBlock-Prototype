from tkinter import *
from PIL import ImageTk, Image
from overlay import Window
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk, font, messagebox
import db_conn
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
from tkinter import ttk

style = Style(theme='lumen')
root = style.master

style.configure('TButton', font=("Helvetica", 16))
style.configure('my.TButton', font=("Helvetica", 10))
style.configure("menustyle.TFrame", background = "gray")
style.configure('login.TNotebook', tabposition='nsew')
style.configure("transparent.TButton")
style.configure("scrolltab.TButton")
style.configure("invisible.Horizontal.TScrollbar")
style.configure("item.TButton")

root.title("Login Window")
root.geometry("414x896")

    #textbox labels and labels
load = Image.open("Images/pawnblock_ss.png")
resized_image= load.resize((87,159), Image.ANTIALIAS)
render= ImageTk.PhotoImage(resized_image)
img = Label(root, image=render)
img.image = render
img.grid(row=0, column=0, columnspan=2, ipadx= 5, ipady=20, sticky=S)

# Tab
tabControl = ttk.Notebook(root, width=350, height=520, style='login.TNotebook')
tabControl.grid(row=1, column=0, columnspan=2, padx=30)
#
login = ttk.Frame(root)
signup = ttk.Frame(root)
#
tabControl.add(login, text="Login")
tabControl.add(signup, text="Signup")

#login
#textbox labels and labels
usernameLabel = ttk.Label(login, text="   Username: ", style='primary.TLabel')
usernameLabel.grid(row=1, column=0, ipadx= 5, ipady=20, sticky=E)

username = StringVar()
usernameEntry = ttk.Entry(login, textvariable=username, style='info.TEntry')
usernameEntry.grid(row=1, column=1, sticky=W)

passwordLabel = ttk.Label(login, text="   Password: ", style='primary.TLabel')
passwordLabel.grid(row=2, column=0, ipadx= 5, ipady=20, sticky=E)

password = StringVar()
passwordEntry = ttk.Entry(login, textvariable=password, style='info.TEntry')
passwordEntry.grid(row=2, column=1, sticky=W)

# #hide pass checkbox
# self.var1 = IntVar()
# self.btn_hide = ttk.Checkbutton(self.login, text="Hide Password", onvalue=1, variable=self.var1, command=self.hidepass, style='info.TCheckbutton')
# self.btn_hide.grid(row=3, column=1, sticky=W)

# login button
def temp():
    username= "n"
    root.withdraw()
    import homePage as homepage
    homepage = homepage.home(root, username)

def checkLogin():
    txt_username = username.get()
    txt_password = password.get()
    print(txt_username)
    print(txt_password)

    sql = "SELECT count(*) FROM tbl_user_profile  where username = '" + txt_username + "' and password = '" + txt_password + "'"
        #count(*)= check through all rows
    conn = db_conn.mysqlconnect()
    cur = conn.cursor()
    cur.execute(sql) # execute sql query

    result = cur.fetchone()
        #fetchone = makes into table (only one row, but if multiple rows=fetchall)
    if result[0] == 1:
        root.withdraw()
        import homePage as homepage
        homepage = homepage.home(root, txt_username)

        #nameoffile.nameofclass

    else:
        #messagebox.showinfo("wrong password/username")
        messagebox.showinfo("result", "wrong password or username")

        #fetchone = makes into table (only one row, but if multiple rows=fetchall)

btn_login = ttk.Button(login, text="Login", width=10, command = checkLogin, style='my.TButton').grid(row=4, column=0,columnspan=2,sticky=S)

#signup
# textbox labels and labels
firstnameLabel = ttk.Label(signup, text="Firstname: ", ).grid(row=0, column=0)
firstname = StringVar()
firstnameEntry = ttk.Entry(signup, textvariable=firstname)
firstnameEntry.grid(row=0, column=1)

lastnameLabel = ttk.Label(signup, text="Lastname: ", ).grid(row=1, column=0)
lastname = StringVar()
lastnameEntry = ttk.Entry(signup, textvariable=lastname)
lastnameEntry.grid(row=1, column=1)

emailLabel = ttk.Label(signup, text="Email: ", ).grid(row=2, column=0)
email = StringVar()
emailEntry = ttk.Entry(signup, textvariable=email)
emailEntry.grid(row=2, column=1)

usernameLabel = ttk.Label(signup, text="Username: ", ).grid(row=3, column=0)
username = StringVar()
usernameEntry = ttk.Entry(signup, textvariable=username)
usernameEntry.grid(row=3, column=1)

passwordLabel = ttk.Label(signup, text="Password: ", ).grid(row=4, column=0)
password = StringVar()
passwordEntry = ttk.Entry(signup, textvariable=password)
passwordEntry.grid(row=4, column=1)

# signup button
def insertNewuser():
    txt_username = username.get()
    txt_password = password.get()
    txt_firstname = firstname.get()
    txt_lastname = lastname.get()
    txt_email = email.get()

    conn = db_conn.mysqlconnect()
    cur = conn.cursor()

    sql = "INSERT INTO tbl_user_profile (firstname, lastname, email, username, password) VALUES (%s, %s, %s, %s, %s)"
    val = (txt_firstname, txt_lastname, txt_email, txt_username, txt_password)
    cur.execute(sql, val)

    conn.commit()
    print(cur.rowcount, "record inserted.")
    messagebox.showinfo("result", "User created")

btn_signup = ttk.Button(signup, text="Signup", width=10, command=insertNewuser)
btn_signup.grid(row=5, column=1)

root.mainloop()

#work VERTICAL--------------------------
# self.mycanvas = Canvas(self.all, height=390, width=335)
# self.mycanvas.grid(row=0, column=0)
# self.yscrollbar = ttk.Scrollbar(self.all, orient='vertical', command=self.mycanvas.yview)
# self.yscrollbar.grid(row=0, column=1, sticky=NS)
# self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)
# self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))
#
# self.itemsframe = Frame(self.mycanvas)
# self.mycanvas.create_window((0, 0), window=self.itemsframe, anchor='nw')
#
# self.item = ttk.Frame(self.itemsframe, height=500, width=100, style="info.TFrame")
# self.item.grid(row=0, column=0, sticky=N)

#work HORIZONTAL----------------------------
# self.mycanvas = Canvas(self.all, height=370, width=354)
# self.mycanvas.grid(row=0, column=0)
# self.xscrollbar = ttk.Scrollbar(self.all, orient='horizontal', command=self.mycanvas.xview)
# self.xscrollbar.grid(row=100, column=0, sticky=EW)
# self.mycanvas.configure(yscrollcommand=self.xscrollbar.set)
# self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))
#
# self.itemsframe = Frame(self.mycanvas)
# self.mycanvas.create_window((0, 0), window=self.itemsframe, anchor='nw')
#
# self.item = ttk.Frame(self.itemsframe, height=500, width=100, style="info.TFrame")
# self.item.grid(row=0, column=0, sticky=N)
mainloop()




#
# class goto:
#     def gotofavs(self):
#         username = "n"
#         self.root.withdraw()
#         import favsPage as favspage
#         favspage = favspage.home(self.root, username)
#
#     def gotohome(self):
#         username = "n"
#         self.root.withdraw()
#         import homePage as homepage
#         homepage = homepage.home(self.root, username)
#
#     def gotocontract(self):
#         username = "n"
#         self.root.withdraw()
#         import contractPage as contractpage
#         contractpage = contractpage.contract(self.root, username)
#
#     def gotomarket(self):
#         username = "n"
#         # dont forget to user later for ALLL!!!!!!
#         self.root.withdraw()
#         import marketPage as marketpage
#         marketpage = marketpage.market(self.root, username)
#
#     def gotoprofile(self):
#         username = "n"
#         self.root.withdraw()
#         import profilePage as profilepage
#         profilepage = profilepage.profile(self.root, username)