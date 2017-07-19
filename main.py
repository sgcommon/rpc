from os import system
import random

choices = ["rock", "paper", "scissors"]

def say(something):
    system('say "%s"' % something)

def getPlayerChoice():
	print("Enter your choice (rock/paper/scissors):")
	say("Enter your choice")
	choice = raw_input('-> ').lower()
	while choice not in ('rock', 'paper', 'scissors'):
		print("%s is not a valid choice, try again" % choice)
		say("%s is not a valid choice, try again" % choice)
		print("Enter your choice (rock/paper/scissors):")
		say("Enter your choice")
		choice = raw_input('-> ').lower()
	print ("playerChoice: %s " % choice)
	say("You chose %s, let's see if the computer can beat you" % choice)
	return choice

def getComputerChoice():
	choice = random.choice(choices)
	print ("computerChoice: %s " % choice)
	say("The computer chose %s" % choice)
	return choice

def updateScore(player_choice, computer_choice):
	global playerScore
	global computerScore
	if player_choice == computer_choice:
		say("It's a draw")
	elif (player_choice == 'rock' and computer_choice == 'paper'):
		say("Sorry you lose")
		computerScore +=1
	elif (player_choice == 'rock' and computer_choice == 'scissors'):
		say("Congratulations you win")
		playerScore +=1
	elif (player_choice == 'scissors' and computer_choice == 'paper'):
		say("Congratulations you win")
		playerScore +=1
	elif (player_choice == 'scissors' and computer_choice == 'rock'):
		say("Sorry, you lose")
		computerScore+=1
	elif (player_choice == 'paper' and computer_choice == 'rock'):
		say("Congratulations you win")
		playerScore+=1
	elif (player_choice == 'paper' and computer_choice == 'scissors'):
		say("Sorry, you lose")
		computerScore+=1
	print("Current score: You - %d, Computer - %d" % (playerScore, computerScore))

def playAgain():
	print("Play again (yes/no)?")
	say("Would you like to play again")
	answer = raw_input('-> ').lower()
	if answer == 'yes':
		return 0
	elif answer == 'no':
		say("Thanks for playing")
		print("Thanks for playing! Final score: You - %d, Computer - %d" % (playerScore, computerScore))
		return 1

first_line = "You joined Rock, Paper, Scissors.  Lets play."
print(first_line)
say(first_line)
playerScore = 0
computerScore = 0
finished = 0

while not finished:
	player_choice = getPlayerChoice()
	computer_choice = getComputerChoice()
	updateScore(player_choice, computer_choice)
	finished = playAgain()

