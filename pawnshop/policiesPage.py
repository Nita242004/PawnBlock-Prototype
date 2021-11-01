from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home as home
from overlay import Window

class policies:
    def __init__(self, root1, user):
        self.username = user

        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Privacy Policies")
        self.root.geometry("414x896")

        # menu
        self.mb = ttk.Menubutton(self.root, style='primary.TMenubutton')
        # create menu
        self.menu = tk.Menu(self.mb)
        # add options
        self.option_var = tk.StringVar()
        self.menu.add_radiobutton(label="Homepage", value=0, variable=self.option_var, command=self.gotohome)
        self.menu.add_radiobutton(label="Orders", value=1, variable=self.option_var, command=self.gotoorders)
        self.menu.add_radiobutton(label="Profile", value=2, variable=self.option_var, command=self.gotoprofile)
        self.menu.add_radiobutton(label="Settings", value=3, variable=self.option_var, command=self.gotosettings)
        self.menu.add_radiobutton(label="Policies", value=4, variable=self.option_var, command=self.gotopolicies)

        # associate menu with menubutton
        self.mb['menu'] = self.menu
        self.mb.grid(row=0, column=0, padx=5, pady=40, sticky=W)

        self.title = ttk.Label(self.root, text= "Privacy Policies", font=('Helvetica', 18))
        self.title.grid(row=0, column=1, columnspan=3, sticky=W)
        self.label = ttk.Label(self.root, text = "Unavailable", font=('Helvetica', 28))
        self.label.grid(row=1, column=0, columnspan=4, pady=330, padx=130)

        self.root.mainloop()

    def gotohome(self):
        username = self.username
        self.root.withdraw()
        import homePage as homepage
        homepage = homepage.home(self.root, username)

    def gotoorders(self):
        username = "n"
        self.root.withdraw()
        import ordersPage as orderspage
        orderspage = orderspage.orders(self.root, username)

    def gotopolicies(self):
        username = self.username
        self.root.withdraw()
        import policiesPage as policiespage
        policiespage = policiespage.policies(self.root, username)

    def gotomarket(self):
        username = self.username
        # dont forget to user later for ALLL!!!!!!
        self.root.withdraw()
        import marketPage as marketpage
        marketpage = marketpage.market(self.root, username)

    def gotosettings(self):
        username = self.username
        self.root.withdraw()
        import settingsPage as settingspage
        settingspage = settingspage.settings(self.root, username)

    def gotoprofile(self):
        username = self.username
        self.root.withdraw()
        import profilePage as profilepage
        profilepage = profilepage.profile(self.root, username)

    def itemInfo(self, database):
        self.sql = "SELECT code, name, photo_path FROM " + database
        print(self.sql)
        # count(*)= check through all rows
        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()
        self.cur.execute(self.sql)  # execute sql query
        self.result = self.cur.fetchall()

        self.record = []
        for row in self.result:
            self.record.append(row)
        return self.record
