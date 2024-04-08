import tkinter as tk
import random
import string

root = tk.Tk()

def error_label_text():
        error_label.config(text="")

def generate_password(uname, length):
    listview.delete(0, tk.END)
    if(uname == "" or length == ""):
        error_label.config(text="All fields must be filled")
        root.after(3000, error_label_text)
        return
    
    length = int(length)
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    characters = lowercase_letters + uppercase_letters + digits + special_characters
    password = uname
    
    remaining_length = length - len(uname)
    for _ in range(remaining_length):
        password += random.choice(characters)
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    listview.insert(tk.END, password)        

root.title("Password Generator")
root.config(bg="#232324")

canvas = tk.Canvas(root,bg="beige",width=400,height=370)
canvas.grid(row=0,column=0,padx=20,pady=20)

label = tk.Label(root,text="Password Generator",bg="beige",font=("Berlin Sans FB",30))
canvas.create_window(200,40, window=label)

uname = tk.Label(root,text="Username:",bg="beige",font=("Bahnschrift",14))
canvas.create_window(200,100, window=uname)
uname_entry = tk.Entry(root,bg="#1c1c1c",fg="white",insertbackground="white",width=30,font=("Bahnschrift",12),justify='center')
canvas.create_window(200,130, window=uname_entry)

length_label = tk.Label(root,text="Enter Length:",bg="beige",font=("Bahnschrift",14))
length_entry = tk.Entry(root,bg="#1c1c1c",fg="white",insertbackground="white",width=5,font=("Bahnschrift",12),justify='center')
canvas.create_window(170,170, window=length_label)
canvas.create_window(270,170, window=length_entry)

error_label = tk.Label(root,text="",bg="beige",fg="red",font=("Bahnschrift",14))
canvas.create_window(200,200, window=error_label)

generate_button = tk.Button(root,text="Generate",bg="lightgrey",activebackground="grey",width=10,font=("Bahnschrift",14),command=lambda: generate_password(uname_entry.get(),length_entry.get()))
canvas.create_window(200,240, window=generate_button)

listview = tk.Listbox(root,width=35,height=2,borderwidth=2,font=("Bahnschrift",14),justify='center')
canvas.create_window(200,300, window=listview)

root.mainloop()