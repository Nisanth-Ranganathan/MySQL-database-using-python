from tkinter import *
import mysql.connector
from tkinter import messagebox
import pandas as pd
import openpyxl
import pymysql
from sqlalchemy import create_engine

root=Tk()
root.title("Student Form")
root.geometry("380x530")

#Database creation
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='Student')#install the mysql and then type the paaward that you used in the mysql password
my_cursor=mydb.cursor()
#Create table
#my_cursor.execute("CREATE TABLE Registration (First_Name VARCHAR(255),Last_Name VARCHAR(255), Roll_No VARCHAR(25),Email_ID VARCHAR(255), Mobile_Number BIGINT, Blood_Group VARCHAR(15), City VARCHAR(35), ID INTEGER AUTO_INCREMENT PRIMARY KEY)")

def Submit():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Student')
    my_cursor = mydb.cursor()
    firstname=e1.get()
    lastname=e2.get()
    rollno=e3.get()
    emailid=e4.get()
    mobileno=e5.get()
    blgr=e6.get()
    city=e7.get()
    my_cursor.execute("INSERT INTO Registration (First_Name,Last_Name,Roll_No,Email_ID,Mobile_Number,Blood_Group,City) VALUES ('"+firstname+"','"+lastname+"','"+rollno+"','"+emailid+"','"+mobileno+"','"+blgr+"','"+city+"')")
    mydb.commit()
    messagebox.showinfo("Success","Inserted succesfully")
    mydb.close()
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
def Delete():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Student')
    my_cursor = mydb.cursor()

    my_cursor.execute("DELETE FROM Registration WHERE ID='"+entry_delete.get()+"'")
    id=entry_delete.get()
    d= my_cursor.execute("SELECT * FROM Registration WHERE ID = '"+entry_delete.get()+"'")
    if id is not d:
        mydb.commit()
        messagebox.showinfo("Deleted", "Succesfully Deleted")
    else:
        messagebox.showinfo("Warning", "Nothing there to be Deleted")
    mydb.close()
def Update():
    global upd
    if entry_delete.get() == "":
        return
    else:
        upd=Tk()
        upd.title("Update")
        upd.geometry("420x480")
        mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Student')
        my_cursor = mydb.cursor()
        # Label Creation
        my_cursor.execute("SELECT * FROM Registration WHERE ID='"+entry_delete.get()+"'")
        dbresult=my_cursor.fetchall()
        global e1_edit
        global e2_edit
        global e3_edit
        global e4_edit
        global e5_edit
        global e6_edit
        global e7_edit
        b=""
        for record in dbresult:
            b+= str(record) + "\n"

        f_edit= Label(upd, text=b, font=("Pangolin", 10), pady=5, anchor="center")
        f_edit.grid(row=0, column=0, pady=10,columnspan=2)
        f1_edit = Label(upd, text="First Name", font=("Pangolin", 10), pady=5, anchor="center")
        f1_edit.grid(row=1, column=0, pady=10)
        f2_edit = Label(upd, text="Last Name", font=("Pangolin", 10), pady=5, anchor="center")
        f2_edit.grid(row=2, column=0, pady=5)
        f3_edit = Label(upd, text="Roll No", font=("Pangolin", 10), pady=5, anchor="center")
        f3_edit.grid(row=3, column=0, pady=5)
        f4_edit = Label(upd, text="Email ID", font=("Pangolin", 10), pady=5, anchor="center")
        f4_edit.grid(row=4, column=0, pady=5)
        f5_edit = Label(upd, text="Mobile Number", font=("Pangolin", 10), pady=5, anchor="center")
        f5_edit.grid(row=5, column=0, pady=5)
        f6_edit = Label(upd, text="Blood Group", font=("Pangolin", 10), pady=5, anchor="center")
        f6_edit.grid(row=6, column=0, pady=5)
        f7_edit = Label(upd, text="City", font=("Pangolin", 10), pady=5, anchor="center")
        f7_edit.grid(row=7, column=0, pady=5)
        # Entry creation
        e1_edit = Entry(upd, width=30, relief="flat", bd=3)
        e1_edit.grid(row=1, column=1, padx=5, pady=5)
        e2_edit = Entry(upd, width=30, relief="flat", bd=3)
        e2_edit.grid(row=2, column=1, padx=5, pady=5)
        e3_edit = Entry(upd, width=30, relief="flat", bd=3)
        e3_edit.grid(row=3, column=1, padx=5, pady=5)
        e4_edit = Entry(upd, width=30, relief="flat", bd=3)
        e4_edit.grid(row=4, column=1, padx=5, pady=5)
        e5_edit = Entry(upd, width=30, relief="flat", bd=3)
        e5_edit.grid(row=5, column=1, padx=5, pady=5)
        e6_edit = Entry(upd, width=30, relief="flat", bd=3)
        e6_edit.grid(row=6, column=1, padx=5, pady=5)
        e7_edit = Entry(upd, width=30, relief="flat", bd=3)
        e7_edit.grid(row=7, column=1, padx=5, pady=5)
        for record in dbresult:
            e1_edit.insert(0,record[0])
            e2_edit.insert(0, record[1])
            e3_edit.insert(0, record[2])
            e4_edit.insert(0, record[3])
            e5_edit.insert(0, record[4])
            e6_edit.insert(0, record[5])
            e7_edit.insert(0, record[6])
            # save the changes
        save_button = Button(upd, text="Save", command=save)
        save_button.grid(row=8, column=0, columnspan=2)
        # commit changes
        mydb.commit()
        mydb.close()


