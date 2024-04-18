import tkinter as tk
from tkinter import ttk

root = tk.Tk()
contacts = {}

def delContact():
    select = contactList.curselection()
    if select:
        index = select[0]
        name = contactList.get(index)[2:]
        contacts.pop(name, None)
        contactList.delete(index)
        
        for item in tree.get_children():
            values = tree.item(item, "values")
            if values[0] == name:
                tree.delete(item)
                break
            
    updateList()

def updateList():
    contactList.delete(0,tk.END)
    x = "\u25B6"
    for name in contacts:
        contactList.insert(tk.END,f'{x} {name}')
    for item in tree.get_children():
        tree.delete(item)
    for name, details in contacts.items():
        phone, email = details
        tree.insert("","end",values=(name,phone,email))
        
def onExit():
    root.destroy()

def clearError():
    errorLbl.config(text="")

def update_contact(event=None):
    selected_item = contactList.curselection()
    if selected_item:
        index = selected_item[0]
        name = contactList.get(index)[2:]
        if name in contacts:
            fname, lname = name.split()
            phone, email = contacts[name]
            fname_entry.delete(0, tk.END)
            lname_entry.delete(0, tk.END)
            number_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            fname_entry.insert(0, fname)
            lname_entry.insert(0, lname)
            number_entry.insert(0, phone)
            email_entry.insert(0, email)
            update_window()
    else:
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        update_window()

def updateContact(fname,lname,num,email):
    full_name = f"{fname} {lname}"
    selected_item = contactList.curselection()

    if selected_item:
        index = selected_item[0]
        old_name = contactList.get(index)[2:]
        if old_name in contacts:
            contacts.pop(old_name)
            for item in tree.get_children():
                values = tree.item(item, "values")
                if values[0] == old_name:
                    tree.delete(item)
                    break

    contacts[full_name] = (num, email)
    updateList()
    backFunc()

def addContact(fname,lname,num,email):
    if(fname == "" or lname == "" or num == "" or email == ""):
        errorLbl.config(text="All fields must be filled!")
        root.after(3000, clearError)
        return
    full_name = f"{fname} {lname}"
    contacts[full_name] = (num, email)
    fname_entry.delete(0,tk.END)
    lname_entry.delete(0,tk.END)
    number_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    updateList()

def backFunc():
    if add_canvas.winfo_viewable():
        add_canvas.grid_forget()
    if update_canvas.winfo_viewable():
        update_canvas.grid_forget()
    main_window()    

def update_window():
    if main_canvas.winfo_viewable():
        main_canvas.grid_forget()
    update_canvas.grid(row=0,column=0)
    
    label.config(text="Update Contact")
    update_canvas.create_window(240,30,window=label)
    
    update_canvas.create_window(15,80,window=fname_label,anchor="w")
    update_canvas.create_window(15,110,window=lname_label,anchor="w")
    update_canvas.create_window(15,140,window=number_label,anchor="w")
    update_canvas.create_window(15,170,window=email_label,anchor="w")
    
    update_canvas.create_window(140,80,window=fname_entry,anchor="w")
    update_canvas.create_window(140,110,window=lname_entry,anchor="w")
    update_canvas.create_window(140,140,window=number_entry,anchor="w")
    update_canvas.create_window(140,170,window=email_entry,anchor="w")
    
    update_button.config(command=lambda: updateContact(fname_entry.get(),lname_entry.get(),number_entry.get(),email_entry.get()))
    update_canvas.create_window(160,220,window=update_button)
    back_button.config(command=lambda: backFunc())
    update_canvas.create_window(320,220,window=back_button)
    
    update_canvas.create_window(240,350,window=tree)

