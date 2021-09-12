from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("","end",values=i)

def search():
    q2 = var1.get()
    command2 = "select * from customers where first_name like '%"+q2+"%' or last_name like '%"+q2+"%'"
    cursor.execute(command2)
    rows =cursor.fetchall()
    mydb.commit()
    update(rows)
def clear():
    cursor = mydb.cursor()
    command = "select id,first_name,last_name,age from customers"
    cursor.execute(command)
    rows = cursor.fetchall()
    mydb.commit()
    update(rows)
def getall(event):
    rowid = trv.identify_row(event.y)
    item =trv.item(trv.focus())
    var2.set(item['values'][0])
    var3.set(item['values'][1])
    var4.set(item['values'][2])
    var5.set(item['values'][3])
def addnew():
    cursor1 = mydb.cursor()
    command=('insert into customers(id,first_name,last_name,age) value (NULL,%s,%s,%s) ')
    vals=(var3.get(),var4.get(),var5.get())
    cursor1.execute(command,vals)
    rows = cursor.fetchall()
    mydb.commit()
    clear()

def updatec():
    vals=(var3.get(),var4.get(),var5.get(),var2.get())
    command = ('update customers set first_name =%s,last_name  =%s,age =%s where id = %s ')
    cursor.execute(command,vals)
    mydb.commit()
    clear()

def delete():
    cusyid =var2.get()
    msg1  =messagebox.askyesno("Confirmation","Are you sure do you want to delete Customers data")
    if msg1==True:
        cursor3 = mydb.cursor()
        command3 = 'delete from customers where id = '+cusyid
        cursor3.execute(command3)
        mydb.commit()
        clear()
    else:
        pass

root = Tk()
root.geometry("800x700")
wrap1 =LabelFrame(root,text = "Customer Details" )
wrap1.pack(fill="both",expand = "yes",padx = 20,pady = 10)
wrap2 =LabelFrame(root,text = "Search")
wrap2.pack(fill="both",expand = "yes",padx = 20,pady = 10)
wrap3 =LabelFrame(root,text = "Customers Data")
wrap3.pack(fill="both",expand = "yes",padx = 20,pady = 10)
trv = ttk.Treeview(wrap1,columns = (1,2,3,4),show = "headings",height ="6")
trv.pack()
trv.heading(1,text = "Customer id")
trv.heading(2,text = "first name")
trv.heading(3,text = "last name")
trv.heading(4,text = "age")
trv.bind("<Double-1>",getall)
mydb =mysql.connector.connect(host='localhost', user='root', password='#', database='hotelui')
cursor =mydb.cursor()
command = "select id,first_name,last_name,age from customers"
cursor.execute(command)
rows = cursor.fetchall()
update(rows)
# Search Section
lbl1 = Label(wrap2,text = "Search")
lbl1.pack(side = "left")
var1 = StringVar()
tnt = Entry(wrap2,textvariable = var1)
tnt.pack(side = "left")
btn = Button(wrap2,text = "Search",command = search)
btn.pack(side = "left")
btn2 = Button(wrap2,text = "clear",command = clear)
btn2.pack(side = "left")
# data section
lbl1 = Label(wrap3,text = "Customer id")
lbl2 = Label(wrap3,text = "First Name")
lbl3 = Label(wrap3,text = "Last Name")
lbl4 = Label(wrap3,text = "Age")
lbl1.grid(row = 0,column = 1,padx = 5,pady = 3)
lbl2.grid(row = 1,column = 1,padx = 5,pady = 3)
lbl3.grid(row = 2,column = 1,padx = 5,pady = 3)
lbl4.grid(row = 3,column = 1,padx = 5,pady = 3)
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
ent1 = Entry(wrap3,textvariable = var2)
ent1.grid(row = 0,column = 2,padx = 5,pady = 3)
ent2 = Entry(wrap3,textvariable = var3)
ent2.grid(row = 1,column = 2,padx = 5,pady = 3)
ent3 = Entry(wrap3,textvariable = var4)
ent3.grid(row = 2,column = 2,padx = 5,pady = 3)
ent4 = Entry(wrap3,textvariable = var5)
ent4.grid(row = 3,column = 2,padx = 5,pady = 3)
btn3 = Button(wrap3,text="Add New",command = addnew)
btn3.grid(row = 4,column =1,padx =5,pady =3)
btn4 = Button(wrap3,text="Update",command = updatec)
btn4.grid(row = 4,column =2,padx =5,pady =3)
btn5 = Button(wrap3,text="Delete",command = delete)
btn5.grid(row = 4,column =3,padx =5,pady =3)

root.mainloop()
