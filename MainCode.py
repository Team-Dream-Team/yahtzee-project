#Main Code
import classes that ben /is making

print:('''
╔═══════════╗╔═══════════╗
║ Ones 		║║Player One ║
╠═══════════╣╠═══════════╣
║ Twos		║║			 ║
╠═══════════╣╠═══════════╣
║ Threes	║║			 ║
╠═══════════╣╠═══════════╣
║ Fours		║║			 ║
╠═══════════╣╠═══════════╣
║ Fives		║║			 ║
╠═══════════╣╠═══════════╣
║ Sixes		║║			 ║
╠═══════════╣╠═══════════╣
║ Total		║║			 ║
╠═══════════╬╬═══════════╬		  			 
╠═══════════╬╬═══════════╬
║ Three of	║║			 ║
║ a kind	║║			 ║
╠═══════════╣╠═══════════╣
║ Four of	║║			 ║
║ a kind	║║			 ║
╠═══════════╣╠═══════════╣
║ Full House║║			 ║
╠═══════════╣╠═══════════╣
║ Small		║║			 ║
║ Straight	║║			 ║
╠═══════════╣╠═══════════╣
║ Large		║║			 ║
║ Straight	║║			 ║
╠═══════════╣╠═══════════╣
║ Chance	║║			 ║
╠═══════════╣╠═══════════╣
║ Yahtzee	║║			 ║
╚═══════════╝╚═══════════╝
''')
dice.roll(5)
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
		large straight = sum(DiceValues)
	else:
		print(????)





