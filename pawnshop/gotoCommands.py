from tkinter import *
from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk

# class menuCommands:
#     def gotohome(self, root, user):
#         self.root.withdraw()
#         import homePage as homepage
#         homepage = homepage.homepage(root, user)
#     def gotoprofile(self, root, user):
#         self.root.withdraw()
#         import profilePage as profilepage
#         profilepage = profilepage.profile(root, user)
#     def gotosettings(self, root, user):
#         self.root.withdraw()
#         import settingsPage as settingspage
#         settingspage = settingspage.settings(root, user)
#     def gotopolicies(self, root, user):
#         self.root.withdraw()
#         import policiesPage as policiespage
#         policiespage = policiespage.policies(root, user)
#
#     incomp-skxnkas

class goto:
    def gotofavs(self):
        username = "n"
        self.root.withdraw()
        import favsPage as favspage
        favspage = favspage.home(self.root, username)

    def gotohome(self):
        username = "n"
        self.root.withdraw()
        import homePage as homepage
        homepage = homepage.home(self.root, username)

    def gotocontract(self):
        username = "n"
        self.root.withdraw()
        import policiesPage as contractpage
        contractpage = contractpage.contract(self.root, username)

    def gotomarket(self):
        username = "n"
        # dont forget to user later for ALLL!!!!!!
        self.root.withdraw()
        import marketPage as marketpage
        marketpage = marketpage.market(self.root, username)

    def gotoprofile(self):
        username = "n"
        self.root.withdraw()
        import profilePage as profilepage
        profilepage = profilepage.profile(self.root, username)

class widgets:
    def scrollframe(self):
        self.canvas = Canvas(all, height=390, width=335)
        # make dimension a bit smaller to see scroll bar
        self.canvas.grid(row=0, column=0, sticky=NSEW)
        self.yscrollbar = ttk.Scrollbar(all, orient='vertical', command=self.canvas.yview)
        self.yscrollbar.grid(row=0, column=1, sticky=NS)
        self.canvas.configure(yscrollcommand=self.yscrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        self.itemsframe = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.itemsframe, anchor="nw")