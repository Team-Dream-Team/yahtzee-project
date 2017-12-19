import random

class Player: 

	def __init__(self, name, score):
		#multiple players, multiple names
		self.name = name 
		self.score = score

	def roll_dice(self, x):
		#dice class, dice list needs to be global since it will be used to check scores
		global dice
		dice = []
		for i in range(x):
			dice += [random.randint(1,6)]
			dice = sorted(dice)
			print(dice)	
		return dice

	def roll_replace(self): 
		replacing = []
		replacing_indexes = []
		rolls = 0
		print("Your first roll was:", dice, "\n")
		result = input("Do you want to keep these? (y or n)?")
		result = (result.lower()).strip
		while result not in ("y","n"):
			result = input("You probably mistyped something...please try again")
			result = result.lower()
		if result == "n":
			while rolls != 2: 
				if rolls != 0:
					print("Your current dice are:", dice, "\n")
					result = input("Do you want to keep these dice (y or n) (default is n)? \n")
					result = result.lower()
					if result == "y":
						break;
				replaceNums = input("Type the ordinal numbers (first position would be 1, second would be 2) \n dice to replace")
				try: 
					replaced_dice = list(replaceNums)
					for replaceNums in replaced_dice: 
						skip = False

						array_index = int(index) - 1
						if array_index < 0:
							raise IndexError("That wasn't an ordinal number!")
						while array_index in replacing_indexes: 
							print("Sorry, you are already replacing" + str(dice[array_index]) + ".\n")
							skip = True
							break
						if skip:
							continue
						replacing.append(dice[array_index])
						replacing_indexes.append(array_index)
				except IndexError:
					print("You only have 5 dice!")
					replacing = []
					replacing_indexes = []
					continue
				except: 
					print("You spelled something wrong. Try again.")
					replacing = []
					replacing_indexes = []
					continue
				if len(replacing) == 0: 
					print("You are keeping all dice...")
					break;
				print("Replacing dice...")
				keeping = []

				for index in (set([0,1,2,3,4]) - set(replacing_indexes)):
					keeping.append(dice[index])

				new_dice = roll_dice(len(replacing))

				for new_die in new_dice:
					keeping.append(new_die)

				current_dice = keeping
				replacing = []
				replacing_indexes = []
				rolls += 1
		print("Your new roll was: \n" %(dice))


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



