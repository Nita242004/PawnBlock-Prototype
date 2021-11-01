from tkinter import *
from tkinter import font

newline = ''
fileContent = []
filePath = 'C:/path to/ file.txt'
lines = open(filePath)
newline = lines.read()

w = Tk()


def openViewer():
    pop = Toplevel(w)
    pop.title('Operation Report')
    pop.geometry("750x500+15+20")
    pop.state('zoomed')  # Window's Miximize button
    frame = Frame(pop, width=780, height=560)
    frame.grid(row=0, column=0)
    # I decreased the canvas height to show the x scrollbar and removed
    # the create_text method width attribute to unwrap the text and
    # activate the horizontal scrollbar
    canvas = Canvas(frame, width=780, height=530, background='black')
    verdana_font = font.Font(family="Verdana", size=13)
    canvas.create_text((0, 0), anchor='nw', text=newline,
                       font=verdana_font, fill='light grey',
                       justify=LEFT)  # Add this width=750 to wrap text
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=canvas.xview)
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=canvas.yview)
    canvas.config(scrollregion=canvas.bbox(ALL))
    canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    canvas.pack(side=LEFT, expand=True, fill=BOTH)


btn = Button(w, text='View Content', command=openViewer)
btn.pack()

w.mainloop()