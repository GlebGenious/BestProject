import random

EmptyBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}
board_keys = []
for key in EmptyBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def botMove():
    possible_moves = [key for key in EmptyBoard if EmptyBoard[key] == ' ']
    if possible_moves:
        move = random.choice(possible_moves)
        EmptyBoard[move] = 'O'
        return True
    else:
        return False
def game():
    cross = 'X'
    count = 0
    gameOver = False
    for i in range(9):
        printBoard(EmptyBoard)
        if cross == 'X':
            print("Сейчас ваша очередь, " + cross + ". Переместить в другое место")
            move = input()
            if EmptyBoard[move] == ' ':
                EmptyBoard[move] = cross
                count += 1
            else:
                print("Это место уже заполнено:( Переместить в другое место ?")
                continue
        else:
            print('щас робот ходит')
            botMoved = botMove()
            if botMoved:
                count += 1
        if count >= 5:
            if EmptyBoard['7'] == EmptyBoard['8'] == EmptyBoard['9'] != ' ':
                gameOver = True
            elif EmptyBoard['4'] == EmptyBoard['5'] == EmptyBoard['6'] != ' ':
                gameOver = True
            elif EmptyBoard['1'] == EmptyBoard['2'] == EmptyBoard['3'] != ' ':
                gameOver = True
            elif EmptyBoard['1'] == EmptyBoard['4'] == EmptyBoard['7'] != ' ':
                gameOver = True
            elif EmptyBoard['2'] == EmptyBoard['5'] == EmptyBoard['8'] != ' ':
                gameOver = True
            elif EmptyBoard['3'] == EmptyBoard['6'] == EmptyBoard['9'] != ' ':
                gameOver = True
            elif EmptyBoard['7'] == EmptyBoard['5'] == EmptyBoard['3'] != ' ':
                gameOver = True
            elif EmptyBoard['1'] == EmptyBoard['5'] == EmptyBoard['9'] != ' ':
                gameOver = True
            if gameOver:
                printBoard(EmptyBoard)
                print("Игра окончена.")
                if cross == 'X':
                    print(" **** Ура, ты выиграл ****")
                else:
                    print(" **** Блин,ты проиграл ****")
                break
        if count == 9:
            printBoard(EmptyBoard)
            print("Игра окончена")
            break
        if cross == 'X':
            cross = 'O'
        else:
            cross = 'X'
    restart = input("Еще каточку? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            EmptyBoard[key] = " "
        game()
if __name__ == "__main__":
    game()
