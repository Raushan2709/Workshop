from tkinter import *
root=Tk()
text=Text(root)
root.title("EVM")
root.geometry("700x500")


v1=0
v2=0
def vote1():
    global v1
    v1=v1+1
    print("value of v1",v1)
def vote2():
    global v2
    v2=v2+1
    print("value of v2",v2)
def result():
    if v1>v2:
        Label(root,text="Winner party1",height=2,width=10).grid(row=4,column=2)
    elif v1<v2:
        Label(root,text="Winner party2",height=2,width=10).grid(row=4,column=2)
    else:
        Label(root,text="Draw",height=2,width=10).grid(row=4,column=2)

    btn1.config(state=("disable"))
    btn2.config(state=("disable"))         
        
    
Label(root,text="party1",height=2,width=10).grid(row=1,column=1)
btn1=Button(root,text="VOTE",command=vote1)
btn1.grid(row=1,column=2)

Label(root,text="party2",height=2,width=10).grid(row=2,column=1)
btn2=Button(root,text="VOTE",command=vote2)
btn2.grid(row=2,column=2)

btn3=Button(root,text="result",command=result).grid(row=3,column=3)
w=Entry(root,text="enter name")
w.grid(row=4,column=2)
