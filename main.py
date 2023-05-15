#pip install PyMySQL
from tkinter import font
from turtle import width
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connection
def connection():
	conn=pymysql.connect(
		host='localhost',user='root',password='',db='student_db'
	)
	return conn

def refreshTable():
	for data in my_tree.get_children():
		my_tree.delete(data)

	for array in read():
		my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")

	my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',12))
	my_tree.grid(row=8,column=0,columnspan=5,rowspan=11,padx=10,pady=10)

#gui
root = Tk()
root.title("DDD Club Membership Registration System")
root.geometry("1150x720")
my_tree = ttk.Treeview(root)

#functions

#placeholders
ph1=tk.StringVar()
ph2=tk.StringVar()
ph3=tk.StringVar()
ph4=tk.StringVar()
ph5=tk.StringVar()

#placeholder values
def setph(word,num):
	if num ==1:
		ph1.set(word)
	if num ==2:
		ph2.set(word)
	if num ==3:
		ph3.set(word)
	if num ==4:
		ph4.set(word)
	if num ==5:
		ph5.set(word)

def read():
	conn=connection()
	cursor=conn.cursor()
	cursor.execute("SELECT * FROM students")
	results=cursor.fetchall()
	conn.commit()
	conn.close()
	return results

def add():
	studid=str(studidEntry.get())
	fname=str(fnameEntry.get())
	lname=str(lnameEntry.get())
	address=str(addressEntry.get())
	phone=str(phoneEntry.get())

	if(studid=="" or studid==" ") or (fname=="" or fname==" ") or (lname=="" or lname==" ") or (address=="" or address==" ") or (phone=="" or phone==" "):
		messagebox.showinfo("Error","Please fill up the blank entry")
		return
	else:
		try:
			conn=connection()
			cursor=conn.cursor()
			cursor.execute("INSERT INTO students VALUES ('"+studid+"','"+fname+"','"+lname+"','"+address+"','"+phone+"') ")
			results=cursor.fetchall()
			conn.commit()
			conn.close()
		except:
			messagebox.showinfo("Error","Student ID already exists")
			return
	refreshTable()

def reset():
	decision=messagebox.askquestion("Warning!", "Delete all data?")
	if decision != "yes":
		return
	else:
		try:
			conn=connection()
			cursor=conn.cursor()
			cursor.execute("DELETE FROM students")
			results=cursor.fetchall()
			conn.commit()
			conn.close()
		except:
			messagebox.showinfo("Error","An error has occured")
			return
	refreshTable()

def delete():
	decision=messagebox.askquestion("Warning!", "Delete selected data?")
	if decision != "yes":
		return
	else:
		selected_item=my_tree.selection()[0]
		deleteData=str(my_tree.item(selected_item)['values'][0])
		try:
			conn=connection()
			cursor=conn.cursor()
			cursor.execute("DELETE FROM students WHERE STUDID='"+str(deleteData)+"'")
			results=cursor.fetchall()
			conn.commit()
			conn.close()
		except:
			messagebox.showinfo("Error","An error has occured")
			return
	refreshTable()

def select():
	try:
		selected_item=my_tree.selection()[0]
		studid=str(my_tree.item(selected_item)['values'][0])
		fname=str(my_tree.item(selected_item)['values'][1])
		lname=str(my_tree.item(selected_item)['values'][2])
		address=str(my_tree.item(selected_item)['values'][3])
		phone=str(my_tree.item(selected_item)['values'][4])

		setph(studid,1)
		setph(fname,2)
		setph(lname,3)
		setph(address,4)
		setph(phone,5)
	except:
		messagebox.showinfo("Error","Please select a data")

def search():
	studid=str(studidEntry.get())
	fname=str(fnameEntry.get())
	lname=str(lnameEntry.get())
	address=str(addressEntry.get())
	phone=str(phoneEntry.get())

	conn=connection()
	cursor=conn.cursor()
	cursor.execute("SELECT * FROM students WHERE STUDID='"+
    studid+"' or FNAME='"+
    fname+"' or LNAME='"+
    lname+"' or ADDRESS='"+
    address+"' or PHONE='"+
    phone+"' ")	
	
	try:
		result=cursor.fetchall()
		for num in range(0,5):
			setph(result[0][num],(num+1))\

		conn.commit()
		conn.close()
	except:
		messagebox.showinfo("Error","No data found")

