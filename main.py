#Jeffrey Collins
#Ms. Shah App Dev
#04/26/2022
# Program Desription : This is a game where you're a virus fighting in a human's immune system
 
import csv
import sys
import random
import os
import time

#I made a class for charaters so I could add and remove them at any time
class Entity():
    def __init__(self, hp, atk, dif):
        self.hp = hp
        self.atk = atk
        self.dif = dif

class Battle():
  #How damage is calcaulated 
    def Attack(self, attacker, defender):
        damage = max(attacker.atk - defender.dif, 0)
        defender.hp -= damage
        
    #The combat system
    def Combat(self, player, enemy):
        turns = []
        while True:
            while len(turns) < 5:
                turn = random.randint(1, 2)
                if turn == 1:
                    turns.append("player")
                else:
                    turns.append("enemy")

            for current_turn in turns:
                print(player.hp, enemy.hp)
                if current_turn == "player":
                    print(f"TURNS: \n{current_turn}\n{turns[turns.index(current_turn)+ 1:]}")
                  
                    choice = input("1. Attack\n2. Defend\n")
                    if choice == "1":
                        self.Attack(player, enemy)
                        player.dif = 20
                    elif choice == "2":
                        player.dif *= 2
                    else:
                        print("Lost your chance!")
                elif current_turn == "enemy":
                    
                    print("Enemy turn!")
                    print(f"Next turns are: {turns}")
                    enemy_choice = random.randint(1, 2)
                    if enemy_choice == 2:
                        print("He attacks you!")
                        self.Attack(enemy, player)
                        enemy.dif = 0
                        time.sleep(3) #Allows wait time between text
                    else:
                        print("He defends himself.")
                        enemy.dif = 10
                        
                      
                os.system("clear")
                turns.pop(0)
                if player.hp <= 0:
                    gameover()
                    sys.exit(0)
                elif enemy.hp <= 0:
                    winscreen()
                    sys.exit(0)
                break
              
def menu():
    print("[[[[[[\\\\[Viral Agent Demo]///]]]]]")
    print()

    choice = input("""
                      A: Start Game
                      B: About
                      C: Exit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        start()
    elif choice == "B" or choice =="b":
        about()
    elif choice=="C" or choice=="c":
        sys.exit
    else:
        print("No valid inputs detected")
        print("Please try again")
        menu()

def about():
  print("\nHello, My name is Jeffrey Collins\nThis is a text style game for my App Dev Final Project\nThis was actually my project for my John Hopkins class but I decided to fix it and change make it into a properly functioning program.\nI hope you enjoy it\n I plan on adding more enemies and different win conditions later")
  print("\n")
  menu()
  
#This is the introducting text.
def start():
  print("\nYou are an agent.")
  input("Press Enter to continue...\n")
  print("\nYou are an agent so small you can't be seen by any ordinary light microscope.")
  input("Press Enter to continue...\n")
  print("Your job is to infect and replicate inside THIS living organism.")
  input("Press Enter to continue...\n")
  input("Pillage")
  input("Loot")
  input("Plunder")
  input("\nGood Luck Agent")
  playerop()



#Calls the entiies into battle
def playerop():
  charachter = Entity(100, 15, 15)
  boss = Entity(150, 40, 0)
  testbattle = Battle()
  testbattle.Combat(charachter, boss)


def gameover():
  print("The Human lives to see another day and your stain goes extinct with your failure.\n\nGAME OVER\n")
  sys.exit(0)

def winscreen():
  print("You've won. The defences of the human have fallen and its resources are plundered and absorbed.\nThanks for playing!\nYou WON!!!\n")
  sys.exit(0)

  
def main():
   menu()
#the program is initiated, so to speak, here

if __name__ == "__main__":
  main()
  #The Virus takes over and absorbs your body for resouces
