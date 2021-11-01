from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
import db_conn
from homePage import home
from overlay import Window

class market:
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
        self.mainTitle = ttk.Label(self.root, text = "Unclaimed\nItems", style='mainTitle.TLabel', font=('Helvetica', 35))
        self.mainTitle.grid(row=1, column=0, columnspan=2, padx=30, sticky=NW)

# --------
        ## search bar + button
        # self.entry_search = ttk.Entry(self.root, style='info.TEntry', width=56, font=("Helvetica", 18, 'bold'))
        # self.entry_search.grid(row=2, column=0, columnspan=, sticky=W)
        #
        # self.btn_search = ttk.Button(self.root, text='search', style='info.TButton', command=lambda: self.search(self.entry_search.get()))
        # self.btn_search.grid(row=2, column=1, padx=10, sticky=W, ipadx=20)
# ---------

        # category tabs/buttons
        self.categories = ttk.Notebook(self.root, height=390, width=354, style='login.TNotebook')
        self.categories.grid(row=3, column=0, columnspan=2, padx=30, pady=30)

        self.all = LabelFrame(self.root)
        self.jewlery = LabelFrame(self.root)
        self.gold = LabelFrame(self.root)
        self.electronics = LabelFrame(self.root)
        self.others = LabelFrame(self.root)

        self.categories.add(self.all, text="All")
        self.categories.add(self.jewlery, text="Jewelry")
        self.categories.add(self.gold, text="Gold")
        self.categories.add(self.electronics, text="Electronics")
        self.categories.add(self.others, text="Others")

#ALL TAB
    #creating scroll frame
        self.mycanvas = Canvas(self.all, height=390, width=335)
        self.mycanvas.grid(row=0, column=0)
        self.yscrollbar = ttk.Scrollbar(self.all, orient='vertical', command=self.mycanvas.yview)
        self.yscrollbar.grid(row=0, column=1, sticky=NS)
        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion=self.mycanvas.bbox('all')))

        self.itemsframe = Frame(self.mycanvas)
        self.mycanvas.create_window((0, 0), window=self.itemsframe, anchor='nw')
    #all items
        self.allitemList = []
        self.allitemList = self.itemInfo("tbl_all_items")
        print(self.allitemList)

        self.allphotos = []
        for i in range(len(self.allitemList)):
            #self.photo = PhotoImage(file=self.itemList[i][2])
            #self.photoimage = self.photo.subsample(9, 9)
            self.allphotos.append(PhotoImage(file=self.allitemList[i][2]).subsample(9, 9))

        counter = 0
        for i in range(0, len(self.allitemList)):
            print(i)
            if (i%2) == 0:
                self.item = ttk.Frame(self.itemsframe, height=165, width=157, style="info.TFrame")
                self.item.grid(row=counter, column=0)
                self.item.grid_propagate(False)
                self.items_btn = ttk.Button(self.item, text= "tbl_all_items", image=self.allphotos[i], style="item.TButton", command=lambda k=i :self.gotospecifcitem("tbl_all_items", k))
                self.items_btn.grid(row=0, column=0)
                self.title = ttk.Label(self.item, text=self.allitemList[i][1])
                self.title.grid(row=1, column=0)
            else:
                self.item = ttk.Frame(self.itemsframe, height=165, width=157, style="info.TFrame")
                self.item.grid(row=counter, column=1)
                self.item.grid_propagate(False)
                self.items_btn = ttk.Button(self.item, text="tbl_all_items", image=self.allphotos[i], style="item.TButton", command= lambda k=i :self.gotospecifcitem("tbl_all_items", k))
                self.items_btn.grid(row=0, column=0)
                self.title = ttk.Label(self.item, text=self.allitemList[i][1])
                self.title.grid(row=1, column=0)
                counter = counter + 1
        # self.treev.bind('<ButtonRelease-1>', self.itemList)

