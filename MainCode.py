#Ben's Class:
import random

from Player import Player

#Main Code
print("Welcome to Yahtzee.")
name1 = input(str("What is player 1's name? "))
player1 = Player(name1, 0)
name2 = input(str("What is player 2's name? "))
player2 = Player(name2, 0)
for turnNum in range(13):
	print(player1.name+"'s Turn")
	player1.roll_dice(5)
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
	elif choice == "Fives" or choice == "threes":
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
	elif choice == "Chance" or choice == "chance":
		print(sum(dice))
		Chance = sum(dice)
	elif choice == "none":
		roll_replace()		
	else: 
		choice = input("Which category would you like to choose? (type 'none' to roll again) ")
						
		
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
	elif choice == "Fives" or choice == "threes":
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
	elif choice == "Chance" or choice == "chance":
		print(sum(dice))
		Chance = sum(dice)
	elif choice == "none":
		roll_replace()		
	else: 
		choice = input("Which category would you like to choose? (type 'none' to roll again) ")
						
		

'''dice.roll(5)
print("You rolled: " DiceValues)
player.validChoices(DiceValues) #Displays valid category choices based on dice values
if player.validChoices != 0:
	choice = input("Which category would you like to choose? (type 'none' to roll again) ")
	if choice == "Ones":
		for j in range(0, len(DiceValues)):
			if j != 1:
				DiceValues.remove(j)
		ones = sum(DiceValues)
	elif choice == "Twos":
		for j in range(0, len(DiceValues)):
			if j != 2:
				DiceValues.remove(j)
		twos = sum(DiceValues)
	elif choice == "Threes":
		for j in range(0, len(DiceValues)):
			if j != 3:
				DiceValues.remove(j)
		threes = sum(DiceValues)
	elif choice == "Fours":
		for j in range(0, len(DiceValues)):
			if j != 4:
				DiceValues.remove(j)
		fours = sum(DiceValues)
	elif choice == "Fives":
		for j in range(0, len(DiceValues)):
			if j != 5:
				DiceValues.remove(j)
		fives = sum(DiceValues)
	elif choice == "Sixes":
		for j in range(0, len(DiceValues)):
			if j != 6:
				DiceValues.remove(j)
		sixes = sum(DiceValues)
	elif choice == "Three of a kind":
		three_of_a_kind = sum(DiceValues)
	elif choice == "Four of a kind":
		four_of_a_kind = sum(DiceValues)
	elif choice == "Full House":
		full_house = sum(DiceValues)
	elif choice == "Small Straight":
		small_straight = sum(DiceValues)
	elif choice == "Large Straight":
		large_straight = sum(DiceValues)
	elif choice == "Chance":
		chance = sum(DiceValues)
	else:
		print(????)'''
ones = 2
twos = 4
threes = 9
fours = 12
fives = 10
sixes = 12
three_of_a_kind = 27
four_of_a_kind = 32
full_house = 25
small_straight = 15
large_straight = 21
chance = 0
yahtzee = 0
total = ones+twos+threes+fours+fives+sixes
box_design_length = 10


print("""╔═══════════╗╔═══════════╗
║ Ones      ║║ {0}{1}║
╠═══════════╣╠═══════════╣
║ Twos      ║║ {2}{3}║
╠═══════════╣╠═══════════╣
║ Threes    ║║ {4}{5}║
╠═══════════╣╠═══════════╣
║ Fours     ║║ {6}{7}║
╠═══════════╣╠═══════════╣
║ Fives     ║║ {8}{9}║
╠═══════════╣╠═══════════╣
║ Sixes     ║║ {10}{11}║
╠═══════════╣╠═══════════╣
║ Total     ║║ {12}{13}║
╠═══════════╬╬═══════════╬
╠═══════════╬╬═══════════╬
║ Three of  ║║ {14}{15}║
║ a kind    ║║           ║
╠═══════════╣╠═══════════╣


""".format(
	ones, ' '*(box_design_length-len(str(ones))), 
	twos, ' '*(box_design_length-len(str(twos))), 
	threes, ' '*(box_design_length-len(str(threes))),
	fours, ' '*(box_design_length-len(str(fours))),
	fives, ' '*(box_design_length-len(str(fives))),
	sixes, ' '*(box_design_length-len(str(sixes))),
	total, ' '*(box_design_length-len(str(total))),
	three_of_a_kind, ' '*(box_design_length-len(str(three_of_a_kind)))
	)
)