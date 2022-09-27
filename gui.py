from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox,DISABLED,NORMAL
# import pymysql
import pickle
import datetime
from functools import partial
from PIL import Image, ImageTk
#from testing import process
import time
from tkinter.scrolledtext  import ScrolledText
title="Web attack detection"
bgmain='#4267B2'

def logcheck():
     global username_var,pass_var
     uname=username_var.get()
     pass1=pass_var.get()
     if uname=="admin" and pass1=="admin":
        showcheck()
     else:
         messagebox.showinfo("alert","Wrong Credentials")   

# show home page
# def showhome():
#     top.config(menu=menubar)
#     global f
#     f.pack_forget()
#     f=Frame(top)
#     f.config(bg=bgmain)
#     f.pack(side="top", fill="both", expand=True,padx=10,pady=10)
#     image = Image.open("leaf.jpg")
#     photo = ImageTk.PhotoImage(image.resize((top.winfo_width(), top.winfo_height()), Image.ANTIALIAS))
#     label = Label(f, image=photo, bg=bgmain)
#     label.image = photo
#     label.pack()

#     l=Label(f,text="Welcome",font = "Verdana 60 bold",fg="White",bg=bgmain)
#     l.place(x=500,y=300)

def showcheck():
    top.title(title)
    top.config(menu=menubar)
    global f
    f.pack_forget()
    f=Frame(top)
    f.config(bg="#664a8a")
    f.pack(side="top", fill="both", expand=True,padx=10,pady=10)

    #left 
    f1=Frame(f)
    f1.pack_propagate(False)
    f1.config(bg="#664a8a",width=500)
    f1.pack(side="left",fill="both")
    
    #right
    global f2
    f2=Frame(f)
    f2.pack_propagate(False)
    f2.config(bg="#664a8a",width=500)
    f2.pack(side="right",fill="both")

    #center
    f3=Frame(f)
    f3.pack_propagate(False)
    f3.config(bg="#664a8a",width=600)
    f3.pack(side="right",fill="both")

    f4=Frame(f3)
    f4.pack_propagate(False)
    f4.config(bg="#664a8a",height=200)
    f4.pack(side="bottom",fill="both")

    f7=Frame(f3)
    f7.pack_propagate(False)
    f7.config(height=20)
    f7.pack(side="top",fill="both",padx="3")

    l2=Label(f7,text="Server",font="Helvetica 13 bold")
    l2.pack()

    
    # b3=Button(f4,text="Cancel",font="Verdana 10 bold")
    # b3.pack(pady=2)

    f5=Frame(f1)
    f5.config(bg="#664a8a")
    f5.pack(side="top",fill="both")
    
    global f6
    f6=Frame(f2)
    f6.config(bg="#664a8a")
    f6.pack(side="top",fill="both")
    l1=Label(f6,text="Result",font="Helvetica 13 bold")
    l1.pack(side="top",fill="both")
    
    
    global st1,st2,st3,st4
    global lb1

    st2=ScrolledText(f6,height=5)
    st2.pack(side="bottom",fill="both",pady=7)

    l2=Label(f5,text="Device1",font="Helvetica 13 bold")
    l2.pack(side="top",fill="both")

    st1=ScrolledText(f5,height=5)
    st1.pack(side="top",fill="both",pady=7)

    b2=Button(f5,text="Sent",font="Verdana 10 bold",command=process1)
    b2.pack(pady=2,side='top')

    

    l2=Label(f5,text="Device2",font="Helvetica 13 bold")
    l2.pack(side="top",fill="both")

    st3=ScrolledText(f5,height=5)
    st3.pack(side="top",fill="both",pady=7)

    
    b2=Button(f5,text="Sent",font="Verdana 10 bold",command=process2)
    b2.pack(pady=2,side='top')

    l2=Label(f5,text="Device3",font="Helvetica 13 bold")
    l2.pack(side="top",fill="both")

    st4=ScrolledText(f5,height=5)
    st4.pack(side="top",fill="both",pady=7)

    b2=Button(f5,text="Sent",font="Verdana 10 bold",command=process3)
    b2.pack(pady=2,side='top')
    
    lb1=Listbox(f3,width=400,height=400,font="Helvetica 13 bold")
    lb1.pack(pady=10,padx=5)


