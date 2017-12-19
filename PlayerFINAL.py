import random

class Player: 

	def __init__(self, name, score1, score2, score3, score4, score5, score6, scorethreeofakind, scorefourofakind, scoresmall_straight, scorelarge_straight, scoreFullHouse, scoreYahtzee, score_chance):
		#multiple players, multiple names
		self.name = name 
		self.score1 = score1
		self.score2 = score2
		self.score3 = score3
		self.score4 = score4
		self.score5 = score5
		self.score6 = score6
		self.scorethreeofakind = scorethreeofakind
		self.scorefourofakind = scorefourofakind
		self.scoresmall_straight = scoresmall_straight
		self.scorelarge_straight= scorelarge_straight
		self.scoreFullHouse = scoreFullHouse
		self.scoreYahtzee = scoreYahtzee
		self.score_chance = score_chance


	def roll(self):
			#dice class, dice list needs to be global since it will be used to check scores
			global dice
			self.dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
			self.dice = sorted(self.dice)
			print(self.dice)
	def roll_replace(self):
		i = 1
		while i < 3: 
			result = input("What number dice do you want to reroll? (1-5) (Separate numbers with a space)(Leave blank for no reroll)")
			result2 = list(map(int, result.split()))
			x = 0
			while x < len(result2):
				self.dice[result2[x]-1] = random.randint(1,6)
				x += 1
				print(sorted(self.dice))
			i += 1
		print(sorted(self.dice))
	'''		
	def roll_replace(self):


		result = input("Do you want to keep these dice? (y or n)?")
		result = result.lower()
		rolls = 0
		if result == "y":
			return None
		#if the player wants to roll dice again...
		if result == "n":
			pick = 1
			rolls = 1
			while pick <= 5 and rolls <= 3:
				replaceNums = input("Type the ordinal numbers (first position would be 1, second would be 2) \n dice to replace...type done when done\n")
				if replaceNums == '1': 
					removed1 = dice.pop(0)
					existent = print(dice)
					new = dice.append(self.roll_dice(1))
					print(dice)
					pick += 1
					return removed1
				elif replaceNums == '2': 
					removed2 = dice.pop(1)
					print(dice)
					pick += 1
					return removed2
				elif replaceNums == '3': 
					removed3 = dice.pop(2)
					print(dice)
					pick += 1
					return removed3
				elif replaceNums == '4':
					removed4 = dice.pop(3)
					print(dice)
					pick += 1
					return removed4
				elif replaceNums == '5': 
					removed5 = dice.pop(4)
					print(dice)
					pick += 1
					return removed5
				elif replaceNums == 'done' or replaceNums == "Done":
					keeping =[]
					self.roll_dice(pick)
					new_dice = dice + keeping 
					rolls += 1
					break
		'''		
	

	#check dice list for given number and add them all up
	def checkOne(self, score1): 
		if self.dice.count(1) > 0:
			self.score1 += self.dice.count(1)*1/2
			return self.score1
		else: 
			self.score1 += 0
			return self.score1
	def checkTwo(self, score2): 
		if self.dice.count(2) > 0:
			self.score2 += self.dice.count(2)*2/2
			return self.score2
		else: 
			self.score2 += 0
			return self.score2
	def checkThree(self, score3): 
		if self.dice.count(3) > 0:	
			self.score3 += self.dice.count(3)*3/2
			return self.score3
		else: 
			self.score3 += 0
			return self.score3
	def checkFour(self, score4): 
		if self.dice.count(4) > 0:
			self.score4 += self.dice.count(4)*4/2
			return self.score4
		else: 
			self.score4 += 0
			return self.score4
	def checkFive(self, score5): 
		if self.dice.count(5) > 0:
			self.score5 += self.dice.count(5)*5/2
			return self.score5
		else: 
			self.score5 += 0
			return self.score5
	def checkSix(self, score6): 
		if self.dice.count(6) > 0:
			self.score6 += self.dice.count(6)*6/2
			return self.score6
		else: 
			self.score6 += 0
			return self.score6
	#check three of a kind
	def checkthreeofakind(self, scorethreeofakind):
	#add up all the dice in the list if there is at least a three of a kind
		for number in self.dice: 
			if self.dice.count(number) >= 3: 
				self.scorethreeofakind += sum(self.dice)
				return self.scorethreeofakind
			else: 
				self.scorethreeofakind += 0
				return self.scorethreeofakind

	def checkfourofakind(self, scorefourofakind): 
	#add up all the dice if there is at least a four of a kind
		for number in self.dice: 
			if self.dice.count(number) >= 4: 
				self.scorefourofakind += sum(self.dice)
				return self.scorefourofakind
			else:
				self.scorefourofakind += 0
				return self.scorefourofakind

	def checkYahtzee(self, scoreYahtzee):
	#if there is a yahtzee, you will be awarded points based off your first or second time
		for number in self.dice: 
			if self.dice.count(number) == 5: 
				if yahtzeeWin:
					self.scoreYahtzee += 100
					return self.scoreYahtzee
				else:
					yahtzeeWin = True
					self.scoreYahtzee += 50
					return self.scoreYahtzee
			else: 
				self.scoreYahtzee += 0
				return self.scoreYahtzee

	#check for full house numbers in the dice and award 25 points if full house exists
	#otherwise, award 0 points
	def checkFullHouse(self, scoreFullHouse):
		for num in self.dice: 
			if self.dice.count(num) == 3 or self.dice.count(num) == 2:
				for second_num in self.dice: 
					if self.dice.count(second_num) == 3 or self.dice.count(second_num) == 2:
						self.scoreFullHouse += 25
						return self.scoreFullHouse
			else: 
				self.scoreFullHouse += 0
				return self.scoreFullHouse

	
	def small_straight(self, scoresmall_straight):
		sortArray = list(set(self.dice))
		if sortArray == [1,2,3,4] or sortArray == [2,3,4,5] or sortArray == [3,4,5,6]:
			self.scoresmall_straight += 30/2
			return self.scoresmall_straight
		else: 
			self.scoresmall_straight += 0
			return self.scoresmall_straight

	def large_straight(self, scorelarge_straight):
		sortArray = list(set(self.dice))
		if sortArray == [1,2,3,4,5] or sortArray == [2,3,4,5,6]:
			self.scorelarge_straight += 40/2
			return self.scorelarge_straight
		else: 
			self.scorelarge_straight += 0
			return self.scorelarge_straight
	def chance(self, score_chance):
		chance = sum(self.dice)
		self.score_chance += chance
		return self.score_chance

