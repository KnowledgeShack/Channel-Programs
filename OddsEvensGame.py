import random

print('')
p1Name = input("What is Player 1's name? ")
p2Name = input("What is Player 2's name? ")

persontoChoose = random.randint(1, 2)

if persontoChoose == 1:
    p1choice = input(p1Name + ', you get to choose. Odds, or even? ')
    p1choice = p1choice.lower()
    if p1choice == 'odds':
        p2choice = 'even'
    if p1choice == 'even':
        p2choice = 'odds'
        
if persontoChoose == 2:
    p2choice = input(p2Name + ', you get to choose. Odds, or even? ')
    p2choice = p2choice.lower()
    if p2choice == 'odds':
        p1choice = 'even'
    if p2choice == 'even':
        p1choice = 'odds'
        
        
p1Num = int(input(p1Name + ', what number do you choose? (From 1 to 5) '))
for i in range(20):
    print('')
p2Num = int(input(p2Name + ', what number do you choose? (From 1 to 5) '))

numSum = p1Num + p2Num

if numSum % 2 == 0:
    even = True
    odds = False

elif numSum % 2 == 1:
    odds = True
    even = True
    
if p1choice == 'odds' and odds:
    print('Congratulations ' + p1Name + ', you won!')
elif p1choice == 'even' and even:
    print('Congratulations ' + p1Name + ', you won!')
if p2choice == 'odds' and odds:
    print('Congratulations ' + p2Name + ', you won!')
elif p2choice == 'even' and even:
    print('Congratulations ' + p2Name + ', you won!')