#jewlery items
        self.mycanvas1 = Canvas(self.jewlery, height=390, width=335)
        self.mycanvas1.grid(row=0, column=0)
        self.yscrollbar1 = ttk.Scrollbar(self.jewlery, orient='vertical', command=self.mycanvas1.yview)
        self.yscrollbar1.grid(row=0, column=1, sticky=NS)
        self.mycanvas1.configure(yscrollcommand=self.yscrollbar1.set)
        self.mycanvas1.bind('<Configure>', lambda e: self.mycanvas1.configure(scrollregion=self.mycanvas1.bbox('all')))

        self.jitemsframe = Frame(self.mycanvas1)
        self.mycanvas1.create_window((0, 0), window=self.jitemsframe, anchor='nw')

        self.jewelryitemList = []
        self.jewelryitemList = self.itemInfo("tbl_jewelry")
        print(self.jewelryitemList)

        self.jewelryphotos = []
        for i in range(len(self.jewelryitemList)):
            self.jewelryphotos.append(PhotoImage(file=self.jewelryitemList[i][2]).subsample(9, 9))

        counter = 0
        for i in range(0, len(self.jewelryitemList)):
            if (i % 2) == 0:
                self.jitem = ttk.Frame(self.jitemsframe, height=165, width=157, style="info.TFrame")
                self.jitem.grid(row=counter, column=0)
                self.jitem.grid_propagate(False)
                self.jitems_btn = ttk.Button(self.jitem, text="tbl_jewelry", image=self.jewelryphotos[i],
                                            style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_jewelry", k))
                self.jitems_btn.grid(row=0, column=0)
                self.jtitle = ttk.Label(self.jitem, text=self.jewelryitemList[i][1])
                self.jtitle.grid(row=1, column=0)
            else:
                self.jitem = ttk.Frame(self.jitemsframe, height=165, width=157, style="info.TFrame")
                self.jitem.grid(row=counter, column=1)
                self.jitem.grid_propagate(False)
                self.jitems_btn = ttk.Button(self.jitem, text="tbl_jewelry", image=self.jewelryphotos[i],
                                            style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_jewelry", k))
                self.jitems_btn.grid(row=0, column=0)
                self.jtitle = ttk.Label(self.jitem, text=self.jewelryitemList[i][1])
                self.jtitle.grid(row=1, column=0)
                counter = counter + 1

# Gold items
        self.mycanvas2 = Canvas(self.gold, height=390, width=335)
        self.mycanvas2.grid(row=0, column=0)
        self.yscrollbar2 = ttk.Scrollbar(self.gold, orient='vertical', command=self.mycanvas2.yview)
        self.yscrollbar2.grid(row=0, column=1, sticky=NS)
        self.mycanvas2.configure(yscrollcommand=self.yscrollbar2.set)
        self.mycanvas2.bind('<Configure>', lambda e: self.mycanvas2.configure(scrollregion=self.mycanvas2.bbox('all')))

        self.gitemsframe = Frame(self.mycanvas2)
        self.mycanvas2.create_window((0, 0), window=self.gitemsframe, anchor='nw')

        self.golditemList = []
        self.golditemList = self.itemInfo("tbl_gold")
        print(self.golditemList)

        self.goldphotos = []
        for i in range(len(self.golditemList)):
            self.goldphotos.append(PhotoImage(file=self.golditemList[i][2]).subsample(9, 9))

        counter = 0
        for i in range(0, len(self.golditemList)):
            if (i % 2) == 0:
                self.gitem = ttk.Frame(self.gitemsframe, height=165, width=157, style="info.TFrame")
                self.gitem.grid(row=counter, column=0)
                self.gitem.grid_propagate(False)
                self.gitems_btn = ttk.Button(self.gitem, text="tbl_gold", image=self.goldphotos[i],
                                            style="item.TButton", command= lambda k=i: self.gotospecifcitem("tbl_gold", k))
                self.gitems_btn.grid(row=0, column=0)
                self.gtitle = ttk.Label(self.gitem, text=self.golditemList[i][1])
                self.gtitle.grid(row=1, column=0)
            else:
                self.gitem = ttk.Frame(self.gitemsframe, height=165, width=157, style="info.TFrame")
                self.gitem.grid(row=counter, column=1)
                self.gitem.grid_propagate(False)
                self.gitems_btn = ttk.Button(self.gitem, text="tbl_gold", image=self.goldphotos[i],
                                            style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_gold", k))
                self.gitems_btn.grid(row=0, column=0)
                self.gtitle = ttk.Label(self.gitem, text=self.golditemList[i][1])
                self.gtitle.grid(row=1, column=0)
                counter = counter + 1

# Electric items
        self.mycanvas3 = Canvas(self.electronics, height=390, width=335)
        self.mycanvas3.grid(row=0, column=0)
        self.yscrollbar3 = ttk.Scrollbar(self.electronics, orient='vertical', command=self.mycanvas3.yview)
        self.yscrollbar3.grid(row=0, column=1, sticky=NS)
        self.mycanvas3.configure(yscrollcommand=self.yscrollbar3.set)
        self.mycanvas3.bind('<Configure>', lambda e: self.mycanvas3.configure(scrollregion=self.mycanvas3.bbox('all')))

        self.eitemsframe = Frame(self.mycanvas3)
        self.mycanvas3.create_window((0, 0), window=self.eitemsframe, anchor='nw')

        self.elecitemList = []
        self.elecitemList = self.itemInfo("tbl_electronics")
        print(self.elecitemList)

        self.elecphotos = []
        for i in range(len(self.elecitemList)):
            self.elecphotos.append(PhotoImage(file=self.elecitemList[i][2]).subsample(9, 9))

        counter = 0
        for i in range(0, len(self.elecitemList)):
            if (i % 2) == 0:
                self.eitem = ttk.Frame(self.eitemsframe, height=165, width=157, style="info.TFrame")
                self.eitem.grid(row=counter, column=0)
                self.eitem.grid_propagate(False)
                self.eitems_btn = ttk.Button(self.eitem, text="tbl_electronics", image=self.elecphotos[i],
                                            style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_electronics", k))
                self.eitems_btn.grid(row=0, column=0)
                self.etitle = ttk.Label(self.eitem, text=self.elecitemList[i][1])
                self.etitle.grid(row=1, column=0)
            else:
                self.eitem = ttk.Frame(self.eitemsframe, height=165, width=157, style="info.TFrame")
                self.eitem.grid(row=counter, column=1)
                self.eitem.grid_propagate(False)
                self.eitems_btn = ttk.Button(self.eitem, text="tbl_electronics", image=self.elecphotos[i],
                                            style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_electronics", k))
                self.eitems_btn.grid(row=0, column=0)
                self.etitle = ttk.Label(self.eitem, text=self.elecitemList[i][1])
                self.etitle.grid(row=1, column=0)
                counter = counter + 1

#Others
        self.mycanvas4 = Canvas(self.others, height=390, width=335)
        self.mycanvas4.grid(row=0, column=0)
        self.yscrollbar4 = ttk.Scrollbar(self.others, orient='vertical', command=self.mycanvas4.yview)
        self.yscrollbar4.grid(row=0, column=1, sticky=NS)
        self.mycanvas4.configure(yscrollcommand=self.yscrollbar4.set)
        self.mycanvas4.bind('<Configure>', lambda e: self.mycanvas4.configure(scrollregion=self.mycanvas4.bbox('all')))

        self.oitemsframe = Frame(self.mycanvas4)
        self.mycanvas4.create_window((0, 0), window=self.oitemsframe, anchor='nw')

        self.otheritemList = []
        self.otheritemList = self.itemInfo("tbl_others")
        print(self.otheritemList)

        self.otherphotos = []
        for i in range(len(self.otheritemList)):
            self.otherphotos.append(PhotoImage(file=self.otheritemList[i][2]).subsample(9, 9))

        counter = 0
        for i in range(0, len(self.otheritemList)):
            if (i % 2) == 0:
                self.oitem = ttk.Frame(self.oitemsframe, height=165, width=157, style="info.TFrame")
                self.oitem.grid(row=counter, column=0)
                self.oitem.grid_propagate(False)
                self.oitems_btn = ttk.Button(self.oitem, text="tbl_others", image=self.otherphotos[i],
                                  style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_others", k))
                self.oitems_btn.grid(row=0, column=0)
                self.otitle = ttk.Label(self.oitem, text=self.otheritemList[i][1])
                self.otitle.grid(row=1, column=0)
            else:
                self.oitem = ttk.Frame(self.oitemsframe, height=165, width=157, style="info.TFrame")
                self.oitem.grid(row=counter, column=1)
                self.oitem.grid_propagate(False)
                self.oitems_btn = ttk.Button(self.oitem, text="tbl_others", image=self.otherphotos[i],
                                  style="item.TButton", command=lambda k=i: self.gotospecifcitem("tbl_others", k))
                self.oitems_btn.grid(row=0, column=0)
                self.otitle = ttk.Label(self.oitem, text=self.otheritemList[i][1])
                self.otitle.grid(row=1, column=0)
                counter = counter + 1

    #bottom
        # bottom row buttons
        self.frame2 = ttk.Frame(self.root, height=40, width=354)
        self.frame2['padding'] = (0, 10, 0, 10)
        self.frame2.grid(row=4, column=0, columnspan=2, sticky=NSEW)
            # home but
        self.photo1 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/home-but.png")
        self.photoimage1 = self.photo1.subsample(6, 6)
        self.home_btn = ttk.Button(self.frame2, text='', image=self.photoimage1, style="transparent.TButton", command = self.gotohome)
        self.home_btn.grid(row=0, column=0, padx=30)
            # contract but
        self.photo2 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/contract-but.png")
        self.photoimage2 = self.photo2.subsample(5, 5)
        self.contract_btn = ttk.Button(self.frame2, text='', image=self.photoimage2, style="transparent.TButton")
        self.contract_btn.grid(row=0, column=1, padx=20)
            # marketbut
        self.photo3 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/market-but.png")
        self.photoimage3 = self.photo3.subsample(5, 5)
        self.market_btn = ttk.Button(self.frame2, text='', image=self.photoimage3, style="transparent.TButton", command=self.gotomarket)
        self.market_btn.grid(row=0, column=2, padx=20)
            # profile but
        self.photo4 = PhotoImage(file="/Users/22NitaC/PycharmProjects/pawnshop/Images/profile-but.png")
        self.photoimage4 = self.photo4.subsample(5, 5)
        self.profile_btn = ttk.Button(self.frame2, text='', image=self.photoimage4, style="transparent.TButton", command=self.gotoprofile)
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

    def gotospecifcitem(self, db, code):
        self.code = code
        self.database = db
        print(self.code)
        print(self.database)

        import specifcitemPage as specificitempage
        specificitempage = specificitempage.specificitem(self.root, self.username, self.database, self.code)

        # self.name = self.title.cget('text')
        # print(self.name)
        #
        # self.sql = "SELECT code FROM " + database + " WHEN name = '" + self.name + "'"
        # print(self.sql)
        # # count(*)= check through all rows
        # self.conn = db_conn.mysqlconnect()
        # self.cur = self.conn.cursor()
        # self.cur.execute(self.sql)  # execute sql query
        # self.result = self.cur.fetchall()
        #
        # self.code = []
        # for row in self.result:
        #     self.code.append(row)
        # print(self.code)
        # return self.code
