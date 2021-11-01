from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home as home
from overlay import Window

class specificpawn:
    def __init__(self, root1, user, db, code):
        self.username = user
        self.database = db
        self.code = code
        print(self.code)
        print(self.database)

        self.root = root1
        self.root.title("Specific Pawnshop")
        self.root.geometry("414x896")

#specific item page-----------------------
        self.specificFrame = Frame(self.root, height=896, width=414, background="white")
        self.specificFrame.grid(row=0, column=0)
        self.specificFrame.grid_propagate(False)

        self.pawnList = []
        self.pawnList = self.pawnInfo()
        self.name = self.pawnList[int(self.code)][1]
        self.telephone = self.pawnList[int(self.code)][2]
        self.email = self.pawnList[int(self.code)][3]
        self.address = self.pawnList[int(self.code)][4]

        self.pawnphotopath = ["/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn1.png",
                              "/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn2.png",
                              "/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn3.png",
                              "/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn4.png"]
        self.photoPath = self.pawnphotopath[int(self.code)]
        # print(self.itemList)

        self.photoback = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/back-btn.png")
        self.photoimageback = self.photoback.subsample(6, 6)
        self.photoback_btn = ttk.Button(self.specificFrame, text='', image=self.photoimageback, style="transparent.TButton", command=lambda: self.invisible(self.specificFrame))
        self.photoback_btn.grid(row=0, column=0, padx=25, pady=30, sticky=W)

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

        self.space = ttk.Label(self.textFrame, text=" ").grid(row=3, column=0, padx=5, sticky=W)

        self.itemaddy = ttk.Label(self.textFrame, text="Address:", font=('Helvetica', 22))
        self.itemaddy.grid(row=4, column=0, padx=5, sticky=W)
        self.itemaddyno = ttk.Label(self.textFrame, text=self.address, font=('Helvetica', 15), wraplength=350)
        self.itemaddyno.grid(row=5, column=0, columnspan=2, sticky=NW)

        self.space = ttk.Label(self.textFrame, text=" ").grid(row=6, column=0, padx=5, sticky=W)

        self.itemShop = ttk.Label(self.textFrame, text="Contacts:", font=('Helvetica', 22))
        self.itemShop.grid(row=7, column=0, padx=5, sticky=W)
        self.itemShopno = ttk.Label(self.textFrame, text=self.telephone, font=('Helvetica', 15))
        self.itemShopno.grid(row=8, column=0, columnspan=2, padx=5, sticky=NW)
        self.itemShopno = ttk.Label(self.textFrame, text=self.email, font=('Helvetica', 15))
        self.itemShopno.grid(row=9, column=0, columnspan=2, padx=5, sticky=NW)

        self.space= ttk.Label(self.textFrame, text = " ").grid(row=10, column=0, padx=5, sticky=W)

        self.itemShop = ttk.Label(self.textFrame, text="Description:", font=('Helvetica', 22))
        self.itemShop.grid(row=11, column=0, padx=5, sticky=W)
        self.desFrame = Frame(self.textFrame, height=120, width=354, relief='sunken')
        self.desFrame.grid(row=12, column=0, padx=5, sticky=NSEW)

        self.root.mainloop()

    def pawnInfo(self):
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

    def gotohome(self):
        username = self.username
        self.root.withdraw()
        import homePage as homepage
        homepage = homepage.home(self.root, username)