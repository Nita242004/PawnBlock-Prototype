from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home
from overlay import Window

class profile:
    def __init__(self, root1, user):
        self.username = user

        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Marketplace")
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

        self.title = ttk.Label(self.root, text="My Profile", font=('Helvetica', 18))
        self.title.grid(row=0, column=1, columnspan=2, sticky=W)

        # self.yscroll = ttk.Scrollbar(self.root, orient='horizontal')
        # self.yscroll.grid(row=0, column=1, rowspan=5)

    #all imported info bout profile
        self.profileinfo=[]
        self.profileinfo = self.profileInformation()
        self.usern = self.profileinfo[0][0]
        self.firstn = self.profileinfo[0][1]
        self.lastn = self.profileinfo[0][2]
        self.email = self.profileinfo[0][3]
        self.addr = self.profileinfo[0][4]

#name box thing
        self.nameFrame = Frame(self.root, height=140, width=354, padx=30, background="white")
        self.nameFrame.grid(row=1, column=0, columnspan=3, sticky=NSEW)
        self.nameFrame.grid_propagate(False)

        self.load = Image.open("/Users/22NitaC/PycharmProjects/pawnshop/Images/profile.png")
        self.resized_image = self.load.resize((80, 80), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resized_image)
        self.imgpfp = Label(self.nameFrame, image=self.render)
        self.imgpfp.image = self.render
        self.imgpfp.grid(row=0, column=0, rowspan=3, ipadx=20, ipady=20, padx=20, sticky=NW)

        self.name = ttk.Label(self.nameFrame, text=self.firstn+" "+self.lastn, font=('Helvetica', 18))
        self.name.grid(row=0, column=1, sticky=SW)
        self.usernametitle = ttk.Label(self.nameFrame, text="User: "+self.usern, font=('Helvetica', 13))
        self.usernametitle.grid(row=1, column=1, sticky=W)
        self.emailtitle = ttk.Label(self.nameFrame, text="Email: "+ self.email, font=('Helvetica', 13))
        self.emailtitle.grid(row=2, column=1, sticky=NW)
#Address
        self.titleofaddy = ttk.Label(self.root, text="Addresses:", font=('Helvetica', 18))
        self.titleofaddy.grid(row=2, column=0, columnspan=3, padx=30, sticky=SW)
        self.addyFrame = Frame(self.root, height=200, width=354, background="white")
        self.addyFrame.grid(row=3, column=0, columnspan=3, padx=30, sticky=NSEW)
        self.addyFrame.grid_propagate(False)

        self.treev = ttk.Treeview(self.addyFrame, selectmode='browse', height=5)
        self.treev.grid(row=0, column=0, pady=10, columnspan=2, sticky=NSEW)
        ##scrollbar
        self.verscrlbar = ttk.Scrollbar(self.root, orient="vertical", command=self.treev.yview)
        self.treev["columns"] = ("1", "2")
        self.treev['show'] = 'headings'
        self.treev.column("1", width=60, anchor='c')
        self.treev.heading("1", text="Location")
        self.treev.column("2", width=280, anchor='c')
        self.treev.heading("2", text="Address")

        addressinfo = self.addressinfo()
        counter = 1
        for i in range(len(addressinfo)):
            self.treev.insert("", index=i, text=addressinfo[i],
                              values=(counter, addressinfo[i]))
            counter = counter + 1

        self.treev.bind('<ButtonRelease-1>', self.item_selected)

        self.location = StringVar()
        self.locationEntry = ttk.Entry(self.addyFrame, textvariable=self.location, style='info.TEntry')
        self.locationEntry.grid(row=6, column=0, sticky=W)

        self.address = StringVar()
        self.addressEntry = ttk.Entry(self.addyFrame, textvariable=self.address, style='info.TEntry')
        self.addressEntry.grid(row=6, column=1, sticky=W)

        self.btn_add = ttk.Button(self.addyFrame, text="Add", width=5, command=self.insertNewaddress, style="primary.TButton")
        self.btn_add.grid(row=6, column=1, sticky=E)


#payment
        self.titleofpay = ttk.Label(self.root, text="Payment:", font=('Helvetica', 18))
        self.titleofpay.grid(row=4, column=0, columnspan=3, padx=30, pady=30, sticky=SW)
        self.payFrame = Frame(self.root, height=140, width=354, background="white")
        self.payFrame.grid(row=5, column=0, columnspan=3, padx=30, sticky=NSEW)
        self.payFrame.grid_propagate(False)

        self.option1 = ttk.Radiobutton(self.payFrame, text="Cash on Delivery", style="payment.TRadiobutton")
        self.option1.grid(row=0, column=0, sticky=W, padx=30)
        self.option2 = ttk.Radiobutton(self.payFrame, text="Credit Card", style="payment.TRadiobutton")
        self.option2.grid(row=1, column=0, sticky=W, padx=30)
        self.option2 = ttk.Radiobutton(self.payFrame, text="Paypal", style="payment.TRadiobutton")
        self.option2.grid(row=2, column=0, sticky=W, padx=30)

        self.root.mainloop()

    def profileInformation(self):
        self.sql = "SELECT username, firstname, lastname, email, address FROM tbl_user_profile WHERE username = '" + self.username+"'"
        print(self.sql)
        # count(*)= check through all rows
        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()
        self.cur.execute(self.sql)  # execute sql query
        self.result = self.cur.fetchall()

        self.record = []
        for row in self.result:
            self.record.append(row)
        print(self.record)
        return self.record

    def addressinfo(self):
        sql = "SELECT location, address FROM tbl_address WHERE username='" + self.username + "'"
        # count(*)= check through all rows
        conn = db_conn.mysqlconnect()
        cur = conn.cursor()
        cur.execute(sql)  # execute sql query
        result = cur.fetchall()

        record = []
        for row in result:
            record.append(row)
        return record

    def item_selected(self, event):
        self.symbol=self.treev.selection()[0]
        self.item = self.treev.item(self.symbol)['text']
        print(self.item)

    def insertNewaddress(self):
        self.txt_location = self.location.get()
        self.txt_address = self.address.get()

        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()

        self.sql = "INSERT INTO tbl_address (location, address) VALUES (%s, %s)"
        self.val = (self.txt_location, self.txt_address)
        self.cur.execute(self.sql, self.val)

        self.conn.commit()
        print(self.cur.rowcount, "record inserted.")
        messagebox.showinfo("result", "Address Added")



    def gotohome(self):
        username = self.username
        self.root.withdraw()
        import homePage as homepage
        homepage = homepage.home(self.root, username)

    def gotoorders(self):
        username = self.username
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