# create a  save function
def save():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Student')
    my_cursor = mydb.cursor()

    sql_command="""UPDATE Registration SET First_Name= %s, Last_Name= %s, Roll_No=%s, Email_ID=%s, Mobile_Number=%s, Blood_Group=%s, City=%s WHERE ID=%s"""
    First_Name=e1_edit.get()
    Last_Name=e2_edit.get()
    Roll_No=e3_edit.get()
    Email_ID=e4_edit.get()
    Mobile_Number=e5_edit.get()
    Blood_Group=e6_edit.get()
    City=e7_edit.get()
    ID=entry_delete.get()
    Inputs=(First_Name,Last_Name,Roll_No,Email_ID,Mobile_Number,Blood_Group,City,ID)
    my_cursor.execute(sql_command,Inputs)
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Update", "Succesfully Updated")
    upd.destroy()
def Query():
    Quer=Tk()
    Quer.title("Query")
    Quer.geometry("550x200")
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Student')
    my_cursor = mydb.cursor()
    my_cursor.execute("select * from Registration")

    records = my_cursor.fetchall()
    print_records = ''
   # loop for records
    for record in records:
        print_records += str(record) + "\n"
    query_label = Label(Quer, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    # pandas data


    df = pd.read_sql_query("SELECT * FROM Registration", mydb)
    df.head()
    print(df)
    # commit changes
    mydb.commit()
    mydb.close()
def Export():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Student')
    df = pd.read_sql_query("SELECT * FROM Registration", mydb)
    df1=pd.DataFrame(df)
    a=tkvar.get()
    if a == "Csv":
        df1.to_csv('C:/Nisanth Files/file1.csv')
        messagebox.showinfo("Exported", "Succesfully Exported")
    elif a == "Text":
        df1.to_csv('C:/Nisanth Files/file1.txt')
        messagebox.showinfo("Exported", "Succesfully Exported")
    elif a == "Excel":
        with pd.ExcelWriter('C:/Nisanth Files/file1.xlsx') as writer:
            df1.to_excel(writer, sheet_name='Sheet_name_3')
        messagebox.showinfo("Exported", "Succesfully Exported")
#Label Creation
f1=Label(root,text="First Name",font=("Pangolin",10),pady=5,anchor="center")
f1.grid(row=0,column=0,pady=10)
f2 = Label(root, text="Last Name", font=("Pangolin", 10), pady=5, anchor="center")
f2.grid(row=1, column=0,pady=5)
f3 = Label(root, text="Roll No", font=("Pangolin", 10), pady=5, anchor="center")
f3.grid(row=2, column=0,pady=5)
f4 = Label(root, text="Email ID", font=("Pangolin", 10), pady=5, anchor="center")
f4.grid(row=3, column=0,pady=5)
f5 = Label(root, text="Mobile Number", font=("Pangolin", 10), pady=5, anchor="center")
f5.grid(row=4, column=0,pady=5)
f6 = Label(root, text="Blood Group", font=("Pangolin", 10), pady=5, anchor="center")
f6.grid(row=5, column=0,pady=5)
f7 = Label(root, text="City", font=("Pangolin", 10), pady=5, anchor="center")
f7.grid(row=6, column=0,pady=5)
label_delete=Label(root,text="Select ID",font=("Pangolin",10),pady=5,anchor="center")
label_delete.grid(row=8, column=0, pady=10)


#Entry creation
e1=Entry(root,width=30,relief="flat",bd=3)
e1.grid(row=0,column=1,padx=5,pady=5)
e2 = Entry(root, width=30, relief="flat", bd=3)
e2.grid(row=1, column=1, padx=5,pady=5)
e3 = Entry(root, width=30, relief="flat", bd=3)
e3.grid(row=2, column=1, padx=5,pady=5)
e4 = Entry(root, width=30, relief="flat", bd=3)
e4.grid(row=3, column=1, padx=5,pady=5)
e5 = Entry(root, width=30, relief="flat", bd=3)
e5.grid(row=4, column=1, padx=5,pady=5)
e6 = Entry(root, width=30, relief="flat", bd=3)
e6.grid(row=5, column=1, padx=5,pady=5)
e7 = Entry(root, width=30, relief="flat", bd=3)
e7.grid(row=6, column=1, padx=5,pady=5)
entry_delete = Entry(root, width=30, relief="flat", bd=3)
entry_delete.grid(row=8, column=1, padx=5, pady=5)

#Button Creation

submit=Button(root,width=22,text="Submit",command=Submit)
submit.grid(row=7,column=0,columnspan=2,pady=10)
delete=Button(root,width=22,text="Delete",command=Delete)
delete.grid(row=9,column=0,columnspan=2,pady=10)
update=Button(root,width=22,text="Update",command=Update)
update.grid(row=10,column=0,padx=5,pady=10)
Query=Button(root,width=22,text="Query",command=Query)
Query.grid(row=10,column=1,pady=10,)
Export_button=Button(root,width=22,text="Export",command=Export)
Export_button.grid(row=11,column=1,pady=10)
# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Csv','Text','Excel'}
tkvar.set('Csv')

popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.grid(row = 11, column =0)

root.mainloop()
