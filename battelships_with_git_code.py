from random import randint,choice
import random #mo<na go pominac bo nie byl uzyty
import time
print("Let the Battleships game begin!")
player_1 = input("What's your name? ")
player_2 = input("What's your name? ")
players = [player_1, player_2]
total_turns= 0
Rows = 9
Columns = 9
ship_x=randint(0,10)
ship_y=randint(0,10)
print(ship_x)
print(ship_y)
board = []
#board[ship_x][ship_y] = "+"


def random_player(players):
    return choice(players)

if random_player(players) == player_1:
        print(player_1, " starts the game")
else:
        print(player_2, " starts the game")
time.sleep(4)

def print_board(board):
    for row in board:
        print(" ".join(row))
        while (Rows > 10) or (Columns > 10) or (Rows <= 0) or (Columns <= 0):
            Rows = int(9)
            Columns = int(9)
    print()

def create_grid(Rows, Columns): #Creates the 2D Data Grid
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid.append(row)
    return grid

def display_grid(Rows, Columns): #Prints the labels for the grid
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
        print(number + 1, '| ' + ' | '.join(row) + ' |')

def guess_x():#gracz wybiera pole na planszy przeciwnika 
    guess_x = 999   #ta liczba jest po to zeby na starcie wchodzic do while'a *magic string*, mozna tez to zrobic rozmiar planszy +1
    while guess_x not in range(0,11):
        try:  #try and except wylapuje bledy jakby ktos np wpisal litery zamiast liczb
            guess_x = int(input("enter position x (row): "))
        except: 
            pass #dodac typerror dla usera
        if guess_x not in range(0,11):
            print ("number outside of range")

def guess_y():
    guess_y = 999
    while guess_y not in range(0,11):
        try:
            guess_y = int(input("enter position y (column): "))
        except: 
            pass
        if guess_y not in range(0,11):
            print ("number outside of range")


def hitship():
    while ship_x == guess_x and ship_y == guess_y:
        print ("Trafiony, masz jeszcze jeden ruch")
        board[ship_x][ship_y] = "X"
        print_board(board)
    try:
        guess_y = int(input("enter position x (row): "))
        guess_x = int(input("enter position y (column): "))
    except:
        pass
    

#elif guess_x != ship_x and guess_y != ship_y:
# print('Pudlo! Nie masz wiecej ruchow') 



def update_gridHit(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = 'O'

def update_gridMiss(grid, GuessRow, GuessColumn):
    grid[GuessRow-1][GuessColumn-1] = 'X'

print("Teraz ruch gracza drugiego!")

def player_turns(total_turns):
    if total_turns %2 == 0:
        total_turns +=1
        return player_1
    else:
        return player_2

#Gameplay
print_board(board)
grid = create_grid(Rows,Columns)
display_grid(Rows, Columns)
guess_x()
guess_y()
hitship()
player_turns()




