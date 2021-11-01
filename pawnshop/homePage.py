from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from tkinter.ttk import *

class home:
    def __init__(self, root1, user):
        self.username = user

        self.style = Toplevel(root1)
        self.root = self.style
        self.root.title("Homepage")
        self.root.geometry("414x896")

        #menu
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

        self.photo = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/fav-but.png")
        self.photoimage = self.photo.subsample(6, 6)
        self.fav_btn = ttk.Button(self.root, text='', image=self.photoimage, style="transparent.TButton", command = self.gotofavs)
        self.fav_btn.grid(row=0, column=1, padx=30, sticky=E)

        #textbox labels and labels
        self.mainTitle = ttk.Label(self.root, text = "Available\nPawnshops", style='mainTitle.TLabel', font=('Helvetica', 35))
        self.mainTitle.grid(row=1, column=0, columnspan=2, padx=30, sticky=NW)

# --------
        # # search bar + button
        # self.entry_search = ttk.Entry(self.root, style='info.TEntry', width=56, font=("Helvetica", 18, 'bold'))
        # self.entry_search.grid(row=2, column=0, columnspan=, sticky=W)
        #
        # self.btn_search = ttk.Button(self.root, text='search', style='info.TButton', command=lambda: self.search(self.entry_search.get()))
        # self.btn_search.grid(row=2, column=1, padx=10, sticky=W, ipadx=20)
# ---------

#pawnshops frame scroll
        self.frame1 = ttk.Frame(self.root, height=428, width=414)
        self.frame1['padding'] = (0, 10, 0, 10)
        self.frame1.grid(row=3, column=0, columnspan=2, sticky=NSEW)

        self.mycanvas = Canvas(self.frame1, height=390, width=414)
        self.mycanvas.grid(row=0, column=0)
        self.yscrollbar = ttk.Scrollbar(self.frame1, orient='horizontal', command=self.mycanvas.xview)
        self.yscrollbar.grid(row=1, column=0, sticky=EW)
        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))

        self.shopsframe = Frame(self.mycanvas)
        self.mycanvas.create_window((0, 0), window=self.shopsframe, anchor='nw')

        self.pawnshopsList = []
        self.pawnshopsList = self.itemInfo("tbl_pawnshops")
        print(self.pawnshopsList)

        self.pawnphotopath = ["/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn1.png", "/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn2.png",
                              "/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn3.png", "/Users/22NitaC/PycharmProjects/pawnshop/Images/pawn4.png"]
        self.pawnshopphotos = []
        for i in range(len(self.pawnshopsList)):
            self.pawnshopphotos.append(PhotoImage(file=self.pawnphotopath[i]).subsample(7, 7))

        for i in range(0, len(self.pawnshopsList)):
            self.shopFrame = ttk.Frame(self.shopsframe, height=330, width=250, style="info.TFrame")
            self.shopFrame.grid(row=0, column=i, pady=40, padx=30)
            self.shopFrame.grid_propagate(False)
            self.shop_btn = ttk.Button(self.shopFrame, text="tbl_pawnshops", image=self.pawnshopphotos[i],
                                         style="item.TButton",command=lambda k=i: self.gotospecifcshop("tbl_pawnshops", k))
            self.shop_btn.grid(row=0, column=0, padx=5, sticky=EW)
            self.shoptitle = ttk.Label(self.shopFrame, text=self.pawnshopsList[i][0], font=('Helvetica', 20))
            self.shoptitle.grid(row=1, column=0, padx=5, sticky=EW)


        #bottom row buttons
        self.frame2 = ttk.Frame(self.root, height=40, width=354)
        self.frame2['padding'] = (0, 30, 0, 30)
        self.frame2.grid(row=4, column=0, columnspan=2, sticky=NSEW)

            #home but
        self.photo1 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/home-but.png")
        self.photoimage1 = self.photo1.subsample(6, 6)
        self.home_btn = ttk.Button(self.frame2, text='', image=self.photoimage1, style="transparent.TButton")
        self.home_btn.grid(row=0, column=0, padx=30, pady=30)
            #contract but
        self.photo2 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/contract-but.png")
        self.photoimage2 = self.photo2.subsample(5, 5)
        self.contract_btn = ttk.Button(self.frame2, text='', image=self.photoimage2, style="transparent.TButton", command = self.gotocontracts)
        self.contract_btn.grid(row=0, column=1, padx=20, pady=30)
            #marketbut
        self.photo3 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/market-but.png")
        self.photoimage3 = self.photo3.subsample(5,5)
        self.market_btn = ttk.Button(self.frame2, text='', image=self.photoimage3, style = "transparent.TButton", command = self.gotomarket)
        self.market_btn.grid(row=0, column=2, padx=20, pady=30)
            #profile but
        self.photo4 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/profile-but.png")
        self.photoimage4 = self.photo4.subsample(5, 5)
        self.profile_btn = ttk.Button(self.frame2, text='', image=self.photoimage4, style="transparent.TButton", command = self.gotoprofile)
        self.profile_btn.grid(row=0, column=3, padx=30, pady=30)

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
    '''def search(self, search):
         in generalstockscreen2'''

    def gotospecifcshop(self, db, code):
        self.code = code
        self.database = db
        print(self.code)
        print(self.database)

        import specificpawnPage as specificpawnpage
        specificpawnpage = specificpawnpage.specificpawn(self.root, self.username, self.database, self.code)

    def itemInfo(self, database):
        self.sql = "SELECT name FROM " + database
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

    def gotocontracts(self):
        username = self.username
        self.root.withdraw()
        import contractsPage as contractsPage
        contractsPage = contractsPage.contracts(self.root, username)