def add_window():
    if main_canvas.winfo_viewable():
        main_canvas.grid_forget()
    fname_entry.delete(0,tk.END)
    lname_entry.delete(0,tk.END)
    number_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    add_canvas.grid(row=0,column=0)
    
    label.config(text="Add Contact")
    add_canvas.create_window(240,30,window=label)
    
    add_canvas.create_window(15,80,window=fname_label,anchor="w")
    add_canvas.create_window(15,110,window=lname_label,anchor="w")
    add_canvas.create_window(15,140,window=number_label,anchor="w")
    add_canvas.create_window(15,170,window=email_label,anchor="w")
    
    add_canvas.create_window(240,210,window=errorLbl)
    
    add_canvas.create_window(140,80,window=fname_entry,anchor="w")
    add_canvas.create_window(140,110,window=lname_entry,anchor="w")
    add_canvas.create_window(140,140,window=number_entry,anchor="w")
    add_canvas.create_window(140,170,window=email_entry,anchor="w")
    
    add_button.config(command=lambda: addContact(fname_entry.get(),lname_entry.get(),number_entry.get(),email_entry.get()))
    add_canvas.create_window(160,250,window=add_button)
    back_button.config(command=lambda: backFunc())
    add_canvas.create_window(320,250,window=back_button)
    
    add_canvas.create_window(240,380,window=tree)
    
def main_window():
    main_canvas.grid(row=0,column=0)
    
    label.config(text="Contact Book")
    main_canvas.create_window(240,30,window=label)
    
    main_canvas.create_window(160,260,window=contactList)
    contactList.bind("<Double-1>", lambda event: update_contact())
    
    add_button.config(command=lambda: add_window())
    main_canvas.create_window(400,80,window=add_button)
    update_button.config(command=lambda: update_window())
    main_canvas.create_window(400,130,window=update_button)
    delete_button.config(command=lambda: delContact())
    main_canvas.create_window(400,180,window=delete_button)
    exit_button.config(command=lambda: onExit())
    main_canvas.create_window(400,430,window=exit_button)
    
root.title("ContactBook")

main_canvas = tk.Canvas(root,width=480,height=480)
add_canvas = tk.Canvas(root,width=480,height=480)
update_canvas = tk.Canvas(root,width=480,height=480)

label = tk.Label(root,text="",font=("Berlin Sans FB",28))
errorLbl = tk.Label(root,text="",font=("Bahnschrift",12))

contactList = tk.Listbox(root,width=50,height=25)

add_button = tk.Button(root,text="Add",font=("Bahnschrift",16),width=10,bg="green",activebackground="green")
update_button = tk.Button(root,text="Update",font=("Bahnschrift",16),width=10,bg="yellow",activebackground="yellow")
delete_button = tk.Button(root,text="Delete",font=("Bahnschrift",16),width=10,bg="orange",activebackground="orange")
exit_button = tk.Button(root,text="Exit",font=("Bahnschrift",16),width=10,bg="red",activebackground="red")
back_button = tk.Button(root,text="Back",font=("Bahnschrift",16),width=10,bg="blue",activebackground="blue")

fname_label = tk.Label(root,text="First Name:",font=("Bahnschrift",12))
lname_label = tk.Label(root,text="Last Name:",font=("Bahnschrift",12))
number_label = tk.Label(root,text="Phone Number:",font=("Bahnschrift",12))
email_label = tk.Label(root,text="E-Mail:",font=("Bahnschrift",12))

fname_entry = tk.Entry(root,font=("Bahnschrift",12),width=35)
lname_entry = tk.Entry(root,font=("Bahnschrift",12),width=35)
number_entry = tk.Entry(root,font=("Bahnschrift",12),width=35)
email_entry = tk.Entry(root,font=("Bahnschrift",12),width=35)

tree = ttk.Treeview(columns=("Name","Phone Number","E-mail"),show="headings",height=8)
tree.heading("Name",text="Name")
tree.heading("Phone Number",text="Phone Number")
tree.heading("E-mail",text="E-mail")

tree.column("Name",width=150)
tree.column("Phone Number",width=100)

main_window()
root.mainloop()