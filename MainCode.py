#Main Code
import classes that ben /is making

scoreboardLayout='''
╔═══════════╗╔═══════════╗
║ Ones 		║║	{0}		 ║
╠═══════════╣╠═══════════╣
║ Twos		║║	{1}		 ║
╠═══════════╣╠═══════════╣
║ Threes	║║	{2}		 ║
╠═══════════╣╠═══════════╣
║ Fours		║║	{3}		 ║
╠═══════════╣╠═══════════╣
║ Fives		║║	{4}		 ║
╠═══════════╣╠═══════════╣
║ Sixes		║║	{5}		 ║
╠═══════════╣╠═══════════╣
║ Total		║║	{6}		 ║
╠═══════════╬╬═══════════╬
╠═══════════╬╬═══════════╬
║ Three of	║║	{7}		 ║
║ a kind	║║			 ║
╠═══════════╣╠═══════════╣
║ Four of	║║	{8}		 ║
║ a kind	║║			 ║
╠═══════════╣╠═══════════╣
║ Full House║║	{9}		 ║
╠═══════════╣╠═══════════╣
║ Small		║║	{10}	 ║
║ Straight	║║			 ║
╠═══════════╣╠═══════════╣
║ Large		║║	{11}	 ║
║ Straight	║║			 ║
╠═══════════╣╠═══════════╣
║ Chance	║║	{12}	 ║
╠═══════════╣╠═══════════╣
║ Yahtzee	║║	{13}	 ║
╚═══════════╝╚═══════════╝
'''
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

print(scoreboardLayout.format(ones, twos, threes, fours, fives, sixes, total, three_of_a_kind, four_of_a_kind, full_house, small_straight, large_straight, chance, yahtzee))
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
		print(????)





