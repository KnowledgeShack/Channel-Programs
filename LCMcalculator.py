# Code by Ryvaan Das
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

# Identifying the greater number
if x > y:
    greater = x
    smaller = y
elif y > x:
    greater = y
    smaller = x
else:
    greater = y
    smaller = x
    
# Main LCM Finding Loop
for i in range(1, smaller + 1):
    if (greater * i) % smaller == 0:
        print('The LCM is ' + str((greater * i)) + '.')
        break
    
    
