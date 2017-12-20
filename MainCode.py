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
Ones = 0
Twos = 0
Threes = 0
Fours = 0
Fives = 0
Sixes = 0

player1score = []
player2score = []
three_of_a_kind = 0
four_of_a_kind = 0
small_straight = 0
large_straight = 0
full_house = 0
chAnce = 0
yahtzee = 0
box_design_length = 10

currentPlayer = player1
categoryChosen = False

x = 1
while x < 27:
	categoryChosen = False
	print(currentPlayer.name+"'s Turn")
	currentPlayer.roll()
	while categoryChosen == False:
		choice = input("Which category would you like to choose? (type 'none' to roll again) ")

		if choice == "Ones" or choice == "ones":
			print(currentPlayer.checkOne(0))
			Ones = currentPlayer.checkOne(0)
			categoryChosen = True
		elif choice == "Twos" or choice == "twos":
			print(currentPlayer.checkTwo(0))
			Twos = currentPlayer.checkTwo(0)
			categoryChosen = True
		elif choice == "Threes" or choice == "threes":
			print(currentPlayer.checkThree(0))
			Threes = currentPlayer.checkThree(0)
			categoryChosen = True
		elif choice == "Fours" or choice == "fours":
			print(currentPlayer.checkFour(0))
			Fours = currentPlayer.checkFour(0)
			categoryChosen = True
		elif choice == "Fives" or choice == "fives":
			print(currentPlayer.checkFive(0))
			Fives = currentPlayer.checkFive(0)
			categoryChosen = True
		elif choice == "Sixes" or choice == "sixes":
			print(currentPlayer.checkSix(0))
			Sixes = currentPlayer.checkSix(0)
			categoryChosen = True
		elif choice == "Three of a kind" or choice == "three of a kind":
			print(currentPlayer.checkthreeofakind(0))
			three_of_a_kind = currentPlayer.checkthreeofakind(0)
			categoryChosen = True
		elif choice == "Four of a kind" or choice == "four of a kind":
			print(currentPlayer.checkfourofakind(0))
			four_of_a_kind = currentPlayer.checkfourofakind(0)
			categoryChosen = True
		elif choice == "small straight" or choice == "Small Straight":
			print(currentPlayer.small_straight(0))
			small_straight = currentPlayer.small_straight(0)
			categoryChosen = True
		elif choice == "large straight" or choice == "Large Straight":
			print(currentPlayer.large_straight(0))
			large_straight = currentPlayer.large_straight(0)
			categoryChosen = True
		elif choice == "Full house" or choice == "full house" or choice == "Full House":
			print(currentPlayer.checkFullHouse(0))
			full_house = checkFullHouse(0)
			categoryChosen = True
		elif choice == "Chance" or choice == "chance":
			print(currentPlayer.chance(0))
			chAnce = currentPlayer.chance(0)
			categoryChosen = True
		elif choice == "Yahtzee" or choice == "yahtzee":
			print(currentPlayer.checkYahtzee(0))
			yahtzee = currentPlayer.checkYahtzee(0)
			categoryChosen = True
		elif choice == "none":
			currentPlayer.roll_replace()		
		else: 
			choice = input("Which category would you like to choose? (type 'none' to roll again) ")
		
		total = Ones+Twos+Threes+Fours+Fives+Sixes
		
		if currentPlayer == player1:
			player1score = (Ones, Twos, Threes, Fours, Fives, Sixes, total, three_of_a_kind, four_of_a_kind, small_straight, large_straight, full_house, chAnce, yahtzee)	
		elif currentPlayer == player2:
			player2score = (Ones, Twos, Threes, Fours, Fives, Sixes, total, three_of_a_kind, four_of_a_kind, small_straight, large_straight, full_house, chAnce, yahtzee)
		
		print("""
		╔═══════════╗╔═══════════╗╔═══════════╗
		║ Ones      ║║ {0}{1}║║ {27}{28}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Twos      ║║ {2}{3}║║ {29}{30}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Threes    ║║ {4}{5}║║ {31}{32}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Fours     ║║ {6}{7}║║ {33}{34}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Fives     ║║ {8}{9}║║ {35}{36}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Sixes     ║║ {10}{11}║║ {37}{38}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Total     ║║ {12}{13}║║ {39}{40}║
		╠═══════════╬╬═══════════╬╬═══════════╣
		╠═══════════╬╬═══════════╬╬═══════════╣
		║ Three of  ║║ {14}{15}║║ {41}{42}║
		║ a kind    ║║           ║║           ║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Four of   ║║ {15}{16}║║ {43}{44}║
		║ a kind    ║║           ║║           ║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Small     ║║ {17}{18}║║ {45}{56}║
		║ Straight  ║║           ║║           ║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Large     ║║ {19}{20}║║ {47}{48}║
		║ Straight  ║║           ║║           ║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Full House║║ {21}{22}║║ {49}{50}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Chance    ║║ {23}{24}║║ {51}{52}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Yahtzee   ║║ {25}{26}║║ {53}{54}║
		╚═══════════╝╚═══════════╝╚═══════════╝
		""".format(
			player1score[0], ' '*(box_design_length-len(str(player1score[0]))), 
			player1score[1], ' '*(box_design_length-len(str(player1score[1]))), 
			player1score[2], ' '*(box_design_length-len(str(player1score[2]))),
			player1score[3], ' '*(box_design_length-len(str(player1score[3]))),
			player1score[4], ' '*(box_design_length-len(str(player1score[4]))),
			player1score[5], ' '*(box_design_length-len(str(player1score[5]))),
			player1score[6], ' '*(box_design_length-len(str(player1score[6]))),
			player1score[7], ' '*(box_design_length-len(str(player1score[7]))),
			player1score[8], ' '*(box_design_length-len(str(player1score[8]))),
			player1score[9], ' '*(box_design_length-len(str(player1score[9]))),
			player1score[10], ' '*(box_design_length-len(str(player1score[10]))),
			player1score[11], ' '*(box_design_length-len(str(player1score[11]))),
			player1score[12], ' '*(box_design_length-len(str(player1score[12]))),
			player1score[13], ' '*(box_design_length-len(str(player1score[13]))),
			player2score[0], ' '*(box_design_length-len(str(player2score[0]))),
			player2score[1], ' '*(box_design_length-len(str(player2score[1]))),
			player2score[2], ' '*(box_design_length-len(str(player2score[2]))),
			player2score[3], ' '*(box_design_length-len(str(player2score[3]))),
			player2score[4], ' '*(box_design_length-len(str(player2score[4]))),
			player2score[5], ' '*(box_design_length-len(str(player2score[5]))),
			player2score[6], ' '*(box_design_length-len(str(player2score[6]))),
			player2score[7], ' '*(box_design_length-len(str(player2score[7]))),
			player2score[8], ' '*(box_design_length-len(str(player2score[8]))),
			player2score[9], ' '*(box_design_length-len(str(player2score[9]))),
			player2score[10], ' '*(box_design_length-len(str(player2score[10]))),
			player2score[11], ' '*(box_design_length-len(str(player2score[11]))),
			player2score[12], ' '*(box_design_length-len(str(player2score[12]))),
			player2score[13], ' '*(box_design_length-len(str(player2score[13]))),
			


			)
		)
	if currentPlayer == player1:
		currentPlayer = player2
	elif currentPlayer == player2:
		currentPlayer = player1
	time.sleep(5)
	cls()
	x+=1