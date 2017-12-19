#Ben's Class:
import random

class Player: 

	def __init__(self, name, score):
		#multiple players, multiple names
		self.name = name 
		self.score = score

	def roll_dice(x):
		#dice class, dice list needs to be global since it will be used to check scores
		global dice
		dice = []
		for i in range(x):
			dice += [random.randint(1,6)]
			dice = sorted(dice)
			print(dice)	
		return dice
	#check dice list for given number and add them all up
	def checkOne(): 
		if self.dice.count(1) > 0:
			self.score += self.dice.count(1)*1
		else: 
			self.score += 0
		return self.score
	def checkTwo(): 
		if self.dice.count(2) > 0:
			self.score += self.dice.count(2)*2
		else: 
			self.score += 0
		return self.score
	def checkThree(): 
		if self.dice.count(3) > 0:	
			self.score += self.dice.count(3)*3
		else: 
			self.score += 0
		return self.score
	def checkFour(): 
		if self.dice.count(4) > 0:
			self.score += self.dice.count(4)*4
		else: 
			self.score += 0
		return self.score
	def checkFive(): 
		if self.dice.count(5) > 0:
			self.score += self.dice.count(5)*5
		else: 
			self.score += 0
		return self.score
	def checkSix(): 
		if self.dice.count(1) > 0:
			self.score += self.dice.count(6)*6
		else: 
			self.score += 0
		return self.score
	#check three of a kind
	def checkthreeofakind():
	#add up all the dice in the list if there is at least a three of a kind
		for number in dice: 
			if dice.count(number) >= 3: 
				self.score += sum(dice)
			else: 
				self.score += 0
		return self.score
	def checkfourofakind(): 
	#add up all the dice if there is at least a four of a kind
		for number in dice: 
			if dice.count(number) >= 4: 
				self.score += sum(dice)
			else:
				self.score += 0
		return self.score
	def checkYahtzee():
	#if there is a yahtzee, you will be awarded points based off your first or second time
		for number in dice: 
			if dice.count(number) == 5: 
				if yahtzeeWin:
					self.score += 100
				else:
					yahtzeeWin = True
					self.score += 50
			else: 
				self.score += 0
		return self.score
	#check for full house numbers in the dice and award 25 points if full house exists
	#otherwise, award 0 points
	def checkFullHouse():
		for num in dice: 
			if dice.count(num) == 3:
				for second_num in dice: 
					if dice.count(second_num) == 2:
						self.score += 25
			else: 
				self.score += 0
		return self.score
	
	def small_straight():
		sortArray = list(set(dice))
		if sortArray == [1,2,3,4] or sortArray == [2,3,4,5] or sortArray == [3,4,5,6]:
			self.score += 30
		else: 
			self.score += 0
	def large_straight():
		sortArray = list(set(dice))
		if sortArray == [1,2,3,4,5] or sortArray == [2,3,4,5,6]:
			self.score += 40
		else: 
			self.score += 0



	def stats(self):
		print("Name: " +self.name)
		print("Score:" +str(self.score))



#Main Code
print("Welcome to yahtzee.")
name1 = input(str("What is player 1's name? "))
player1 = Player(name1, 0)
name2 = input(str("What is player 2's name? "))
player2 = Player(name2, 0)
while rolls <= 3:
	print(Player.name+"'s Turn")
	available = 5
	input("Press enter to roll your dice.")
	player.roll_dice(available)
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
		three_of_a_kind = Player.checkthreeofakind
	elif choice == "Four of a kind" or choice == "four of a kind"



	elif choice == "Chance" or choice == "chance":
		print(sum(dice))
		Chance = sum(dice)
	elif choice == "none"
		while (???):
		print(dice)
		numvalue = input("Which dice would you like to remove?(enter number shown on dice) ")
		chosenDice = dice.find(numvalue)
		dice.remove(chosenDice)
		



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