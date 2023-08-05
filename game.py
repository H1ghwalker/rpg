 #Python text RPG

import cmd
import textwrap
import sys
import os
import time 
import random

screen_width = 100

#Player Setup

class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self. mp = 0
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False

my_player = Player()

#Title screen 
def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        setup_game() #placeholder until written
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command")
        option = input(">")
        if option.lower() == ("play"):
            setup_game() #placeholder until written
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
            
def title_screen():
    os.system("clear")
    print("############################")
    print("# Welcome to the text RPG! #")
    print("############################")
    print("          - Play -         ")
    print("          - Help -         ")
    print("          - Quit -         ")
    print("    Copyright 2023 Benjii  ")
    title_screen_selections()
    
def help_menu():
    print("###########################")
    print("# Welcome to the text RPG! #")
    print("###########################")
    print("- Use up, down, left, right to move -")
    print("- Type your commands to do them -")
    print("- Use 'look' to inspect something -")
    print("- Good luck and have fun! -")
    title_screen_selections()

#Game map
# a1, a2 ... #Player starts at b2
# -------------
# |  |  |  |  | a4
# -------------
# |  |  |  |  | b4...
# -------------
# |  |  |  |  |
# -------------
# |  |  |  |  |
# -------------
ZONENAME = 'zonename'
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
                'b1': False,'b2': False,'b3': False,'b4': False,
                'c1': False,'c2': False,'c3': False,'c4': False,
                'd1': False,'d2': False,'d3': False,'d4': False,
                }
zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
    },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks the same',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    
}

#Game interactivity
def print_location():
    print('\n' + ('#' * (4 + len(my_player.location))))
    print('# ' + my_player.location.upper() + ' #')
    print('# ' + zonemap[my_player.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(my_player.location))))

def prompt():
    print('\n' + '======================')
    print('What would you like to do?')
    action = input(">")
    accepteble_actions =['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in accepteble_actions:
        print('Unknown action, try again\n')
        action = input(">")
    if action.lower() =='quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
        
def player_move(my_action):
    ask = 'Where would you like to move to?\n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[my_player.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[my_player.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[my_player.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[my_player.location][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    print('\n' + 'You have moved to the ' + destination + '.')
    my_player.location = destination
    print_location()

def player_examine(action):
    if zonemap[my_player.location[SOLVED]]:
        print('You have already exhausted this zone.')
    else:
        print('You can trigger puzzle here')
    
#Game functionality

def main_game_loop():
    while my_player.game_over is False:
        prompt()
        #here handle if puzzles have been solved, boss defeated, expored everything, etc

def setup_game():
    os.system('clear')
    
    #Name collecting
    question1 = "Hello, what's your name\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('>')
    my_player.name = player_name
   
   #Job handling 
    question2 = "What role do you want to play?\n"
    question2_added = 'You can play as a warriror, mage or a priest.'
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2_added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input('>')
    valid_jobs = ['warriror', 'mage', 'priest']
    if player_job.lower() in valid_jobs:
        my_player.job = player_job
        print('You are now a ' + player_job + "!\n" )
    while player_job.lower() not in valid_jobs:
        player_job = input('>')
        if player_job.lower() in valid_jobs:
            my_player.job = player_job
            print('You are now a ' + player_job + "!\n" )
    
    #Player stats
    if my_player.job is 'warriror':
        self.hp =120
        self.mp = 20
    elif my_player.job is 'mage':
        self.hp = 40
        self.mp = 120
    elif my_player.job is 'priest':
        self.hp = 60
        self.mp = 60
        
    #my_player.job = player_job

    #Introduction
    question3 = "Welcome, " + player_name + ' the ' + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    
    speech1 = 'Welcome to this fantasy world\n'
    speech2 = 'I hope it greets you well\n'
    speech3 = 'Just make sure you dont get too lost...\n'
    speech4 = 'He-he-he!\n'
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    
    os.system('clear')
    print('#########################')
    print('#    Lets start now!    #')
    print('#########################')
    main_game_loop()
    
    
    
    
title_screen()