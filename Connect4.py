def print_board(board):
    '''print_board(board) -> str
    returns a string that represents the Connect 4 Board'''
    boardString = '\n'
    for col in range(7):
        boardString += str(col) + ' '
    
    for row in range(6):
        for col in range(7):
            boardString += board[row][col] + ' '
        boardString += '\n'
    
    return boardString

def check_line_for_win(board, r, c, dr, dc, piece):
    '''check_line_for_win(board, r, c, dr, dc, piece) -> bool
    returns True if piece has a winning line
    starts at row r, col c, and moves in direction given by dr and dc'''
    for i in range(4):
        if board[r + i * dr][c + i * dc] != piece:
            return False
    return True

def check_for_win(board, piece):
    '''check_for_win(board, piece) -> bool
    returns True if piece has a winning line on the board'''
    # Check horizontally
    for row in range(6):
        for col in range(4):
            if check_line_for_win(board, row, col, 0, 1, piece):
                return True
    # Check vertically
    for row in range(3):
        for col in range(7):
            if check_line_for_win(board, row, col, 1, 0, piece):
                return True
            
    # Check NW - SE diag
    for row in range(3):
        for col in range(4):
            if check_line_for_win(board, row, col, 1, 1, piece):
                return True
            
    # Check NE - SW diag
    for row in range(3, 6):
        for col in range(4):
            if check_line_for_win(board, row, col, -1, 1, piece):
                return True
            
    return False

def play_connect_four():
    # Initialization
    playerNames = []
    playerNames.append(input('Player X, enter your name: '))
    playerNames.append(input('Player O, enter your name: '))
    pieces = ['X', 'O']
    turn = 0
    turns = 0
    # Set up a blank board
    boardRow = ['.'] * 7
    board = []
    for i in range(6):
        board.append(boardRow)
        
    # Initialize column heights
    # Initializes number of pieces in each column
    columnHeights = [0] * 7
    
    while turns < 42:
        print(print_board(board))
        legalPlay = False
        while not legalPlay:
            play = input(playerNames[turn] + ", you're " + pieces[turn] + '.' + "Which column would you like to play in? ")
            if not play.isdigit():
                print("That is not a vaild column. Please choose again. ")
            else:
                play = int(play)
                if play < 0 or play > 6:
                    print("That is not a vaild column. Please choose again. ")
                elif columnHeights[play] == 6:
                    print("That column is full. Please choose again. ")
                else:
                    legalPlay = True
                    
        # Make the play
        height = 5-columnHeights[play]
        board[height][play] = pieces[turn]
        columnHeights[play] += 1
        winner = check_for_win(board, pieces[turn])
        if winner:
            print(print_board(board))
            print("Congratulations, " + str(playerNames[turn]) + " , you won! ")
            break
        turn = (turn + 1) % 2
        turns += 1
    if turns == 42:
        print(print_board())
        print("It's a tie!")
    
play_connect_four()