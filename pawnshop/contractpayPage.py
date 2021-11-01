from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home as home
from overlay import Window

class contractpay:
    def __init__(self, root1, user, contract):
        self.username = user
        self.contractname = contract
        self.code=code
        print(self.contractname)

        self.root = root1
        self.root.title("Checkout")
        self.root.geometry("414x896")

#specific item page-----------------------
        self.specificFrame2 = Frame(self.root, height=896, width=414, background="white")
        self.specificFrame2.grid(row=0, column=0)
        self.specificFrame2.grid_propagate(False)

        self.photoback2 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/back-btn.png")
        self.photoimageback2 = self.photoback2.subsample(6, 6)
        self.photoback_btn2 = ttk.Button(self.specificFrame2, text='', image=self.photoimageback2, style="transparent.TButton", command=lambda: self.invisible(self.specificFrame2))
        self.photoback_btn2.grid(row=0, column=0, padx=30, pady=30, sticky=W)

        # self.titlemain2 = ttk.Label(self.specificFrame2, text="             Checkout", font=('Helvetica', 18))
        # self.titlemain2.grid(row=0, column=0,columnspan=2, sticky=E)

        self.itemTitle2 = ttk.Label(self.specificFrame2, text="Payment", font=('Helvetica', 28))
        self.itemTitle2.grid(row=1, column=0, columnspan=3, padx=30, sticky=W)

        self.contractinfo = self.contractInfo()
        self.titleofpay1 = ttk.Label(self.specificFrame2, text="Contract Information:", font=('Helvetica', 18))
        self.titleofpay1.grid(row=3, column=0, columnspan=3, padx=30, pady=30, sticky=SW)
        self.payFrame1 = Frame(self.root, height=140, width=354, background="white")
        self.payFrame1.grid(row=2, column=0, columnspan=3, padx=30, sticky=NSEW)
        self.payFrame1.grid_propagate(False)
        self.title1 = ttk.Label(self.payFrame1, text="Contract: "+self.contractinfo[0])
        self.title1.grid(row=0, column=0)
        self.title22 = ttk.Label(self.payFrame1, text="How much is Owed: " + self.contractinfo[1])
        self.title22.grid(row=0, column=0)
        self.title3 = ttk.Label(self.payFrame1, text="Item Pawned: " + self.contractinfo[2])
        self.title3.grid(row=0, column=0)


        self.titleofpay2 = ttk.Label(self.specificFrame2, text="Payment:", font=('Helvetica', 18))
        self.titleofpay2.grid(row=3, column=0, columnspan=3, padx=30, pady=30, sticky=SW)
        self.payFrame2 = Frame(self.root, height=140, width=354, background="white")
        self.payFrame2.grid(row=4, column=0, columnspan=3, padx=30, sticky=NSEW)
        self.payFrame2.grid_propagate(False)

        self.option11 = ttk.Radiobutton(self.payFrame2, text="Cash on Delivery", style="payment.TRadiobutton")
        self.option11.grid(row=0, column=0, sticky=W, padx=30)
        self.option22 = ttk.Radiobutton(self.payFrame2, text="Credit Card", style="payment.TRadiobutton")
        self.option22.grid(row=1, column=0, sticky=W, padx=30)
        self.option32 = ttk.Radiobutton(self.payFrame2, text="Paypal", style="payment.TRadiobutton")
        self.option32.grid(row=2, column=0, sticky=W, padx=30)

        self.totaltitle2 = ttk.Label(self.specificFrame2, text="Total:", font=('Helvetica', 17))
        self.totaltitle2.grid(row=6, column=0, columnspan=3, padx=30, sticky=W)
        self.totaltitleno2 = ttk.Label(self.specificFrame2, text=str(self.contractinfo[1]) + "THB", font=('Helvetica', 17))
        self.totaltitleno2.grid(row=6, column=0, columnspan=3, padx=30, sticky=E)

        self.checkout_btn2 = ttk.Button(self.specificFrame2, text="         Checkout         ", style="bottomMain.TButton", command=self.gotohome)
        self.checkout_btn2.grid(row=7, column=0, columnspan=3, pady=50, padx=30, sticky=EW)

        self.root.mainloop()

    def contractInfo(self):
        self.sql = "SELECT contract, owe, pawneditem FROM tbl_contracts WHERE contract = '" +self.contractname+"' and username = '"+self.username+"'"
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

    def invisible(self, widget):
        widget.grid_forget()

    def gotohome(self):
        messagebox.showinfo("result", "Payment Complete")
        username = self.username
        self.root.withdraw()
        import homePage as homepage
        homepage = homepage.home(self.root, username)