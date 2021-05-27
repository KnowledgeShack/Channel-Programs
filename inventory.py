# Program gives options for an inventory
# inventory = {"Apple": 0, "Banana": 0, "Orange": 0}

# Imports
import json

# Opens file for the first time
with open('fruits.json') as json_file:
    data = json.load(json_file)
    for i in data:
        print(i + ': ' + str(data[i]))

# Setting dict our program can deal with to the data
inventory = data

# Initializing
running = True

json_file.close()

# Main loop
while running:
    
    # Input selection
    selection = int(input('''Enter the action you would like to do. 1 to remove, 2 to add, 3 to check how many for each type, and 4 to stop the program. '''))
    
    # If you want to remove
    if selection == 1:
        input1 = input('''What fruit would you like to remove from and how many?
(Enter the name of the fruit and the number seperated with a comma) Ex. Apple, 3. ''')
        
        fruitName1 = input1.split(', ')[0]        # Takes name of fruit
        fruitNum1 = int(input1.split(', ')[1])    # Takes number of fruit (str converted into int)
        
        if fruitName1 in inventory:
            if isinstance(inventory[fruitName1], int):                             # Checks if vslue is an integer
                if inventory[fruitName1] - int(fruitNum1) >= 0:                    # Checks if there is enough inventory to remove
                    inventory[fruitName1] = inventory[fruitName1] - int(fruitNum1) # Takes away
                    print('Okay!')
                else:
                    print('Not enough to remove.')
        else:
            print('That is not a valid fruit name.')
    
    # If you choose to add
    if selection == 2:
        input2 = input('''What fruit would you like to add to and how many?
(Enter the name of the fruit and the number seperated with a comma) Ex. Apple, 3. ''')
        
        fruitName2 = input2.split(', ')[0]
        fruitNum2 = int(input2.split(', ')[1])
        
        if fruitName2 in inventory:
            if isinstance(inventory[fruitName2], int):
                if inventory[fruitName2] + fruitNum2 >= 0:
                    inventory[fruitName2] = inventory[fruitName2] + fruitNum2
                    print('Okay!')
                else:
                    print('Not enough to remove.')
        else:
            print('That is not a valid fruit name.')
    
    # If you choose to check
    if selection == 3:
        for i in inventory:
            print(i + ': ' + str(inventory[i]))
    
    # If you want to end it
    if selection == 4:
        myFile = open('fruits.json', 'w')
        myFile.truncate(0)                      # Clears File
        jsonString = json.dumps(inventory)      # Turns dict Inventory into a string
        myFile.write(jsonString)                # Writes string into file
        running = False                         # Loop won't run again
        myFile.close()                          # Closes the file