def notint(x):
    try:
        x=float(x)
        return False
    except:
        return True   

from predict import predict1
def process1():
    lb1.delete(0,END)
    
    global st1,st2,t
    t=1
    
    st2.delete('1.0',END)
    text=st1.get('1.0',END)

    lb1.after(t,delayed_insert,lb1,0,'Request recieved from Device1')
    lb1.update()
    t+=1
  
    lb1.after(t,delayed_insert,lb1,0,'Extracting features')
    lb1.update()
    t+=1
    lb1.after(t,delayed_insert,lb1,0,'Load ensemble model')
    lb1.update()
    t+=1    
    lb1.after(t,delayed_insert,lb1,0,'Make prediction')
    lb1.update()
    t+=1 
    
    ret=predict1(text)
    if ret==0:
        msg="Normal"
    else:
        msg="Attack"    
    st2.after(2,showresult,msg)   

def process2():
    lb1.delete(0,END)
    
    global st1,st2,t
    t=1
    
    st2.delete('1.0',END)
    text=st1.get('1.0',END)

    lb1.after(t,delayed_insert,lb1,0,'Request recieved from Device2')
    lb1.update()
    t+=1
  
    lb1.after(t,delayed_insert,lb1,0,'Extracting features')
    lb1.update()
    t+=1
    lb1.after(t,delayed_insert,lb1,0,'Load ensemble model')
    lb1.update()
    t+=1    
    lb1.after(t,delayed_insert,lb1,0,'Make prediction')
    lb1.update()
    t+=1 
    
    ret=predict1(text)
    if ret==0:
        msg="Normal"
    else:
        msg="Attack"    
    st2.after(2,showresult,msg)   

def process3():
    lb1.delete(0,END)
    
    global st1,st2,t
    t=1
    
    st2.delete('1.0',END)
    text=st1.get('1.0',END)

    lb1.after(t,delayed_insert,lb1,0,'Request recieved from Device3')
    lb1.update()
    t+=1
  
    lb1.after(t,delayed_insert,lb1,0,'Extracting features')
    lb1.update()
    t+=1
    lb1.after(t,delayed_insert,lb1,0,'Load ensemble model')
    lb1.update()
    t+=1    
    lb1.after(t,delayed_insert,lb1,0,'Make prediction')
    lb1.update()
    t+=1 
    
    ret=predict1(text)
    if ret==0:
        msg="Normal"
    else:
        msg="Attack"    
    st2.after(2,showresult,msg)   

def showresult(res):
    global st2
    st2.insert(INSERT,res)


def delayed_insert(label,index,message):
    label.insert(0,message)  
    

if __name__=="__main__":

    top = Tk()  
    top.title("Login")
    top.geometry("1900x700")
    footer = Frame(top, bg='grey', height=30)
    footer.pack(fill='both', side='bottom')

    lab1=Label(footer,text="Developed by ###",font = "Verdana 8 bold",fg="white",bg="grey")
    lab1.pack()

    menubar = Menu(top)  
    #menubar.add_command(label="Home",command=showhome)  
    menubar.add_command(label="Detect",command=showcheck)
    

    top.config(bg=bgmain,relief=RAISED)  
    f=Frame(top)
    f.config(bg=bgmain)
    f.pack(side="top", fill="both", expand=True,padx=10,pady=10)
    l=Label(f,text=title,font = "Verdana 40 bold",fg="white",bg=bgmain)
    l.place(x=50,y=50)
    l2=Label(f,text="Username:",font="Verdana 10 bold",bg=bgmain)
    l2.place(x=550,y=300)
    global username_var
    username_var=StringVar()
    e1=Entry(f,textvariable=username_var,font="Verdana 10 bold")
    e1.place(x=700,y=300)

    l3=Label(f,text="Password:",font="Verdana 10 bold",bg=bgmain)
    l3.place(x=550,y=330)
    global pass_var
    pass_var=StringVar()
    e2=Entry(f,textvariable=pass_var,font="Verdana 10 bold",show='*')
    e2.place(x=700,y=330)

    b1=Button(f,text="Login", command=logcheck,font="Verdana 10 bold")
    b1.place(x=750,y=360)

    top.mainloop() 
