from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]


def computer_wins():
    global computer_score, player_score
    computer_score += 1
    winner_label.config(text="Computer Won!!!")
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))

def player_wins():
    global player_score, computer_score
    player_score += 1
    winner_label.config(text = "PLAYER wins")
    player_score_label.config(text='player Score : ' + str(player_score))
    computer_score_label.config(text='computer Score : ' + str(computer_score))

def tie():
    global player_score, computer_score
    winner_label.config(text = "draw")
    player_score_label.config(text='player Score : ' + str(player_score))
    computer_score_label.config(text='computer Score : ' + str(computer_score))


def player_choice(player_input):
    global player_score,computer_score
    computer_input = get_computer_choice()
    player_choice_label.config(text = "you selected - " + player_input[0])
    computer_choice_label.config(text = "computer selected - " + computer_input[0])

    if (player_input == computer_input):
        tie ()
    
    if (player_input[1] == 0):
        if (computer_input[1] == 1):
            computer_wins()

        
        elif (computer_input[1] == 2):
            player_wins()

    elif (player_input[1] == 1):
        if (computer_input[1] == 0):
          player_wins()

        
        elif (computer_input[1] == 2):
         computer_wins()

    elif (player_input[1] == 2):
        if (computer_input[1] == 0):
          computer_wins()


        elif (computer_input[1] == 1):
         player_wins()

def get_computer_choice ():
   return random.choice(options)

main= Tk()
main.geometry("700x700")
main.title("RPS")
game_font = font.Font(size = 12)

game_title = Label(text= "Rock Paper Scissors", font= game_font, fg = "black")
game_title.pack()

winner_label = Label(text = "lets start", fg = "green", font = game_font, pady=8)
winner_label.pack()

input_frame = Frame(main)
input_frame.pack()

player_options = Label(input_frame, text = "your options are:  ", font = game_font, fg = "blue")
player_options.grid(row = 0, column=0, pady=8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)
paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'silver', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)
scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)


#Displaying Score and players choise
score_label = Label(input_frame, text = 'Score : ', font = game_font, fg = 'grey')
score_label.grid(row = 2, column = 0)
player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = game_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)
player_score_label = Label(input_frame, text = 'Your Score : -', font = game_font)
player_score_label.grid(row = 3, column = 2, pady = 5)
computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = game_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)
computer_score_label = Label(input_frame, text = 'Computer Score : -', font = game_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

main.mainloop()



