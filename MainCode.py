#Ben's Class:
import random
import time
from Player import Player

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
three_of_a_kind = 0
four_of_a_kind = 0
small_straight = 0
large_straight = 0
full_house = 0
chance = 0
yahtzee = 0
box_design_length = 10

for turnNum in range(13):
	print(player1.name+"'s Turn")
	player1.roll_dice(5)
	n = 1
	while n == 1: 
		choice = input("Which category would you like to choose? (type 'none' to roll again) ")

		if choice == "Ones" or choice == "ones":
			print(player1.checkOne(0))
			Ones = player1.checkOne(0)
		elif choice == "Twos" or choice == "twos":
			print(player1.checkTwo(0))
			Twos = player1.checkTwo(0)
		elif choice == "Threes" or choice == "threes":
			print(player1.checkThree(0))
			Threes = player1.checkThree(0)
		elif choice == "Fours" or choice == "fours":

			print(player1.checkFour(0))
			Fours = player1.checkFour(0)
		elif choice == "Fives" or choice == "threes":
			print(player1.checkFive(0))
			Fives = player1.checkFive(0)

			print(Player.checkFour(0))
			Fours = Player.checkFour(0)
		elif choice == "Fives" or choice == "fives":
			print(player1.checkFive(0))
			Fives = player1.checkFive(0)

		elif choice == "Sixes" or choice == "sixes":
			print(player1.checkSix(0))
			Sixes = player1.checkSix(0)
		elif choice == "Three of a kind" or choice == "three of a kind":
			print(player1.checkthreeofakind(0))
			three_of_a_kind = player1.checkthreeofakind(0)
		elif choice == "Four of a kind" or choice == "four of a kind":

			print(player1.checkfourofakind(0))
			four_of_a_kind = player1.checkfourofakind(0)

			print(player1.checkfourofakind(0))
			four_of_a_kind = Player.checkfourofakind(0)
		elif choice == "small straight" or choice == "Small Straight":
			print(player1.small_straight(0))
			small_straight = player1.small_straight(0)
		elif choice == "large straight" or choice == "Large Straight":
			print(player1.large_straight(0))
			large_straight = player1.large_straight(0)
		elif choice == "Full house" or choice == "full house" or choice == "Full House":
			print(player1.checkFullHouse(0))
			full_house = checkFullHouse(0)

		elif choice == "Chance" or choice == "chance":
			print(player1.chance(0))
			chance = player1.chance(0)
		elif choice == "Yahtzee" or choice == "yahtzee":
			print(player1.checkYahtzee(0))
			yahtzee = player1.checkYahtzee(0)
		elif choice == "none":
			player1.roll_replace()		
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
		║ Four of   ║║ {14}{15}║║ {14}{15}║
		║ a kind    ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Small     ║║ {14}{15}║║ {14}{15}║
		║ Straight  ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Large     ║║ {14}{15}║║ {14}{15}║
		║ Straight  ║║           ║║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Full House║║ {14}{15}║║ {14}{15}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Chance    ║║ {16}{17}║║ {16}{16}║
		╠═══════════╣╠═══════════╣╠═══════════╣
		║ Yahtzee   ║║ {17}{18}║║ {17}{18}║
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
			chance, ' '*(box_design_length-len(str(chance))),
			yahtzee, ' '*(box_design_length-len(str(yahtzee))),
			)
		)			
			
for turnNum in range(13):
	print(player2.name+"'s Turn")
	input("Press enter to roll your dice.")
	player2.roll_dice(5)
	choice = input("Which category would you like to choose? (type 'none' to roll again) ")
	# print table
	if choice == "Ones" or choice == "ones":
		print(Player.checkOne())
		Ones = Player.checkOne()
	elif choice == "Twos" or choice == "twos":
		print(Player.checkTwo())
		Twos = Player.checkTwo()
	elif choice == "Threes" or choice == "threes":
		print(Player.checkThree())
		Threes = Player.checkThree()
	elif choice == "Fours" or choice == "fours":
		print(Player.checkFour())
		Fours = Player.checkFour()
	elif choice == "Fives" or choice == "fives":
		print(Player.checkFive())
		Fives = Player.checkFive()
	elif choice == "Sixes" or choice == "sixes":
		print(Player.checkSix())
		Sixes = Player.checkSix()
	elif choice == "Three of a kind" or choice == "three of a kind":
		print(Player.checkthreeofakind())
		three_of_a_kind = Player.checkthreeofakind()
	elif choice == "Four of a kind" or choice == "four of a kind":
		print(Player.checkfourofakind())
		four_of_a_kind = Player.checkfourofakind()
	elif choice == "small straight" or choice == "Small Straight":
		print(Player.small_straight())
		small_straight = Player.small_straight()
	elif choice == "large straight" or choice == "Large Straight":
		print(Player.large_straight())
		large_straight = Player.large_straight()
	elif choice == "Full house" or choice == "full house" or choice == "Full House":
		print(Player.checkFullHouse())
		full_house = checkFullHouse()
	elif choice == "Chance" or choice == "chance":
		print(sum(dice))
		Chance = sum(dice)
	elif choice == "Yahtzee" or choice == "yahtzee":
		print(Player.checkYahtzee())
		yahtzee = Player.checkYahtzee()
	elif choice == "none":
		player1.roll_replace()		
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
	║ a kind    ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Four of   ║║ {14}{15}║║ {14}{15}║
	║ a kind    ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Small     ║║ {14}{15}║║ {14}{15}║
	║ Straight  ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Large     ║║ {14}{15}║║ {14}{15}║
	║ Straight  ║║           ║║           ║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Full House║║ {14}{15}║║ {14}{15}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Chance    ║║ {15}{16}║║ {16}{17}║
	╠═══════════╣╠═══════════╣╠═══════════╣
	║ Yahtzee   ║║ {18}{19}║║ {18}{19}║
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
		chance, ' '*(box_design_length-len(str(chance))),
		yahtzee, ' '*(box_design_length-len(str(yahtzee))),
		)
	)