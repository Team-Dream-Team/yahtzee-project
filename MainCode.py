#Ben's Class:
import random
import time
from PlayerFINAL import Player
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#Main Code
print("Welcome to Yahtzee.")
name1 = input(str("What is player 1's name? "))
player1 = Player(name1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
name2 = input(str("What is player 2's name? "))
player2 = Player(name2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
player1score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
player2score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

box_design_length = 10

global currentPlayer
currentPlayer = player1

def turn(currentPlayerPre):
	categoryChosen = False
	print(currentPlayer.name+"'s Turn")
	currentPlayer.roll()
	while categoryChosen == False:
		choice = input("Which category would you like to choose? (type 'none' to roll again) ")

		if choice == "Ones" or choice == "ones":
			print(currentPlayer.checkOne(0))
			currentPlayerPre[0] += currentPlayer.checkOne(0)
			categoryChosen = True
		elif choice == "Twos" or choice == "twos":
			print(currentPlayer.checkTwo(0))
			currentPlayerPre[1] += currentPlayer.checkTwo(0)
			categoryChosen = True
		elif choice == "Threes" or choice == "threes":
			print(currentPlayer.checkThree(0))
			currentPlayerPre[2] += currentPlayer.checkThree(0)
			categoryChosen = True
		elif choice == "Fours" or choice == "fours":
			print(currentPlayer.checkFour(0))
			currentPlayerPre[3] += currentPlayer.checkFour(0)
			categoryChosen = True
		elif choice == "Fives" or choice == "fives":
			print(currentPlayer.checkFive(0))
			currentPlayerPre[4] += currentPlayer.checkFive(0)
			categoryChosen = True
		elif choice == "Sixes" or choice == "sixes":
			print(currentPlayer.checkSix(0))
			currentPlayerPre[5] += currentPlayer.checkSix(0)
			categoryChosen = True
			
		elif choice == "Three of a kind" or choice == "three of a kind":
			print(currentPlayer.checkthreeofakind(0))
			currentPlayerPre[7] += currentPlayer.checkthreeofakind(0)
			categoryChosen = True
		elif choice == "Four of a kind" or choice == "four of a kind":
			print(currentPlayer.checkfourofakind(0))
			currentPlayerPre[8] += currentPlayer.checkfourofakind(0)
			categoryChosen = True
		elif choice == "small straight" or choice == "Small Straight":
			print(currentPlayer.small_straight(0))
			currentPlayerPre[9] += currentPlayer.small_straight(0)
			categoryChosen = True
		elif choice == "large straight" or choice == "Large Straight":
			print(currentPlayer.large_straight(0))
			currentPlayerPre[10] += currentPlayer.large_straight(0)
			categoryChosen = True
		elif choice == "Full house" or choice == "full house" or choice == "Full House":
			print(currentPlayer.checkFullHouse(0))
			currentPlayerPre[11] += currentPlayer.checkFullHouse(0)
			categoryChosen = True
		elif choice == "Chance" or choice == "chance":
			print(currentPlayer.chance(0))
			currentPlayerPre[12] += currentPlayer.chance(0)
			categoryChosen = True
		elif choice == "Yahtzee" or choice == "yahtzee":
			print(currentPlayer.checkYahtzee(0))
			currentPlayerPre[13] += currentPlayer.checkYahtzee(0)
			categoryChosen = True
		elif choice == "none":
			currentPlayer.roll_replace()
		else: 
			choice = input("Which category would you like to choose? (type 'none' to roll again) ")
		
		total = (sum(currentPlayerPre)-currentPlayerPre[6])
		return currentPlayerPre

x = 1
while x < 27:
	categoryChosen = False
	if currentPlayer == player1:
		player1score = turn(player1score)
	elif currentPlayer == player2:
		player2score = turn(player2score)
	print("""
	╔═══════════╗╔═══════════╗╔═══════════╗
	║ Ones      ║║ {0}{1}║║ {28}{29}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Twos      ║║ {2}{3}║║ {30}{31}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Threes    ║║ {4}{5}║║ {32}{33}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Fours     ║║ {6}{7}║║ {34}{35}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Fives     ║║ {8}{9}║║ {36}{37}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Sixes     ║║ {10}{11}║║ {38}{39}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Total     ║║ {12}{13}║║ {40}{41}║
	╠═══════════╬╬═══════════╬╬═══════════╣
	╠═══════════╬╬═══════════╬╬═══════════╣
	║ Three of  ║║ {14}{15}║║ {42}{43}║
	║ a kind    ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Four of   ║║ {16}{17}║║ {44}{45}║
	║ a kind    ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Small     ║║ {18}{19}║║ {46}{47}║
	║ Straight  ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Large     ║║ {20}{21}║║ {48}{49}║
	║ Straight  ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Full House║║ {22}{23}║║ {50}{51}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Chance    ║║ {24}{25}║║ {52}{53}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Yahtzee   ║║ {26}{27}║║ {54}{55}║
	╚═══════════╝╚═══════════╝╚═══════════╝
	""".format(
		str(player1score[0]), ' '*(box_design_length-len(str(player1score[0]))), 
		str(player1score[1]), ' '*(box_design_length-len(str(player1score[1]))), 
		str(player1score[2]), ' '*(box_design_length-len(str(player1score[2]))),
		str(player1score[3]), ' '*(box_design_length-len(str(player1score[3]))),
		str(player1score[4]), ' '*(box_design_length-len(str(player1score[4]))),
		str(player1score[5]), ' '*(box_design_length-len(str(player1score[5]))),
		str(player1score[6]), ' '*(box_design_length-len(str(player1score[6]))),
		str(player1score[7]), ' '*(box_design_length-len(str(player1score[7]))),
		str(player1score[8]), ' '*(box_design_length-len(str(player1score[8]))),
		str(player1score[9]), ' '*(box_design_length-len(str(player1score[9]))),
		str(player1score[10]), ' '*(box_design_length-len(str(player1score[10]))),
		str(player1score[11]), ' '*(box_design_length-len(str(player1score[11]))),
		str(player1score[12]), ' '*(box_design_length-len(str(player1score[12]))),
		str(player1score[13]), ' '*(box_design_length-len(str(player1score[13]))),
		str(player2score[0]), ' '*(box_design_length-len(str(player2score[0]))),
		str(player2score[1]), ' '*(box_design_length-len(str(player2score[1]))),
		str(player2score[2]), ' '*(box_design_length-len(str(player2score[2]))),
		str(player2score[3]), ' '*(box_design_length-len(str(player2score[3]))),
		str(player2score[4]), ' '*(box_design_length-len(str(player2score[4]))),
		str(player2score[5]), ' '*(box_design_length-len(str(player2score[5]))),
		str(player2score[6]), ' '*(box_design_length-len(str(player2score[6]))),
		str(player2score[7]), ' '*(box_design_length-len(str(player2score[7]))),
		str(player2score[8]), ' '*(box_design_length-len(str(player2score[8]))),
		str(player2score[9]), ' '*(box_design_length-len(str(player2score[9]))),
		str(player2score[10]), ' '*(box_design_length-len(str(player2score[10]))),
		str(player2score[11]), ' '*(box_design_length-len(str(player2score[11]))),
		str(player2score[12]), ' '*(box_design_length-len(str(player2score[12]))),
		str(player2score[13]), ' '*(box_design_length-len(str(player2score[13]))),
		)
	)
	if currentPlayer == player1:
		currentPlayer = player2
	elif currentPlayer == player2:
		currentPlayer = player1
	input("Press Enter to end your turn: ")
	cls()
	x+=1