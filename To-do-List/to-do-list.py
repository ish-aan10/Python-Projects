import tkinter as tk

root = tk.Tk()
custom_font = ("Bahnschrift",12)
tasks = []
file_path = r"D:\Core\projects-codsoft\To-do-List\tasks.txt"

def update_listview():
    task_listbox.delete(0,tk.END) 
    x = "\u25B6"
    for task in tasks:
        task_listbox.insert(tk.END,f'{x} {task}')

def delete_task():
    select = task_listbox.curselection()
    if select:
        index = select[0]
        tasks.pop(index)
        update_listview()

def on_exit():
    save_tasks()
    root.destroy()
        
def load_tasks_on_start():
    try:
        with open(file_path,'r') as file:
            tasks.extend(file.read().splitlines())
        print(f"Tasks loaded from {file_path}")
        update_listview()
    except FileNotFoundError:
        print("No tasks file found.")

def save_tasks():
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Tasks saved to {file_path}.")
    
def add_task(task):
    if task:
        tasks.append(task)
        task_entry.delete(0,tk.END)  
        update_listview() 

def main_window():
    main_frame.grid(row=0,column=0,padx=30,pady=30)
    
    label = tk.Label(main_frame,text="To-Do List",bg="#1c1c1c",fg="white",font=(("Berlin Sans FB",24)))
    label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    
    task_label = tk.Label(main_frame,text="Task:",bg="#1c1c1c",fg="white",font=custom_font)
    task_label.grid(row=2,column=0,padx=5,pady=5,sticky='W')
    
    task_entry.grid(in_=main_frame,row=3,column=0,padx=5,pady=5,sticky='nsew')
    
    task_listbox.grid(in_=main_frame,row=2,column=1,rowspan=8,columnspan=2,padx=15,pady=15)
    
    add_button.config(command=lambda: add_task(task_entry.get()))
    delete_button.config(command=lambda: delete_task())
    exit_button.config(command=lambda: on_exit())
    
    add_button.grid(in_=main_frame,row=4,column=0,padx=5,pady=5,sticky='nsew')
    delete_button.grid(in_=main_frame,row=5,column=0,padx=5,pady=5,sticky='nsew')
    exit_button.grid(in_=main_frame,row=6,column=0,padx=5,pady=5,sticky='nsew')
    

root.geometry("625x620")
root.title("To-Do List Application")
root.config(bg="#232324")

main_frame = tk.Frame(root,bg="#1c1c1c")

task_entry = tk.Entry(bg="#1c1c1c",fg="white",font=custom_font,insertbackground="white")

task_listbox = tk.Listbox(width=28,height=18,bg="#e9dab9",fg="black",border=0,font=("Bahnschrift",16))

add_button = tk.Button(text="ADD TASK",bg="#1c1c1c",fg="white",activebackground="#1c1c1c",activeforeground="white")
delete_button = tk.Button(text="DELETE TASK",bg="#1c1c1c",fg="white",activebackground="#1c1c1c",activeforeground="white")
exit_button = tk.Button(text="EXIT",bg="#1c1c1c",fg="white",activebackground="#1c1c1c",activeforeground="white")

load_tasks_on_start()

main_window()

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()