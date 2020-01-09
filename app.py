from tkinter import*
from tkinter import messagebox
import os
from db import Database
db=Database('store.db')

def populatelist():
    parts_list.delete(0,END)
    for item in db.fetch():
        parts_list.insert(END, item)
    # print('List populated')

def changetheme()

def add_item():
    if partText.get() == '' or customerText.get() == '' or retailerText.get()=='' or priceText.get() == '':
        messagebox.showerror('REQUIRED FIELDS','Please fill in all forms to add ')
        return
    db.insert(partText.get(),customerText.get(),retailerText.get(),priceText.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(partText.get(),customerText.get(),retailerText.get(),priceText.get()))
    populatelist()
    
def clearInput():
    part_entry.delete(0,END)
    customer_entry.delete(0,END)
    retailer_entry.delete(0,END)
    price_entry.delete(0,END)

def selectItem(event):
    try:
        global  selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index )

        part_entry.delete(0,END)
        part_entry.insert(END,selected_item[1])
        retailer_entry.delete(0,END)
        retailer_entry.insert(END,selected_item[2])
        customer_entry.delete(0,END)
        customer_entry.insert(END,selected_item[3])
        price_entry.delete(0,END)
        price_entry.insert(END,selected_item[4])
    except:
        pass


def removebutton():
    db.remove(selected_item[0])
    populatelist()

def updateButton():
    db.update(selected_item[0],partText.get(),customerText.get(),retailerText.get(),priceText.get())
    parts_list.delete(0,END)
    parts_list.insert(selected_item[0])
    populatelist()

app=Tk()

partText=StringVar()
part_label=Label(app,text='Part Name',font=('bold',16),pady=20)
part_label.grid(row=0,column=0)
part_entry=Entry(app,textvariable=partText)
part_entry.grid(row=0,column=1)

# retailer part
retailerText=StringVar()
retailer=Label(app,text='Retailer',font=('bold',16),pady=20)
retailer.grid(row=1,column=0)
retailer_entry=Entry(app,textvariable=retailerText)
retailer_entry.grid(row=1,column=1)

# Customer
customerText=StringVar()
customer=Label(app,text='Customer',font=('bold',16),pady=20,padx=10)
customer.grid(row=0,column=2,sticky=W)
customer_entry=Entry(app,textvariable=customerText)
customer_entry.grid(row=0,column=3, sticky=W)

# price
priceText=StringVar()
price=Label(app,text='Price',font=('bold',16),padx=10)
price.grid(row=1,column=2,sticky=W)
price_entry=Entry(app,textvariable=priceText)
price_entry.grid(row=1,column=3,sticky=W)

# Listbox
parts_list=Listbox(app,height=20,width=70,border=0)
parts_list.grid(row=3,column=0, columnspan=3,rowspan=6,pady=25,padx=10)
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
parts_list.bind('<<ListboxSelect>>',selectItem)

# utilities
add_buttnon=Button(app,text='ADD ITEM',width=15,command=add_item)
add_buttnon.grid(row=2,column=0,pady=20)
remove_button=Button(app,text='REMOVE ITEM',width=15,command=removebutton)
remove_button.grid(row=2,column=1)
update_button=Button(app,text='UPDATE',width=15,command=updateButton)
update_button.grid(row=2,column=2)
clear_input=Button(app,text='CLEAR INPUT',width=15,command=clearInput)
clear_input.grid(row=2,column=3)

#Dark theme
darkbtn=Button(app,text='Dark theme',command=changetheme)
darkbtn.grid(row=6,column=0)


app.title('Part Manager')
app.geometry('900x600')
populatelist()
app.mainloop()