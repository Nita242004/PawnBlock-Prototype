from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home as home
from overlay import Window

class specificitem:
    def __init__(self, root1, user, db, code):
        self.username = user
        self.database = db
        self.code = code
        print(self.code)
        print(self.database)

        self.root = root1
        self.root.title("Specific Item")
        self.root.geometry("414x896")

#specific item page-----------------------
        self.specificFrame = Frame(self.root, height=896, width=414, background="white")
        self.specificFrame.grid(row=0, column=0)
        self.specificFrame.grid_propagate(False)

        self.itemList = []
        self.itemList = self.itemInfo()
        self.name = self.itemList[int(self.code)][1]
        self.photoPath = self.itemList[int(self.code)][2]
        self.price = self.itemList[int(self.code)][3]
        self.shop = self.itemList[int(self.code)][4]
        # print(self.itemList)

        self.photoback = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/back-btn.png")
        self.photoimageback = self.photoback.subsample(6, 6)
        self.photoback_btn = ttk.Button(self.specificFrame, text='', image=self.photoimageback, style="transparent.TButton", command=lambda: self.invisible(self.specificFrame))
        self.photoback_btn.grid(row=0, column=0, padx=30, pady=30, sticky=W)

        self.photofav3 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/fav-btn2.png")
        self.photoimagefav3 = self.photofav3.subsample(6, 6)
        self.fav_btn2 = ttk.Button(self.specificFrame, text='', image=self.photoimagefav3, style="transparent.TButton", command=lambda: self.addtofav())
        self.fav_btn2.grid(row=0, column=0, padx=40, sticky=E)

        self.load = Image.open(self.photoPath)
        self.resized_image = self.load.resize((320, 320), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resized_image)
        self.imgitem = Label(self.specificFrame, image=self.render)
        self.imgitem.image = self.render
        self.imgitem.grid(row=1, column=0, ipadx=20, padx=30, ipady=10, sticky=N)

        self.textFrame = Frame(self.specificFrame, height=410, width=354, padx=30, background="white")
        self.textFrame.grid(row=2, column=0, sticky=NSEW)
        self.textFrame.grid_propagate(False)

        self.itemTitle = ttk.Label(self.textFrame, text=self.name, font=('Helvetica', 28))
        self.itemTitle.grid(row=2, column=0, columnspan=2, sticky=EW)

        self.itemPrice = ttk.Label(self.textFrame, text="Price:", font=('Helvetica', 22))
        self.itemPrice.grid(row=3, column=0, ipady=10, padx=5, sticky=W)
        self.itemPriceno = ttk.Label(self.textFrame, text=self.price, font=('Helvetica', 20))
        self.itemPriceno.grid(row=3, column=1, columnspan=2, ipady=10, sticky=W)

        self.itemShop = ttk.Label(self.textFrame, text="Pawnshop:", font=('Helvetica', 22))
        self.itemShop.grid(row=4, column=0, ipady=20, padx=5, sticky=W)
        self.itemShopno = ttk.Label(self.textFrame, text=self.shop, font=('Helvetica', 20))
        self.itemShopno.grid(row=5, column=0, columnspan=2, padx=5, sticky=NW)

        self.addtocart_btn = ttk.Button(self.textFrame, text="Add to Cart", style="bottomMain.TButton", command = self.addcart)
        self.addtocart_btn.grid(row=6, column=0, columnspan=2, pady=50, ipadx=100, padx=25, sticky=EW)

        self.root.mainloop()

    def itemInfo(self):
        self.sql = "SELECT * FROM " + self.database
        # count(*)= check through all rows
        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()
        self.cur.execute(self.sql)  # execute sql query
        self.result = self.cur.fetchall()

        record = []
        for row in self.result:
            record.append(row)
        return record

    def invisible(self, widget):
        widget.grid_forget()

    def visible(self, widget):
        widget.grid(row=0, column=0)

    def addtofav(self):
        self.conn = db_conn.mysqlconnect()
        self.cur = self.conn.cursor()

        self.sqlcheck = "Select * from tbl_favorites where username = '" + self.username + "' and name = '" + self.name + "'"
        self.cur.execute(self.sqlcheck)  # execute sql query
        self.result = self.cur.fetchone()

        if self.result is not None:
            messagebox.showinfo("result", "Item Already Favorited")

        else:
            self.sql = "INSERT INTO tbl_favorites (username, name) VALUES (%s, %s)"
            self.val = (self.username, self.name)
            print(self.sql)
            self.cur.execute(self.sql, self.val)

            self.conn.commit()
            messagebox.showinfo("result", "Item Favorited")

    def gotomarket(self):
        username = self.username
        self.root.withdraw()
        import marketPage as marketpage
        marketpage = marketpage.market(self.root, username)

    def addcart(self):
        conn = db_conn.mysqlconnect()
        cur = conn.cursor()
        self.priceNoText = str(self.price).replace(" THB","").strip()
        self.priceNumber = int(self.priceNoText)

        sqlcheck = "Select * from tbl_cart where username = '" + self.username + "' and item = '" + self.name + "'"
        cur.execute(sqlcheck)  # execute sql query
        result = cur.fetchone()

        if result is not None:
            messagebox.showinfo("result", "Item Already Added")

        else:
            sql = "INSERT INTO tbl_cart (username, item, price) VALUES (%s, %s, %s)"
            val = (self.username, self.name, self.priceNumber)
            print(sql)
            cur.execute(sql, val)

            conn.commit()
            messagebox.showinfo("result", "Item Added")

        self.specificFrame.grid_forget()