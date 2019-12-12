from random import randint,choice
import random #mozna go pominac bo nie byl uzyty A JEDNAK
import time
print("Let the Battleships game begin!")
player_one = input("What's your name? ")
player_two = input("What's your name? ")
players = [player_one, player_two]
total_turns= 10
Rows = 9
Columns = 9
ship_x=randint(0,9)
ship_y=randint(0,9)
player_one_grid=[]
player_two_grid=[]
player_one_shots=[]
player_two_shots=[]

def random_player(players):
    return choice(players)
if random_player(players) == player_one:
        print(player_one, " starts the game")
else:
        print(player_two, " starts the game")
time.sleep(4)

def create_grid(Rows, Columns): #Creates the 2D Data Grid
    grid = []
    for row in range(Rows):
        row = []
        for col in range(Columns):
            row.append(' ')
        grid.append(row)
    return grid

def display_grid(Rows, Columns, grid): #Prints the labels for the grid
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
        print(number + 1, '| ' + ' | '.join(row) + ' |' )

def guess_x():#gracz wybiera pole na planszy przeciwnika
    global guess_x
    guess_x = 999   #ta liczba jest po to zeby na starcie wchodzic do while'a *magic string*, mozna tez to zrobic rozmiar planszy +1
    while guess_x not in range(0,9):
        try:  #try and except wylapuje bledy jakby ktos np wpisal litery zamiast liczb
            guess_x = (int(input("enter position x (row): "))-1)
        except:
            pass #dodac typerror dla usera
        if guess_x not in range(0,9):
            print ("number outside of range")

def guess_y():
    global guess_y
    guess_y = 999
    while guess_y not in range(0,9):
        try:
            guess_y = (int(input("enter position y (column): "))-1)
        except:
            pass
        if guess_y not in range(0,9):
            print ("number outside of range")

def place_ships(empty_grid):
    counter = 0 #musimy wiedziec ile statkow juz jest rozmieszczonych
    while counter < 4 :
        x=random.randrange(9)
        y=random.randrange(9)
        if empty_grid[x][y] == " ": #sprawdza czy nie jest puste pole, jak nie jest puste to znaczy ze jest zajete
            counter+=1
            empty_grid[x][y]='+'
    return empty_grid
    #it's taken
    #placing

def player_turns(total_turns): #Przepisać!
    #todo Checks which player shoots, check those shots on enemies grid
    if float(total_turns) %2 == 0:
        return player_one
    else:
        return player_two
    total_turns +=1
    print("Teraz ruch gracza drugiego!")

def shot(x,y,shot_grid,enemy_grid):
    if enemy_grid[x][y] != " ":
        print("HIT!")
        shot_grid[x][y] = "#"
        enemy_grid[x][y] = "#"
    else:
        print("MISS")
        shot_grid[x][y] ="X"
        
        #todo check if all ships are sunken!


#Gameplay

player_one_grid  = create_grid(9,9)
player_two_grid = create_grid(9,9) #dwie plansze w pamieci
player_one_shots = create_grid(9,9)
player_two_shots = create_grid(9,9)
player_one_grid=place_ships(player_one_grid)
player_two_grid=place_ships(player_two_grid)
#print_board(player_1_grid)

player_one_Turn = True
player_one_Turn = not player_one_Turn

#grid = create_grid(Rows,Columns)
display_grid(Rows, Columns, player_one_shots)
guess_x()
guess_y()
shot(guess_x,guess_y,player_one_shots,player_two_grid)
#hitship(ship_x,ship_y,guess_x,guess_y)
player_turns(total_turns)

#trzeba podliczyc zestrzelone statki i to ktorego gracza zeby robic game over