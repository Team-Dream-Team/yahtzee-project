from random import random
class Dice():
		def __init__(self):
			self.diceList = [randint(1,6), randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
			print(self.diceList)
            
		def roll_replace(self):
			x = 1
			while x < 3:
				ans = str(input("What number dice do you want to reroll? (1-5) (Separate numbers with a space) (Leave blank for no reroll)"))   
				ans2 = list(map(int, ans.split()))  
				i = 0
				while i < len(ans2):
					self.diceList[i-1] = randint(1,6)
					i += 1
				x += 1
				print(self.diceList)

