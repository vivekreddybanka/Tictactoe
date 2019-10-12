TicTacToeBoard = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
player1loc = []
player2loc = []
iMoviesCount = 0
bwhileCondition = True
bTrunFlag = True
bPlay = True
iPlayerOneScore = 0
iPlayerTwoScore = 0

""" function to print the board"""
def PrintTicTacToeBoard():
    for row in range(3):
         print('{} | {} | {}'.format(TicTacToeBoard[row][0],TicTacToeBoard[row][1],TicTacToeBoard[row][2]))
           

""" function to insert values in the board"""          
def InsertInTicTactoeBoard(iPosition,bTrun):
    if (iPosition >=0 and iPosition <= 9):
        iRow = iPosition // 3
        iCol = iPosition % 3
        if (bTrun):
            if (player1loc.count(iPosition) > 0 or player2loc.count(iPosition) > 0):
                return False
            else:
                player1loc.append(iPosition)
                TicTacToeBoard[iRow][iCol] = 'x'
                return True
        else:
            if (player1loc.count(iPosition) > 0 or player2loc.count(iPosition) > 0):
                return False
            else:
                player2loc.append(iPosition)
                TicTacToeBoard[iRow][iCol] = 'o'
                return True
    else:
        print('Position value should be in range 0-9')

def IncPlayerOne():
    global iPlayerOneScore 
    iPlayerOneScore = iPlayerOneScore + 1
def IncPlayerTwo():
    global iPlayerTwoScore
    iPlayerTwoScore =iPlayerTwoScore + 1

""" function to calculate the player scores"""
def CalculatePlayerScores():
    global bwhileCondition
    if (bTrunFlag == True):
        sSearchChar = 'x'
    else:
        sSearchChar = 'o'
    if (iMoviesCount > 4):
        for row in range(3):
            if(TicTacToeBoard[row][0]==sSearchChar and TicTacToeBoard[row][1] == sSearchChar and TicTacToeBoard[row][2] == sSearchChar):
                if(bTrunFlag):
                    IncPlayerOne()
                    determineWinner()
                    bwhileCondition = False
                    return
                else:
                    IncPlayerTwo()
                    determineWinner()
                    bwhileCondition = False
                    return
            if(TicTacToeBoard[0][row]==sSearchChar and TicTacToeBoard[1][row] == sSearchChar and TicTacToeBoard[2][row] == sSearchChar):
                if(bTrunFlag):
                    IncPlayerOne()
                    determineWinner()
                    bwhileCondition = False
                    return
                else:
                    IncPlayerTwo()
                    determineWinner()
                    bwhileCondition = False
                    return
        if (TicTacToeBoard[0][0]==sSearchChar and TicTacToeBoard[1][1] == sSearchChar and TicTacToeBoard[2][2] == sSearchChar):
            if(bTrunFlag):
                IncPlayerOne()
                determineWinner()
                bwhileCondition = False
                return
            else:
                IncPlayerTwo()
                determineWinner()
                bwhileCondition = False
                return
        if (TicTacToeBoard[0][2]==sSearchChar and TicTacToeBoard[1][1] == sSearchChar and TicTacToeBoard[2][0] == sSearchChar):
            if(bTrunFlag):
                IncPlayerOne()
                determineWinner()
                bwhileCondition = False
                return
            else:
                IncPlayerTwo()
                determineWinner()
                bwhileCondition = False
                return
    else:
        return
""" function to reset board"""
def resetBoard():
    TicTacToeBoard = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
    ]
    player1loc = []
    player2loc = []
    iMoviesCount = 0
    bwhileCondition = True
    bTrunFlag = True
    bPlay = True
    iPlayerOneScore = 0
    iPlayerTwoScore = 0

""" fucntio to determine the winner"""
def determineWinner():
    if (iMoviesCount >4):
        if(iPlayerOneScore == iPlayerTwoScore):
            print('Well Played Player - Your Score are Draw')
            print('player 1 score: {} player 2 score: {} '.format(iPlayerOneScore, iPlayerTwoScore))
            userInput = input('Want to play again y/n?')
            if(userInput.lower == 'y'):
                resetBoard()
            else:
                return 
        elif (iPlayerOneScore > iPlayerTwoScore):
            print('Well Played Player - Your player 1 wins')
            print('player 1 score: {} player 2 score: {} '.format(iPlayerOneScore, iPlayerTwoScore))
        else:
            print('Well Played Player - Your player 2 wins')
            print('player 1 score: {} player 2 score: {} '.format(iPlayerOneScore, iPlayerTwoScore))
    else:
        return

""" Ask the player for the input"""
while(bwhileCondition):
    if bPlay :
        uInput = input('Do you want to continue play y/n ?')
        bPlay = False if uInput.lower() == 'y' else True
        if uInput.lower() == 'n':
            bwhileCondition = False
        else:
            PrintTicTacToeBoard()
    else:
        if (bTrunFlag):
            p1Input = input('Enter a Position for Player 1!')
            try:
                p1Input = int(p1Input)
                if InsertInTicTactoeBoard(p1Input,bTrunFlag) :
                    PrintTicTacToeBoard()
                    iMoviesCount += 1
                    CalculatePlayerScores()
                    bTrunFlag = False
                else:
                    print('Entered Postion is already taken')
                
            except Exception as e:
                print(e)
                print('Enter numeric value')
                continue
        else:
            p2Input = input('Enter a Position for Player 2!')
            try:
                p2Input = int(p2Input)
                if InsertInTicTactoeBoard(p2Input,bTrunFlag) :
                    iMoviesCount += 1
                    PrintTicTacToeBoard()
                    CalculatePlayerScores()
                    bTrunFlag = True
                else:
                    print('Entered Position is already taken')
            except Exception as e:
                print('enter a numeric value')
                continue
    if iMoviesCount > 8:
        bwhileCondition = False
        determineWinner()

    
        



                  


