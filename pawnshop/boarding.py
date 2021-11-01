from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from ttkbootstrap import Style
from tkinter import ttk
import db_conn

#customizing style, colors, fonts
style = Style(theme='lumen')
root = style.master
#making custom style
style.configure('TButton', font=("Helvetica", 16))
style.configure('my.TButton', font=("Helvetica", 10))
style.configure("menustyle.TFrame", background = "gray")
style.configure('login.TNotebook', tabposition='nsew')
style.configure("transparent.TButton")
style.configure("scrolltab.TButton")
style.configure("invisible.Horizontal.TScrollbar")
style.configure("item.TButton")
style.configure("bottomMain.TButton")
style.configure("payment.TRadiobutton", font=("Helvetica", 18))

root.title("Boarding Page")
root.geometry("414x896")

frame1 = ttk.Frame(root, height=750, width=370)
frame1['padding'] = (80, 80, 80, 80)
frame1.grid(row=1, column=0, columnspan=10, sticky=NSEW)

#textbox labels and labels
load = Image.open("Images/pawnblock_ss.png")
resized_image= load.resize((205,378), Image.ANTIALIAS)
render= ImageTk.PhotoImage(resized_image)
img = Label(frame1, image=render)
img.image = render
img.grid(row=0, column=0, columnspan=2 ,ipadx= 5, ipady=20, sticky=S)

def gotologin():
    root.withdraw()
    # import LoginPage as login
    # signuppage = login.Login(root)

    import login2 as login2
    login2 = login2.Login(root)

btn_customer = ttk.Button(frame1, text = "Customer", style = "primary.TButton", command = gotologin)
btn_customer.grid(row=1, column=0, columnspan=2, ipadx= 5, ipady=20, sticky=NSEW)

seperator = ttk.Label(frame1, text= "")
seperator.grid(row=2, column=0, columnspan=2)

btn_pawnshop = ttk.Button(frame1, text = "Pawnshop", style = "primary.TButton")
btn_pawnshop.grid(row=3, column=0, columnspan=2, ipadx= 5, ipady=20, sticky=NSEW)

mainloop()

