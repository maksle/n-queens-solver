def update_attacks(x, y, n, squares, fn=operator.add):
    """Update attacks, either removing or adding the attacks from a queen in the
    x, y position. Note x and y are transposed from their typical meaning."""
    i = x
    while i - 1 >= 0:
        i -= 1
        squares[i][y] = fn(squares[i][y], 1)
    i = x
    while i + 1 < n:
        i += 1
        squares[i][y] = fn(squares[i][y], 1)
    j = y
    while j - 1 >= 0:
        j -= 1
        squares[x][j] = fn(squares[x][j], 1)
    j = y
    while j + 1 < n:
        j += 1
        squares[x][j] = fn(squares[x][j], 1)
    i, j = x, y
    while i - 1 >= 0 and j - 1 >= 0:
        i -= 1
        j -= 1
        squares[i][j] = fn(squares[i][j], 1)
    i, j = x, y
    while i - 1 >= 0 and j + 1 < n:
        i -= 1
        j += 1
        squares[i][j] = fn(squares[i][j], 1)
    i, j = x, y
    while i + 1 < n and j + 1 < n:
        i += 1
        j += 1
        squares[i][j] = fn(squares[i][j], 1)
    i, j = x, y
    while i + 1 < n and j - 1 >= 0:
        i += 1
        j -= 1
        squares[i][j] = fn(squares[i][j], 1)

def queen_attacks(s):
    """Returns # of attacks of square for each square.
    Pseudo b/c not looking at the effect of blockers.
    Also returns a square based representation of the state.
    """
    n = len(s)
    squares = [[0]*n for _ in range(n)]
    for x,y in s:
        update_attacks(x, y, n, squares, operator.add)
    return squares

def num_queens_attacked(s, attacks):
    """Returns # of queens pseudo-attacked by other queens. 
    Doesn't consider effect of blockers."""
    return sum(attacks[x][y] for x,y in s)

def greedy_choice(s, attacks, row):
    """Returns lowest attacked square in the row"""
    cols = attacks[row]
    least = float('inf')
    choice = None
    for i, nb_attack in enumerate(cols):
        if nb_attack < least:
            least = nb_attack
            choice = i
    return choice, least
        
def random_board(n):
    """Generates a random board with one queen per row"""
    return [(r, random.randint(0, n-1)) for r in range(n)]

def perturb(s, k=7):
    n = len(s)
    adjustments = [(random.randint(0, n-1), random.randint(0, n-1))
                   for ki in range(k)]
    res = []
    for adjustment in adjustments:
        snew = s[:]
        snew[adjustment[0]] = adjustment
        res.append(snew)
    return res

import os
def hill_climb(input, output):
    """Finds an n-queens solution"""
    for s in iter(input.get, 'STOP'):
        attacks = queen_attacks(s)
        for i in range(300):
            if num_queens_attacked(s, attacks) == 0:
                output.put((True, s))
                break
            if random.random() < 0.1:
                rand_row, next_col = random.randint(0,7), random.randint(0,7)
            else:
                rand_row = random.randint(0, n-1)
                next_col, val = greedy_choice(s, attacks, rand_row)
            curr_col = s[rand_row][1]
            if curr_col != next_col:
                update_attacks(rand_row, curr_col, n, attacks, operator.sub)
                s[rand_row] = rand_row, next_col
                update_attacks(rand_row, next_col, n, attacks, operator.add)
        else:
            output.put((False, s))

def print_board(s):
    """Print board to stdout"""
    n = len(s)
    board = [[" - "]*n for _ in range(n)]
    for x, y in s:
        board[x][y] = " Q "
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="")
            if j == n-1: print("\n")         
