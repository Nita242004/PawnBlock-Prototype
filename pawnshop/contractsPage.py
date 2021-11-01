from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home
from overlay import Window

class contracts:
    def __init__(self, root1, user):
        self.username = user

        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Contracts")
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
        self.mb.grid(row=0, column=0, sticky=W)

        self.load = Image.open("Images/pawnblock_ss.png")
        self.resized_image = self.load.resize((29, 53), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resized_image)
        self.img = Label(self.root, image=self.render)
        self.img.image = self.render
        self.img.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=30, sticky=S)

        self.photofav = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/fav-but.png")
        self.photoimagefav = self.photofav.subsample(6, 6)
        self.fav_btn = ttk.Button(self.root, text='', image=self.photoimagefav, style="transparent.TButton", command=lambda: home.gotofavs(self.root))
        self.fav_btn.grid(row=0, column=1, padx=30, sticky=E)

        #textbox labels and labels
        self.mainTitle = ttk.Label(self.root, text = "Your\nContracts", style='mainTitle.TLabel', font=('Helvetica', 35))
        self.mainTitle.grid(row=1, column=0, columnspan=2, padx=30, sticky=NW)

        # creating scroll frame
        self.mycanvas = Canvas(self.root, height=390, width=335)
        self.mycanvas.grid(row=2, column=0)
        self.yscrollbar = ttk.Scrollbar(self.root, orient='vertical', command=self.mycanvas.yview)
        self.yscrollbar.grid(row=2, column=1, sticky=NS)
        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))

        self.itemsframe = Frame(self.mycanvas)
        self.mycanvas.create_window((0, 0), window=self.itemsframe, anchor='nw')
        # all items
        self.allcontractsList = []
        self.allcontractsList = self.contractInfo("tbl_contracts")
        print(self.allcontractsList)

        counter = 0
        for i in range(0, len(self.allcontractsList)):
            print(i)
            if (i % 2) == 0:
                self.item = ttk.Frame(self.itemsframe, height=165, width=157, style="info.TFrame")
                self.item.grid(row=counter, column=0)
                self.item.grid_propagate(False)
                self.items_btn = ttk.Button(self.item, text=self.allcontractsList[i][0], style="item.TButton",
                                            command=lambda k=i: self.gotospecifcitem("tbl_contracts", k))
                self.items_btn.grid(row=0, column=0)
                self.title = ttk.Label(self.item, text=self.allcontractsList[i][1])
                self.title.grid(row=1, column=0)
            else:
                self.item = ttk.Frame(self.itemsframe, height=165, width=157, style="info.TFrame")
                self.item.grid(row=counter, column=1)
                self.item.grid_propagate(False)
                self.items_btn = ttk.Button(self.item, text=self.allcontractsList[i][0], style="item.TButton",
                                            command=lambda k=i: self.gotospecifcitem("tbl_contracts", k))
                self.items_btn.grid(row=0, column=0)
                self.title = ttk.Label(self.item, text=self.allcontractsList[i][1])
                self.title.grid(row=1, column=0)
                counter = counter + 1

        # bottom
        # bottom row buttons
        self.frame2 = ttk.Frame(self.root, height=40, width=354)
        self.frame2['padding'] = (0, 10, 0, 10)
        self.frame2.grid(row=4, column=0, columnspan=2, sticky=NSEW)
        # home but
        self.photo1 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/home-but.png")
        self.photoimage1 = self.photo1.subsample(6, 6)
        self.home_btn = ttk.Button(self.frame2, text='', image=self.photoimage1, style="transparent.TButton",
                                   command=self.gotohome)
        self.home_btn.grid(row=0, column=0, padx=30)
        # contract but
        self.photo2 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/contract-but.png")
        self.photoimage2 = self.photo2.subsample(5, 5)
        self.contract_btn = ttk.Button(self.frame2, text='', image=self.photoimage2,
                                       style="transparent.TButton")
        self.contract_btn.grid(row=0, column=1, padx=20)
        # marketbut
        self.photo3 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/market-but.png")
        self.photoimage3 = self.photo3.subsample(5, 5)
        self.market_btn = ttk.Button(self.frame2, text='', image=self.photoimage3, style="transparent.TButton",
                                     command=self.gotomarket)
        self.market_btn.grid(row=0, column=2, padx=20)
        # profile but
        self.photo4 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/profile-but.png")
        self.photoimage4 = self.photo4.subsample(5, 5)
        self.profile_btn = ttk.Button(self.frame2, text='', image=self.photoimage4, style="transparent.TButton",
                                      command=self.gotoprofile)
        self.profile_btn.grid(row=0, column=3, padx=30)

        self.root.mainloop()

    def gotofavs(self):
        username = self.username
        self.root.withdraw()
        import favsPage as favspage
        favspage = favspage.home(self.root, username)

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

    def gotopolicies(self):
        username = self.username
        self.root.withdraw()
        import policiesPage as policiespage
        policiespage = policiespage.policies(self.root, username)

    def contractInfo(self, database):
        self.sql = "SELECT contract, owe FROM " + database
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

    def gotospecifcitem(self, contract, code):
        self.contract = contract
        self.code = code
        print(self.contract)

        import contractpayPage as contractpayPage
        contractpayPage = contractpayPage.contractpay(self.root, self.username, self.contract, self.code)


