from tkinter import *
from tkinter import ttk
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker2(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)
def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    val=str(var.get())+", " #value 1,2 või 3
    ent.insert(END,val)

def uus_aken():
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["pilt1.png","pilt2.png","pilt3.png","pilt4.png","pilt5.png"]


    tab1= Frame(tabs)
    img1=PhotoImage(file=texts[0])
    tab2=Frame(tabs)
    tab3=Frame(tabs)
    tab4=Frame(tabs)
    tab5=Frame(tabs)
    tabs.add(tab1,text=texts[0])
    tabs.add(tab2,text=texts[1])
    tabs.add(tab3,text=texts[2])
    tabs.add(tab4,text=texts[3])
    tabs.add(tab5,text=texts[4])
    tabs.grid(row=0,column=0)
    uusaken.mainloop()



aken=Tk() #Akna loomine
aken.title("Akna nimetus") #Akna pealkiri
aken.geometry("600x400") #Akna suurus

btn=Button(aken,text="Vajuta siia",font="Arial 20",fg="green",bg="lightblue", width=20, height=3,relief=SUNKEN)#GROOVE, RAISED Loome nupp
btn2=Button(aken,text="Vell aken", font="Arial 20",fg="green",bg="lightblue",command=uus_aken)

lbl=Label(aken,text="...") #Pealkiri
ent=Entry(aken,fg="blue",width=20,font="Arial 20",justify=CENTER) #Rida teksti sisestamiseks. tekxt on keskel
var=IntVar() #StringVar()
#var.set(3) valib kolmas button
r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik)

btn.bind("<Button-1>",klikker)#LKM 
btn.bind("<Button-3>",klikker2)#PKM
ent.bind("<Return>",text_to_lbl)#Enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
btn2.pack(side=RIGHT)
aken.mainloop()

