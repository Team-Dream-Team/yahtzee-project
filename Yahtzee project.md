# Yahtzee outline

## Classes -
Two classes: player and Dice
### Player
Player class contains all methods of scoring of dice rolls on the scoreboard   
   
   **Top Scoreboard**
* Ones
	* stores the values of ones
* Twos
	* stores the values of twos
* Threes
	* stores the values of threes
* Fours
	* stores the values of fours
* Fives
	* stores the values of fives
* Sixes
	* stores the values of sixes
   
   **Bottom Scoreboard**
* Three of a kind
	* adds up total on dice if they have three
* Four of a Kind
	* adds up total on dice if they have four
* Full house
	* adds 25 points if they have 2 of one, and 3 of another
* Small Straight
	* adds 30 points if they have 4 scaling dice
* Large Straight
	* adds 40 points if they have 1,2,3,4,5, or 2,3,4,5,6
* chance
	* add total of dice
* Yahtzee
	* adds 50 points if they roll 5 of the same the first time
	* adds 100 points if they roll five of the same the next 3 times
### Dice
Keeps track of rolls and values
* Roll
	* generates a random integer between one and six for each die

## Main Code:
![Outline] (https://github.com/Team-Dream-Team/yahtzee-project/blob/master/Hand_Drawn_Outline.jpeg)
