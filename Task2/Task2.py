"""
Создайте программу для игры в ""Крестики-нолики"".
"""

# Это не мое решение. Я решить не смог. Код немного изменен от первоначального.

board = ['0','1','2','3','4','5','6','7','8']

def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end ='')

print_state(board)

win_comby = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def get_winner(state, comby):
    for (x, y, z) in comby:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''

def play_game(board):
    j = 0
    current_sign = 'X'
    while(get_winner(board, win_comby) == ''):
        index = int(input(f'Сделайте свой ход номером ячейки от 0 до 8. Ходят -  {current_sign} '))
        board[index] = current_sign
        j += 1
        print_state(board)

        winner_sign = get_winner(board, win_comby)
        if winner_sign != '':
            print(f'Вы победили: {winner_sign}!')
        current_sign = 'X' if current_sign == 'O' else 'O'
        if j == 9:
            print('Ничья!')
            break
play_game(board)
