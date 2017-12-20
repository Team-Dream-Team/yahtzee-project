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
			full_house = currentPlayer.checkFullHouse(0)
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
		
		print("""
		╔═══════════╗╔═══════════╗╔═══════════╗
		║ Ones      ║║ {0}{1}║║ {0}{1}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Twos      ║║ {2}{3}║║ {2}{3}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Threes    ║║ {4}{5}║║ {4}{5}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Fours     ║║ {6}{7}║║ {6}{7}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Fives     ║║ {8}{9}║║ {8}{9}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Sixes     ║║ {10}{11}║║ {10}{11}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Total     ║║ {12}{13}║║ {12}{13}║
		╠═══════════╬╬═══════════╬╬═══════════╣
		╠═══════════╬╬═══════════╬╬═══════════╣
		║ Three of  ║║ {14}{15}║║ {14}{15}║
		║ a kind    ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Four of   ║║ {16}{17}║║ {16}{17}║
		║ a kind    ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Small     ║║ {18}{19}║║ {18}{19}║
		║ Straight  ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Large     ║║ {20}{21}║║ {20}{21}║
		║ Straight  ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Full House║║ {22}{23}║║ {22}{23}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Chance    ║║ {24}{25}║║ {24}{25}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Yahtzee   ║║ {26}{27}║║ {26}{27}║
		╚═══════════╝╚═══════════╝╚═══════════╝

		""".format(
			Ones, ' '*(box_design_length-len(str(Ones))), 
			Twos, ' '*(box_design_length-len(str(Twos))), 
			Threes, ' '*(box_design_length-len(str(Threes))),
			Fours, ' '*(box_design_length-len(str(Fours))),
			Fives, ' '*(box_design_length-len(str(Fives))),
			Sixes, ' '*(box_design_length-len(str(Sixes))),
			total, ' '*(box_design_length-len(str(total))),
			three_of_a_kind, ' '*(box_design_length-len(str(three_of_a_kind))),
			four_of_a_kind, ' '*(box_design_length-len(str(four_of_a_kind))),
			small_straight, ' '*(box_design_length-len(str(small_straight))),
			large_straight, ' '*(box_design_length-len(str(large_straight))),
			full_house, ' '*(box_design_length-len(str(full_house))),
			chAnce, ' '*(box_design_length-len(str(chAnce))),
			yahtzee, ' '*(box_design_length-len(str(yahtzee))),

			)
		)
	if currentPlayer == player1:
		currentPlayer = player2
	elif currentPlayer == player2:
		currentPlayer = player1
	time.sleep(5)
	cls()
	x+=1
	