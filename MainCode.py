#Main Code

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