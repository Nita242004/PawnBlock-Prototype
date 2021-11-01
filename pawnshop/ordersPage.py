from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home
from overlay import Window

class orders:
    def __init__(self, root1, user):
        self.username = user

        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Cart")
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
        self.mb.grid(row=0, column=0, padx=5, pady=20, sticky=SW)

        self.title = ttk.Label(self.root, text="       Cart", font=('Helvetica', 18))
        self.title.grid(row=0, column=1, columnspan=3, sticky=SW)

    #orders
        # self.btn_delete = ttk.Button(self.root, text='Delete', style='info.TButton', command=self.deleteItem())
        # self.btn_delete.grid(row=1, column=2, padx=10, sticky=W, ipadx=10)

        self.treev1 = ttk.Treeview(self.root, selectmode='browse', height=25)
        self.treev1.grid(row=2, column=0, padx=30, pady=10, columnspan=4, sticky=NSEW)
        ##scrollbar
        self.verscrlbar = ttk.Scrollbar(self.root, orient="vertical", command=self.treev1.yview)
        self.treev1["columns"] = ("1", "2")
        self.treev1['show'] = 'headings'
        self.treev1.column("1", width=270, anchor='c')
        self.treev1.heading("1", text="Item")
        self.treev1.column("2", width=84, anchor='c')
        self.treev1.heading("2", text="Price (THB)")

        self.cartinfo1 = self.cartinfo()
        counter = 1
        for i in range(len(self.cartinfo1)):
            self.treev1.insert("", index=i, text=self.cartinfo1[i][0],
                              values=(self.cartinfo1[i][0], self.cartinfo1[i][1]))
            counter = counter + 1

        # self.treev1.bind('<ButtonRelease-1>', self.item_selected)

        self.btn_deleteall = ttk.Button(self.root, text='Delete All', style='info.TButton', command=self.deleteall)
        self.btn_deleteall.grid(row=3, column=1, columnspan=4, sticky=E, padx=30)

        self.checkout_btn = ttk.Button(self.root, text="Checkout", style="bottomMain.TButton", command=self.gotopayment1)
        self.checkout_btn.grid(row=4, column=0, columnspan=4, pady=50, ipadx=100, padx=25, sticky=EW)
        self.root.mainloop()

    def cartinfo(self):
        sql = "SELECT item, price FROM tbl_cart WHERE username='" + self.username + "'"
        # count(*)= check through all rows
        conn = db_conn.mysqlconnect()
        cur = conn.cursor()
        cur.execute(sql)  # execute sql query
        result = cur.fetchall()

        record = []
        for row in result:
            record.append(row)
        return record

    # def item_selected(self, event):
    #     self.value = self.treev1.focus()
    #     print(self.tree1.item(self.value))
    #     # self.symbol = self.treev1.selection()[0]
    #     # self.item1 = self.treev1.item(self.symbol)['text']
    #     # print(self.item1)
    #
    # def deleteItem(self):
    #     sql = "DELETE from tbl_cart WHERE username='" + self.username + "' and item = '" + self.item1 + "'"
    #
    #     conn = db_conn.mysqlconnect()
    #     cur = conn.cursor()
    #     cur.execute(sql)  # execute sql query
    #     conn.commit()
    #
    #     messagebox.showinfo("result", "Item Deleted")
    def gotopayment1(self):
        username = self.username
        import payment1Page as paymentpage1
        paymentpage1 = paymentpage1.payment1(self.root, username, self.cartinfo1)

    def deleteall(self):
        sql = "DELETE from tbl_cart WHERE username='" + self.username + "'"

        conn = db_conn.mysqlconnect()
        cur = conn.cursor()
        cur.execute(sql)  # execute sql query
        conn.commit()

        messagebox.showinfo("result", "All Items Deleted")

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

