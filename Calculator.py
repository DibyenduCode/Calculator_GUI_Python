#import libs...............................................................

import tkinter
from tkinter import *


#function for buttons......................................................
por=""
val=""
A=0
def bt1_onclicked():
    global val
    val=val+"1"
    data.set(val)

def bt2_onclicked():
    global val
    val=val+"2"
    data.set(val)

def bt3_onclicked():
    global val
    val=val+"3"
    data.set(val)

def bt4_onclicked():
    global val
    global A
    global por
    A=int(val)
    val=val+"+"
    por="+"
    data.set(val)
    
def bt5_onclicked():
    global val
    val=val+"4"
    data.set(val)
    
def bt6_onclicked():
    global val
    val=val+"5"
    data.set(val)
    
def bt7_onclicked():
    global val
    val=val+"6"
    data.set(val)
    
def bt8_onclicked():
    global val
    global A
    global por
    A=int(val)
    por="-"
    val=val+"-"
    data.set(val)
    
def bt9_onclicked():
    global val
    val=val+"7"
    data.set(val)

def bt10_onclicked():
    global val
    val=val+"8"
    data.set(val)
    
def bt11_onclicked():
    global val
    val=val+"9"
    data.set(val)
    
def bt12_onclicked():
    global val
    global A
    global por
    A=int(val)
    por="*"
    val=val+"*"
    data.set(val)
    
def clear():
    global val
    val=""
    data.set(val)




def equal():
    global val
    global A
    global por
    val2=val
    if(por=="+"):
        x=val2.split("+")
        y=int(x[1])
        c=y+A
        data.set(c)
        val=str(c)
    elif(por=="-"):
        x=val2.split("-")
        y=int(x[1])
        c=A-y
        data.set(c)
        val=str(c)
    elif(por=="*"):
        x=val2.split("*")
        y=int(x[1])
        c=A*y
        data.set(c)
        val=c
    elif(por=="/"):
        x=val2.split("/")
        y=int(x[1])
        if(y==0):
            messagebox.showerror("Error","It is not divisibale")
        else:
            c=int(A/y)
            data.set(c)
            val=str(c)

def bt15_onclicked():
    global val
    val=val+"0"
    data.set(val)
    
def bt16_onclicked():
    global val
    global A
    global por
    por="/"
    A=int(val)
    val=val+"/"
    data.set(val)
    

#main GUI ................................................................
    
root=tkinter.Tk()
root.title("Calculator")
root.geometry("250x400")
root.resizable(0,0)
data=StringVar()

#input label.............................................................

lab1=Label(root,
           text="input",
           font=("Calibri","22"),
           bg="white",
           width=20,
           height=2,
           anchor="se",
           textvariable=data,)
lab1.pack()

#frames...................................................................

cab1 = Frame(root,bg="#000000")
cab1.pack(expand = True, fill = "both",)


cab2 = Frame(root)
cab2.pack(expand= True, fill = "both",)

cab3 = Frame(root)
cab3.pack(expand= True, fill = "both",)

cab4 = Frame(root)
cab4.pack(expand = True, fill = "both",)
#buttons(0 to 9,+,-,*,/,=,C).................................................
click_bt1=Button(cab1,
                 text="1",
                 font=("Verdana","22"),
                 border=0,
                 command=bt1_onclicked,
                 )
click_bt1.pack(fill="both",
               expand=True,
               side=LEFT, 
               )

click_bt2=Button(cab1,
                 text="2",
                 font=("Verdana","22"),
                 border=0,
                 command=bt2_onclicked,
                 )
click_bt2.pack(side=LEFT,
               fill="both",
               expand=True)

click_bt3=Button(cab1,
                 text="3",
                 font=("Verdana","22"),
                 border=0,
                 command=bt3_onclicked,
                 )
click_bt3.pack(side=LEFT,
               fill="both",
               expand=True)

click_bt4=Button(cab1,
                 text="+",
                 font=("Verdana","22"),
                 border=0,
                 command=bt4_onclicked,
                 )
click_bt4.pack(side=LEFT,
               fill="both",
               expand=True)

click_bt5=Button(cab2,
                 text="4",
                 font=("Verdana","22"),
                 border=0,
                 command=bt5_onclicked,
                 )
click_bt5.pack(fill="both",
               expand=True,
               side=LEFT
               )

click_bt6=Button(cab2,
                 text="5",
                 font=("Verdana","22"),
                 border=0,
                 command=bt6_onclicked,
                 )
click_bt6.pack(side=LEFT,
               fill="both",
               expand=True)

click_bt7=Button(cab2,
                 text="6",
                 font=("Verdana","22"),
                 border=0,
                 command=bt7_onclicked,
                 )
click_bt7.pack(side=LEFT,
               fill="both",
               expand=True)

click_bt8=Button(cab2,
                 text="-",
                 font=("Verdana","22"),
                 border=0,
                 command=bt8_onclicked,
                 )
click_bt8.pack(side=LEFT,
               fill="both",
               expand=True)

click_bt9=Button(cab3,
                 text="7",
                 font=("Verdana","22"),
                 border=0,
                 command=bt9_onclicked,
                 )
click_bt9.pack(side=LEFT,
               fill="both",
               expand=True,
               )

click_bt10=Button(cab3,
                text="8",
                font=("vardana","22"),
                border=0,
                command=bt10_onclicked,
                  )
click_bt10.pack(side=LEFT,
                fill="both",
                expand=True,
                  )

click_bt11=Button(cab3,
                text="9",
                font=("vardana","22"),
                border=0,
                command=bt11_onclicked,
                  )
click_bt11.pack(side=LEFT,
                fill="both",
                expand=True,
                  )

click_bt12=Button(cab3,
                text="*",
                font=("vardana","22"),
                border=0,
                command=bt12_onclicked,
                  )
click_bt12.pack(side=LEFT,
                fill="both",
                expand=True,
                  )

click_bt13=Button(cab4,
                 text="C",
                 font=("Verdana","22"),
                 border=0,
                 command=clear,
                  )
click_bt13.pack(side=LEFT,
               fill="both",
               expand=True,
               )
click_bt14=Button(cab4,
                text="0",
                font=("vardana","22"),
                border=0,
                command=bt15_onclicked,
                  )
click_bt14.pack(side=LEFT,
                fill="both",
                expand=True,
                  )

click_bt15=Button(cab4,
                text="=",
                font=("vardana","22"),
                border=0,
                command=equal,
                )
click_bt15.pack(side=LEFT,
                fill="both",
                expand=True,
                  )

click_bt16=Button(cab4,
                text="/",
                font=("vardana","22"),
                border=0,
                command=bt16_onclicked,
                  )
click_bt16.pack(side=LEFT,
                fill="both",
                expand=True,
                  )


root.mainloop()
