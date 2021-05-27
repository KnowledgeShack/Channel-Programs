import random

# Initialization
playerScore = 0
cpuScore = 0

choices = ['Rock', 'Paper', 'Scissors']

# Print statements
win = 'You scored a point!'
lose = 'The CPU scored a point!'
draw = 'A tie! No one was awarded points!'

playUntil = int(input('How many points do you want to play until? '))

while playerScore < playUntil and cpuScore < playUntil:
    # Getting the input
    player = input('''Please enter your choice
    (Choose between Rock, Paper, or Scissors with the same syntax): ''')
    
    # CPU's choice
    cpu = random.choice(choices)
    
    # Print CPU's choice
    
    print("The CPU's choice was " + cpu + '.')
    
    # If player chooses rock
    if player == 'Rock':
        if cpu == 'Paper':
            print(lose)
            cpuScore += 1
        
        if cpu == 'Rock':
            print(draw)
        
        if cpu == 'Scissors':
            print(win)
            playerScore += 1
            
    # If player chooses paper
    if player == 'Paper':
        if cpu == 'Paper':
            print(draw)
        
        if cpu == 'Rock':
            print(win)
            playerScore += 1
        
        if cpu == 'Scissors':
            print(lose)
            cpuScore += 1
            
    # If player chooses scissors
    if player == 'Scissors':
        if cpu == 'Paper':
            print(win)
            playerScore += 1
        
        if cpu == 'Rock':
            print(lose)
            cpuScore += 1

        if cpu == 'Scissors':
            print(draw)
    
    print('Your score: ' + str(playerScore))
    print("CPU's score: " + str(cpuScore))
    
if playerScore == playUntil:
    print('Congratulations! You won!')
    
if cpuScore == playUntil:
    print('Oh no! You lost!')