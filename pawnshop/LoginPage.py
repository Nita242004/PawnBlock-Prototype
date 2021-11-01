from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
from tkinter import ttk
import db_conn

class Login:
    def __init__(self, root1):
        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Login Window")
        self.root.geometry("414x896")

        #textbox labels and labels
        self.load = Image.open("Images/pawnblock_ss.png")
        self.resized_image= self.load.resize((87,159), Image.ANTIALIAS)
        self.render= ImageTk.PhotoImage(self.resized_image)
        self.img = Label(self.root, image=self.render)
        self.img.image = self.render
        self.img.grid(row=0, column=0, columnspan=2, ipadx= 5, ipady=20, sticky=S)

        # Tab
        self.tabControl = ttk.Notebook(self.root, width=350, height=520, style='login.TNotebook')
        self.tabControl.grid(row=1, column=0, columnspan=2, padx=30)

        self.login = ttk.Frame(self.root)
        self.signup = ttk.Frame(self.root)

        self.tabControl.add(self.login, text="Login")
        self.tabControl.add(self.signup, text="Signup")

#login
        self.usernameLabel = ttk.Label(self.login, text="   Username: ", style='primary.TLabel')
        self.usernameLabel.grid(row=1, column=0, ipadx= 5, ipady=20, sticky=E)
        self.username = StringVar()
        self.usernameEntry = ttk.Entry(self.login, textvariable=self.username, style='info.TEntry')
        self.usernameEntry.grid(row=1, column=1, sticky=W)

        self.passwordLabel = ttk.Label(self.login, text="   Password: ", style='primary.TLabel')
        self.passwordLabel.grid(row=2, column=0, ipadx= 5, ipady=20, sticky=E)
        self.password = StringVar()
        self.passwordEntry = ttk.Entry(self.login, textvariable=self.password, style='info.TEntry')
        self.passwordEntry.grid(row=2, column=1, sticky=W)

        # #hide pass checkbox
        # self.var1 = IntVar()
        # self.btn_hide = ttk.Checkbutton(self.login, text="Hide Password", onvalue=1, variable=self.var1, command=self.hidepass, style='info.TCheckbutton')
        # self.btn_hide.grid(row=3, column=1, sticky=W)

        # login button
        self.btn_login = ttk.Button(self.login, text="Login", width=10, command = self.temp, style='my.TButton')
        self.btn_login.grid(row=4, column=0,columnspan=2,sticky=S)

#signup
        # textbox labels and labels
        self.firstnameLabel = ttk.Label(self.signup, text="Firstname: ", ).grid(row=0, column=0)
        self.firstname = StringVar()
        self.firstnameEntry = ttk.Entry(self.signup, textvariable=self.firstname)
        self.firstnameEntry.grid(row=0, column=1)

        self.lastnameLabel = ttk.Label(self.signup, text="Lastname: ", ).grid(row=1, column=0)
        self.lastname = StringVar()
        self.lastnameEntry = ttk.Entry(self.signup, textvariable=self.lastname)
        self.lastnameEntry.grid(row=1, column=1)

        self.emailLabel = ttk.Label(self.signup, text="Email: ", ).grid(row=2, column=0)
        self.email = StringVar()
        self.emailEntry = ttk.Entry(self.signup, textvariable=self.email)
        self.emailEntry.grid(row=2, column=1)

        self.usernameLabel = ttk.Label(self.signup, text="Username: ", ).grid(row=3, column=0)
        self.username = StringVar()
        self.usernameEntry = ttk.Entry(self.signup, textvariable=self.username)
        self.usernameEntry.grid(row=3, column=1)

        self.passwordLabel = ttk.Label(self.signup, text="Password: ", ).grid(row=4, column=0)
        self.password = StringVar()
        self.passwordEntry = ttk.Entry(self.signup, textvariable=self.password)
        self.passwordEntry.grid(row=4, column=1)

        # signup button
        self.btn_signup = ttk.Button(self.signup, text="Signup", width=10, command=self.insertNewuser)
        self.btn_signup.grid(row=5, column=1)

        self.root.mainloop()

    # def hidepass(self):
    #     if self.var1.get() == 1:
    #         self.passwordEntry = ttk.Entry(self.root, textvariable=self.password, show="*", style='info.TEntry').grid(row=1, column=1)
    #     else:
    #         self.passwordEntry = ttk.Entry(self.root, textvariable=self.password, style='info.TEntry').grid(row=1, column=1)

    def temp(self):
        username= "n"
        self.root.withdraw()
        import homePage as homepage
        homepage = homepage.home(self.root, username)
            #dont forget to add self.txt_username

    def checkingLogin(self, username, password):
        #command = lambda:self.checkingLogin(self.usernameEntry.get(), self.passwordEntry.get())
        self.txt_username = username
        self.txt_password = password
        print(self.txt_username)
        print(username)
        print(password)

        self.sql = "SELECT count(*) FROM tbl_user_profile  where username = '" + self.txt_username + "' and password = '" + self.txt_password + "'"
        print(self.sql)
            #count(*)= check through all rows
        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()
        self.cur.execute(self.sql) # execute sql query

        self.result = self.cur.fetchone()
            #fetchone = makes into table (only one row, but if multiple rows=fetchall)
        if self.result[0] == 1:
            self.root.withdraw()
            import homePage as homepage
            homepage = homepage.homepage(self.root, self.txt_username)
            #nameoffile.nameofclass
        elif self.result[0] != 1:
            #messagebox.showinfo("wrong password/username")
            messagebox.showinfo("result", "wrong password or username")

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
        messagebox.showinfo("result", "User created")
