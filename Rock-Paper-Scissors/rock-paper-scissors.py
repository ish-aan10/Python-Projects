import tkinter as tk
import random
from PIL import ImageTk,Image

root = tk.Tk()
rock_image = ImageTk.PhotoImage(Image.open(r"D:\Core\projects-codsoft\codsoft_taskno-4_ROCK-PAPER-SCISSORS_GAME\images\rock.png"))
paper_image = ImageTk.PhotoImage(Image.open(r"D:\Core\projects-codsoft\codsoft_taskno-4_ROCK-PAPER-SCISSORS_GAME\images\paper.png"))
scissor_image = ImageTk.PhotoImage(Image.open(r"D:\Core\projects-codsoft\codsoft_taskno-4_ROCK-PAPER-SCISSORS_GAME\images\scissors.png"))
userScore = 0
compScore = 0

def reset_game():
    global userScore, compScore
    userScore = 0
    compScore = 0
    score.config(text=f"{userScore} - {compScore}")

def determine_winner(user, comp):
    global userScore, compScore
    if user == comp:
        resultLabel.config(text="TIE!")
        return
    if user == "rock":
        if comp == "paper":
            compScore += 1
        else:
            userScore += 1
    elif user == "paper":
        if comp == "scissor":
            compScore += 1
        else:
            userScore += 1
    elif user == "scissor":
        if comp == "rock":
            compScore += 1
        else:
            userScore += 1

def comp_choice():
    choices = ['rock','paper','scissor']
    return random.choice(choices)

def user_choice(choice):
    resultLabel.config(text="")
    comp = comp_choice()
    determine_winner(user=choice,comp=comp)
    
    user_choice_image_label.config(image=globals()[f"{choice}_image"])
    comp_choice_image_label.config(image=globals()[f"{comp}_image"])
    score.config(text=f"{userScore} - {compScore}")

root.title("Rock-Paper-Scissor")
canvas = tk.Canvas(root,width=640,height=480,bg="#232324",border=0)
canvas.pack()

label = tk.Label(root,text="Rock-Paper-Scissor",font=("Bahnschrift",42,"bold"),fg="silver",bg="#232324")
canvas.create_window(320,60,window=label)

resultLabel = tk.Label(root,text="",bg="#232324",fg="red",font=("Bahnschrift",18,"bold"))
canvas.create_window(320,140,window=resultLabel)

score = tk.Label(root,text=f"{userScore} - {compScore}",fg="red",bg="#232324",font=("Bahnschrift",24,"bold"))
canvas.create_window(320,200,window=score)

rockButton = tk.Button(root,text="ROCK",width=8,fg="black",bg="gold",activebackground="gold",activeforeground="black",font=("Bahnschrift",16,"bold"),command=lambda: user_choice('rock'))
canvas.create_window(180,320,window=rockButton)
paperButton = tk.Button(root,text="PAPER",width=8,fg="black",bg="gold",activebackground="gold",activeforeground="black",font=("Bahnschrift",16,"bold"),command=lambda: user_choice('paper'))
canvas.create_window(320,320,window=paperButton)
scissorButton = tk.Button(root,text="SCISSOR",width=8,fg="black",bg="gold",activebackground="gold",activeforeground="black",font=("Bahnschrift",16,"bold"),command=lambda: user_choice('scissor'))
canvas.create_window(460,320,window=scissorButton)

user_choice_image_label = tk.Label(root,bg="#232324")
canvas.create_window(160,200,window=user_choice_image_label)
comp_choice_image_label = tk.Label(root,bg="#232324")
canvas.create_window(480,200,window=comp_choice_image_label)

reset = tk.Button(root,text="RESET",width=8,fg="black",bg="silver",activebackground="silver",activeforeground="black",font=("Bahnschrift",16,"bold"),command=lambda: reset_game())
canvas.create_window(320,370,window=reset)

root.mainloop()