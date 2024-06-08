from tkinter import *
import ast                      #  Abstract Syntax Tree : Its has a bunch of methods
                                #                         we can pass our expression 
                                #                         and evaluate it

root = Tk()
i = 0
button_font = ('Berlin Sans FB', 14)


def undo():
    entire_string = entry.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        entry.insert(0,new_string)
    else:
        clear_all()
        entry.insert(0,"")

def calculate():
    entire_string = entry.get()
    try:
        node = ast.parse(entire_string,mode="eval")
        result = eval(compile(node,'<string>','eval'))
        clear_all()
        entry.insert(0,result)
    except Exception as e:
        clear_all()
        entry.insert(0,"ERROR")

def clear_all():
    entry.delete(0,END)

def get_number(num):
    global i
    entry.insert(i,num)
    i+=1

def get_operations(exp):
    global i
    length = len(exp)
    entry.insert(i,exp)
    i+=length

def main_window():
    
    empty_frame.grid(
        in_=main_frame,
        row=0,
        column=0
    )
    entry.grid(
        in_=main_frame,
        row=1,
        column=0,
        columnspan=6,
        padx=4,
        pady=4
    )
    
    number = [1,2,3,4,5,6,7,8,9]
    
    counter = 0
    
    for x in range(3):
        for y in range(3):
            button_text = number[counter]
            num_button = Button(
                main_frame,
                text=button_text,
                bg="#232324",
                fg="white",
                height=2,
                font=button_font,
                command=lambda text=button_text:get_number(text)
            )
            num_button.grid(
                row=x+2,
                column=y,
                padx=2,
                pady=2,
                sticky="nsew"
            )
            counter+=1
    
    zero_button = Button(
        main_frame,
        text="0",
        bg="#232324",
        fg="white",
        height=2,
        font=button_font,
        command=lambda :get_number(0)
    )
    zero_button.grid(
        row=5,
        column=1,
        padx=2,
        pady=2,
        sticky="nsew"
    )
    AC_button = Button(
        main_frame,
        text="AC",
        bg="#232324",
        fg="white",
        height=2,
        font=button_font,
        command=clear_all
    )
    AC_button.grid(
        row=5,
        column=0,
        padx=2,
        pady=2,
        sticky="nsew"
    )
    Equal = Button(
        main_frame,
        text="=",
        bg="#232324",
        fg="white",
        height=2,
        font=button_font,
        command=calculate
    )
    Equal.grid(
        row=5,
        column=2,
        padx=2,
        pady=2,
        sticky="nsew"
    )
    delete_button = Button(
        main_frame,
        text="DEL",
        bg="#232324",
        fg="white",
        height=2,
        font=button_font,
        command=lambda :undo()
    )
    delete_button.grid(
        row=5,
        column=4,
        padx=2,
        pady=2,
        sticky="nsew"
    )
    
    count = 0 
    
    operations = ['+','-',"*","/","*3.14","%","(","**",")","**2"]
    
    for x in range(4):
        for y in range(3):
            if count<len(operations):
                operation_text = operations[count]
                button = Button(
                    main_frame,
                    text=operation_text,
                    bg="#232324",
                    height=2,
                    fg="white",
                    font=button_font,
                    command=lambda text=operation_text:get_operations(text)
                )
                button.grid(
                    row=x+2,
                    column=y+3,
                    padx=2,
                    pady=2,
                    sticky="nsew"
                )
                count+=1
                
        
root.config(bg="#232324")
root.title("PyCalc")

main_frame = Frame(
    root,
    bg="#232324"
)
main_frame.grid(
    row=0,
    column=0
)
empty_frame = Frame(
    bg="#232324"
)

entry = Entry(
    bg="#232324",
    fg="white",
    width=20,
    justify=RIGHT,
    font=('MS Sans Serif Regular',24)
)

main_window()
root.mainloop()