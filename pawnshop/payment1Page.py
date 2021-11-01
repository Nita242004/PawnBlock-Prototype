from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home as home
from overlay import Window

class payment1:
    def __init__(self, root1, user, cart):
        self.username = user
        self.cartinfo1 = cart
        print(self.cartinfo1)

        self.root = root1
        self.root.title("Checkout")
        self.root.geometry("414x896")

#specific item page-----------------------
        self.specificFrame = Frame(self.root, height=896, width=414, background="white")
        self.specificFrame.grid(row=0, column=0)
        self.specificFrame.grid_propagate(False)

        self.photoback = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/back-btn.png")
        self.photoimageback = self.photoback.subsample(6, 6)
        self.photoback_btn = ttk.Button(self.specificFrame, text='', image=self.photoimageback, style="transparent.TButton", command=lambda: self.invisible(self.specificFrame))
        self.photoback_btn.grid(row=0, column=0, padx=30, pady=30, sticky=W)

        self.titlemain = ttk.Label(self.specificFrame, text="      Checkout", font=('Helvetica', 18))
        self.titlemain.grid(row=0, column=0,columnspan=2, sticky=E)

        self.itemTitle = ttk.Label(self.specificFrame, text="Payment", font=('Helvetica', 28))
        self.itemTitle.grid(row=1, column=0, columnspan=3, padx=30, sticky=W)

        self.profiledetail = ttk.Label(self.specificFrame, text="Profile Details:", font=('Helvetica', 17))
        self.profiledetail.grid(row=2, column=0,columnspan=3, padx=30, ipady=30, sticky=SW)

        self.textFrame = Frame(self.specificFrame, height=100, width=374, padx=10, background="white")
        self.textFrame.grid(row=3, column=0, columnspan=3,padx=10,sticky=NSEW)
        self.textFrame.grid_propagate(False)

        self.profileinfo = []
        self.profileinfo = self.profileInformation()
        self.usern = self.profileinfo[0][0]
        self.firstn = self.profileinfo[0][1]
        self.lastn = self.profileinfo[0][2]
        self.email = self.profileinfo[0][3]
        self.addr = self.profileinfo[0][4]

        self.name = ttk.Label(self.textFrame, text="Name:", font=('Helvetica', 17))
        self.name.grid(row=1, column=0, pady=10, padx=5, sticky=W)
        self.namelable = ttk.Label(self.textFrame, text=self.firstn+" "+self.lastn, font=('Helvetica', 17))
        self.namelable.grid(row=1, column=1, columnspan=2, ipady=10, sticky=W)

        self.em = ttk.Label(self.textFrame, text="Email:", font=('Helvetica', 17))
        self.em.grid(row=2, column=0, pady=10, padx=5, sticky=W)
        self.emlable = ttk.Label(self.textFrame, text=self.email, font=('Helvetica', 17))
        self.emlable.grid(row=2, column=1, columnspan=2, ipady=10, sticky=W)
# items info
        self.itemtitlemain = ttk.Label(self.specificFrame, text="Items:", font=('Helvetica', 17))
        self.itemtitlemain.grid(row=4, column=0,columnspan=3, padx=30, pady=30, sticky=SW)
        self.itemsframe = Frame(self.specificFrame, height=200, width=354, padx=30, background="white")
        self.itemsframe.grid(row=5, column=0, columnspan=3, padx=10,sticky=NSEW)
        self.itemsframe.grid_propagate(False)

        self.treev1 = ttk.Treeview(self.itemsframe, selectmode='browse', height=5)
        self.treev1.grid(row=0, column=0, pady=10, columnspan=4, sticky=NSEW)
        ##scrollbar
        self.verscrlbar = ttk.Scrollbar(self.root, orient="vertical", command=self.treev1.yview)
        self.treev1["columns"] = ("1", "2")
        self.treev1['show'] = 'headings'
        self.treev1.column("1", width=230, anchor='c')
        self.treev1.heading("1", text="Item")
        self.treev1.column("2", width=84, anchor='c')
        self.treev1.heading("2", text="Price (THB)")

        counter = 1
        for i in range(len(self.cartinfo1)):
            self.treev1.insert("", index=i, text=self.cartinfo1[i][0],
                               values=(self.cartinfo1[i][0], self.cartinfo1[i][1]))
            counter = counter + 1
#addy
        self.titleofaddy = ttk.Label(self.root, text="Addresses:", font=('Helvetica', 18))
        self.titleofaddy.grid(row=5, column=0, columnspan=3, padx=30, sticky=SW)
        self.addyFrame = Frame(self.root, height=200, width=354, background="white")
        self.addyFrame.grid(row=6, column=0, columnspan=3, padx=30, sticky=NSEW)
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

        self.total=0
        for i in range(len(self.cartinfo1)):
            self.total=self.total+self.cartinfo1[i][1]
            print(self.total)

        self.totaltitle=ttk.Label(self.specificFrame, text="Total:", font=('Helvetica', 17))
        self.totaltitle.grid(row=6, column=0, columnspan=3, padx=30, sticky=W)
        self.totaltitleno=ttk.Label(self.specificFrame, text=str(self.total) + "THB", font=('Helvetica', 17))
        self.totaltitleno.grid(row=6, column=0, columnspan=3, padx=30, sticky=E)

        self.checkout_btn = ttk.Button(self.specificFrame, text="         Checkout         ", style="bottomMain.TButton", command=self.gotopayment2)
        self.checkout_btn.grid(row=7, column=0, columnspan=3, pady=50, padx=30, sticky=EW)

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

    def invisible(self, widget):
        widget.grid_forget()

    def visible(self, widget):
        widget.grid(row=0, column=0)

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

    def gotopayment2(self):
        username = self.username
        # self.specificFrame.grid_forget()
        import payment2Page as paymentpage2
        paymentpage2 = paymentpage2.payment2(self.root, username, self.cartinfo1)
