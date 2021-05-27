# Code by Ryvaan Das
# Take input from user (2 numbers) & Initialization
x = int(input('Enter the first number: '))
if x < 0:
    print('Please enter a different number.')   
y = int(input('Enter the second number: '))
if y < 0:
    print('Please enter a different number.')
gcd = 1

# Bigger or smaller
if x > y:
    bigger = x
    smaller = y
elif x < y:
    bigger = y
    smaller = x
else:
    gcd = x

# Main Division Loop
for i in range(1, smaller + 1):
    if smaller % i == 0:
        if bigger % i == 0:
            gcd = i

# Output GCD
print('The GCD of ' + str(x) + ' and ' + str(y) + ' is ' + str(gcd) + '.')


