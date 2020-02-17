# import pygame
from tkinter import *
from tkinter import ttk
from random import randint
from PIL import Image, ImageTk


class RpsGame(Frame):

    def __init__(self):
        root = Tk()
        # set up the window and widges.
        Frame.__init__(self)
        self.master.title("Rock Paper Scissors Game")
        self.master.resizable(False, False)#not able to resize the window size
        self.grid()

        # computer player shuffle image
        self.image = PhotoImage(file="./images/rock.png")
        self.imageLabel = Label(self, image=self.image)
        self.imageLabel.grid()
        self.textLabel = Label(self, text="Choose option to play game!")
        self.textLabel.grid()

        self.mid = Frame(root)
        self.mid.grid(pady=30, padx=30)

        ## player option buttons
        r_img = Image.open("./images/rock.png")
        r_img = r_img.resize((100, 100), Image.ANTIALIAS)
        self.r_img = ImageTk.PhotoImage(r_img)
        self.r_btn = Button(self.mid, image=self.r_img, command="rock")
        self.r_btn.grid(row=0, column=0, padx=10)


        p_img = Image.open("./images/paper.png")
        p_img = p_img.resize((100, 100), Image.ANTIALIAS)
        self.p_img = ImageTk.PhotoImage(p_img)
        self.p_btn = Button(self.mid, image=self.p_img, command="paper")
        self.p_btn.grid(row=0, column=1, padx=10)

        s_img = Image.open("./images/scissors.png")
        s_img = s_img.resize((100, 100), Image.ANTIALIAS)
        self.s_img = ImageTk.PhotoImage(s_img)
        self.s_btn = Button(self.mid, image=self.s_img, command="scissors")
        self.s_btn.grid(row=0, column=2, padx=10)

    def new_img():
        #pick a new number
        num = random.randit(0,2)
        #assigning img name to numbers
        if num==0:
            img = "rock"
        elif num==1:
            img="paper"
        elif num==2:
            img="scissors"
        #return the imame name
        computerimg = './images/'+img+'.png'

        return computerimg
        
    def update_the_image():
        computerimg = new_img()
        updated_picture = ImageTk.PhotoImage(Image.open(myimg))
        w.configure(image = updated_picture)

#game logic to add after wards 
def game_logic():
    # create a list of play options
    play_options = ["rock", "paper", "scissors"]

    #assign a random play to the computer
    computer = play_options[randint(0,2)]

    #set player to False
    player = False

    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors? \n").lower()
        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
                break
            else:
                print("You win!", player, "smashes", computer)
                break
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
                break
            else:
                print("You win!", player, "covers", computer)
                break
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
                break
            else:
                print("You win!", player, "cut", computer)
                break
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player == False
        computer = play_options[randint(0,2)]

if __name__ == "__main__":
    RpsGame().mainloop()
    # game_logic()