def update():
	selectedStudid=""
	try:
		selected_item=my_tree.selection()[0]
		selectedStudid=str(my_tree.item(selected_item)['values'][0])
	except:
		messagebox.showinfo("Error","Please select a data")

	studid=str(studidEntry.get())
	fname=str(fnameEntry.get())
	lname=str(lnameEntry.get())
	address=str(addressEntry.get())
	phone=str(phoneEntry.get())

	if(studid=="" or studid==" ") or (fname=="" or fname==" ") or (lname=="" or lname==" ") or (address=="" or address==" ") or (phone=="" or phone==" "):
		messagebox.showinfo("Error","Please fill up the blank entry")
		return
	else:
		try:
			conn=connection()
			cursor=conn.cursor()
			cursor.execute("UPDATE students SET STUDID='"+
            studid+"', FNAME='"+
            fname+"', LNAME='"+
            lname+"', ADDRESS='"+
            address+"', PHONE='"+
            phone+"' WHERE STUDID='"+
            selectedStudid+"' ")
			results=cursor.fetchall()
			conn.commit()
			conn.close()
		except:
			messagebox.showinfo("Error","Student ID already exists")
			return
	refreshTable()

#gui
label = Label(root, text="Welcome to DDD Club Membership Registration!", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

studidLabel = Label(root, text="Club ID", font=('Arial', 15))
fnameLabel = Label(root, text="First Name", font=('Arial', 15))
lnameLabel = Label(root, text="Last Name", font=('Arial', 15))
addressLabel = Label(root, text="Hometown", font=('Arial', 15))
phoneLabel = Label(root, text="Student Number", font=('Arial', 15))

studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
lnameLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
addressLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
phoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

#text variable
studidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph1)
fnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph2)
lnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph3)
addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph4)
phoneEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)

studidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
fnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
lnameEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
phoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

#command
addBtn = Button(
    root, text="ADD", padx=65, pady=25, width=10,
    bd=5, font=('Arial Bold', 15), bg="#00FFFF", command=add)
updateBtn = Button(
    root, text="UPDATE", padx=65, pady=25, width=10,
    bd=5, font=('Arial Bold', 15), bg="#00FFFF", command=update)
deleteBtn = Button(
    root, text="DELETE", padx=65, pady=25, width=10,
    bd=5, font=('Arial Bold', 15), bg="#00FFFF", command=delete)
searchBtn = Button(
    root, text="SEARCH", padx=65, pady=25, width=10,
    bd=5, font=('Arial Bold', 15), bg="#00FFFF", command=search)
resetBtn = Button(
    root, text="RESET", padx=65, pady=25, width=10,
    bd=5, font=('Arial Bold', 15), bg="#00FFFF", command=reset)
selectBtn = Button(
    root, text="SELECT", padx=65, pady=25, width=10,
    bd=5, font=('Arial Bold', 15), bg="#00FFFF", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))
my_tree['columns'] = ("Stud ID","Firstname","Lastname","Address","Phone")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Stud ID", anchor=W, width=170)
my_tree.column("Firstname", anchor=W, width=150)
my_tree.column("Lastname", anchor=W, width=150)
my_tree.column("Address", anchor=W, width=165)
my_tree.column("Phone", anchor=W, width=150)

my_tree.heading("Stud ID", text="CLUB ID", anchor=W)
my_tree.heading("Firstname", text="FIRST NAME", anchor=W)
my_tree.heading("Lastname", text="LAST NAME", anchor=W)
my_tree.heading("Address", text="HOMETOWN", anchor=W)
my_tree.heading("Phone", text="STUDENT NUM", anchor=W)

refreshTable()

root.mainloop()