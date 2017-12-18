import random

class Player: 

	def __init__(self, name, score):
		#multiple players, multiple names
		self.name = name 
		self.score = score

	def roll_dice():
		#dice class, dice list needs to be global since it will be used to check scores
		global dice
		dice = []
		for i in range(5):
			dice += [random.randint(1,6)]
			dice = sorted(dice)
			print(dice)	
		return dice
	#check dice list for given number and add them all up
	def checkOne(score1): 
		if self.dice.count(1) > 0:
			self.score1 += self.dice.count(1)*1
		else: 
			self.score1 += 0
	def checkTwo(score2): 
		if self.dice.count(2) > 0:
			self.score2 += self.dice.count(2)*2
		else: 
			self.score2 += 0
	def checkThree(score3): 
		if self.dice.count(3) > 0:	
			self.score3 += self.dice.count(3)*3
		else: 
			self.score3 += 0
	def checkFour(score4): 
		if self.dice.count(4) > 0:
			self.score4 += self.dice.count(4)*4
		else: 
			self.score4 += 0
	def checkFive(score5): 
		if self.dice.count(5) > 0:
			self.score5 += self.dice.count(5)*5
		else: 
			self.score5 += 0
	def checkSix(score6): 
		if self.dice.count(1) > 0:
			self.score6 += self.dice.count(6)*6
		else: 
			self.score6 += 0
	#check three of a kind
	def checkthreeofakind(scorethreeofakind):
	#add up all the dice in the list if there is at least a three of a kind
		for number in dice: 
			if dice.count(number) >= 3: 
				self.scorethreeofakind += sum(dice)
			else: 
				self.scorethreeofakind += 0

	def checkfourofakind(scorefourofakind): 
	#add up all the dice if there is at least a four of a kind
		for number in dice: 
			if dice.count(number) >= 4: 
				self.scorefourofakind += sum(dice)
			else:
				self.scorefourofakind += 0

	def checkYahtzee(scoreYahtzee):
	#if there is a yahtzee, you will be awarded points based off your first or second time
		for number in dice: 
			if dice.count(number) == 5: 
				if yahtzeeWin:
					self.scoreYahtzee += 100
				else:
					yahtzeeWin = True
					self.scoreYahtzee += 50
			else: 
				self.scoreYahtzee += 0

	#check for full house numbers in the dice and award 25 points if full house exists
	#otherwise, award 0 points
	def checkFullHouse(scoreFullHouse):
		for num in dice: 
			if dice.count(num) == 3:
				for second_num in dice: 
					if dice.count(second_num) == 2:
						self.scoreFullHouse += 25
			else: 
				self.scoreFullHouse += 0

	
	def small_straight(scoresmall_straight):
		sortArray = list(set(dice))
		if sortArray == [1,2,3,4] or sortArray == [2,3,4,5] or sortArray == [3,4,5,6]:
			self.scoresmall_straight += 30
		else: 
			self.scoresmall_straight += 0
	def large_straight(scorelarge_straight):
		sortArray = list(set(dice))
		if sortArray == [1,2,3,4,5] or sortArray == [2,3,4,5,6]:
			self.scorelarge_straight += 40
		else: 
			self.scorelarge_straight += 0



	def stats(self):
		print("Name: " +self.name)
		print("Score:" +str(self.score))

Ben = Player('Ben', 0)
new_score = Player.roll_dice()

