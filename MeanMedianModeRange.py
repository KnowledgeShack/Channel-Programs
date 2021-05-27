# Subscribe!

# Setup

import statistics

listSum = 0
s = input('Enter the list sepreated by commas: ')
l = s.split(', ')


# Mean
# Sum all the numbers
for i in l:
    listSum = listSum + int(i)
# Find length of list
listLen = len(l)

# Divide to find average
average = listSum/listLen

print('The average is ' + str(average) + '.')

# Median
1, 2, 3, 4, 5
# Order from least to greatest
lSorted = sorted(l)
# Find middle numbers
if listLen % 2 == 0:
    middleNumbers = [lSorted[listLen//2], lSorted[(listLen//2) - 1]]
    middleNumSum = 0
    for i in middleNumbers:
        middleNumSum += int(i)
    print('The median is ' + str(middleNumSum/2) + '.')
else:
    print('The median is ' + lSorted[(listLen - 1)//2] + '.')
    
# Mode
print('The mode is ' + str(statistics.mode(l)) + '.')

# Range
maxNum = int(max(l))
minNum = int(min(l))

print('The range is ' + str(maxNum - minNum) + '.')
# 2.2, 2, 1, 3
