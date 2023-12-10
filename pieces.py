class King:
    def __init__(self):
        self.value = 6
        self.notation = 'K'

    def movement(game, player, pos, capture=True):
        result = []
        if pos[1]+1 >= 0 and pos[1]+1 <= 7 and pos[0] >= 0 and pos[0] <= 7 and (game.board[pos[1]+1][pos[0]]*player < 0 or game.board[pos[1]+1][pos[0]] == 0):
            result.append((pos[0], pos[1]+1))
        if pos[1]-1 >= 0 and pos[1]-1 <= 7 and pos[0] >= 0 and pos[0] <= 7 and (game.board[pos[1]-1][pos[0]]*player < 0 or game.board[pos[1]-1][pos[0]] == 0):
            result.append((pos[0], pos[1]-1))
        if pos[1] >= 0 and pos[1] <= 7 and pos[0]+1 >= 0 and pos[0]+1 <= 7 and (game.board[pos[1]][pos[0]+1]*player < 0 or game.board[pos[1]][pos[0]+1] == 0):
            result.append((pos[0]+1, pos[1]))
        if pos[1] >= 0 and pos[1] <= 7 and pos[0]-1 >= 0 and pos[0]-1 <= 7 and (game.board[pos[1]][pos[0]-1]*player < 0 or game.board[pos[1]][pos[0]-1] == 0):
            result.append((pos[0]-1, pos[1]))
        if pos[1]+1 >= 0 and pos[1]+1 <= 7 and pos[0]+1 >= 0 and pos[0]+1 <= 7 and (game.board[pos[1]+1][pos[0]+1]*player < 0 or game.board[pos[1]+1][pos[0]+1] == 0):
            result.append((pos[0]+1, pos[1]+1))
        if pos[1]+1 >= 0 and pos[1]+1 <= 7 and pos[0]-1 >= 0 and pos[0]-1 <= 7 and (game.board[pos[1]+1][pos[0]-1]*player < 0 or game.board[pos[1]+1][pos[0]-1] == 0):
            result.append((pos[0]-1, pos[1]+1))
        if pos[1]-1 >= 0 and pos[1]-1 <= 7 and pos[0]+1 >= 0 and pos[0]+1 <= 7 and (game.board[pos[1]-1][pos[0]+1]*player < 0 or game.board[pos[1]-1][pos[0]+1] == 0):
            result.append((pos[0]+1, pos[1]-1))
        if pos[1]-1 >= 0 and pos[1]-1 <= 7 and pos[0]-1 >= 0 and pos[0]-1 <= 7 and (game.board[pos[1]-1][pos[0]-1]*player < 0 or game.board[pos[1]-1][pos[0]-1] == 0):
            result.append((pos[0]-1, pos[1]-1))
        if (pos == (4, 7) or pos == (4, 0)) and game.board[pos[1]][pos[0]+1] == 0 and game.board[pos[1]][pos[0]+2] == 0 and ((game.castling[0] == 1 and game.p_move == 1) or (game.castling[2] == 1 and game.p_move == -1)):
            result.append((pos[0]+2, pos[1]))
        if (pos == (4, 7) or pos == (4, 0)) and game.board[pos[1]][pos[0]-1] == 0 and game.board[pos[1]][pos[0]-2] == 0 and ((game.castling[1] == 1 and game.p_move == 1) or (game.castling[3] == 1 and game.p_move == -1)):
            result.append((pos[0]-2, pos[1]))
        return result

class Queen:
    def __init__(self):
        self.value = 5
        self.notation = 'Q'

    def movement(game, player, pos, capture=True):
        result = []
        check = [True, True, True, True, True, True, True, True]
        for c in range(1, 8, 1):
            if pos[1]+c >= 0 and pos[1]+c <= 7 and pos[0] >= 0 and pos[0] <= 7 and (game.board[pos[1]+c][pos[0]]*player < 0 or game.board[pos[1]+c][pos[0]] == 0) and check[0] == True:
                result.append((pos[0], pos[1]+c))
                if game.board[pos[1]+c][pos[0]]*player < 0 and capture == True:
                    check[0] = False
            else:
                check[0] = False
            if pos[1]-c >= 0 and pos[1]-c <= 7 and pos[0] >= 0 and pos[0] <= 7 and (game.board[pos[1]-c][pos[0]]*player < 0 or game.board[pos[1]-c][pos[0]] == 0) and check[1] == True:
                result.append((pos[0], pos[1]-c))
                if game.board[pos[1]-c][pos[0]]*player < 0 and capture == True:
                    check[1] = False
            else:
                check[1] = False
            if pos[1] >= 0 and pos[1] <= 7 and pos[0]+c >= 0 and pos[0]+c <= 7 and (game.board[pos[1]][pos[0]+c]*player < 0 or game.board[pos[1]][pos[0]+c] == 0) and check[2] == True:
                result.append((pos[0]+c, pos[1]))
                if game.board[pos[1]][pos[0]+c]*player < 0 and capture == True:
                    check[2] = False
            else:
                check[2] = False
            if pos[1] >= 0 and pos[1] <= 7 and pos[0]-c >= 0 and pos[0]-c <= 7 and (game.board[pos[1]][pos[0]-c]*player < 0 or game.board[pos[1]][pos[0]-c] == 0) and check[3] == True:
                result.append((pos[0]-c, pos[1]))
                if game.board[pos[1]][pos[0]-c]*player < 0 and capture == True:
                    check[3] = False
            else:
                check[3] = False
            if pos[1]+c >= 0 and pos[1]+c <= 7 and pos[0]+c >= 0 and pos[0]+c <= 7 and (game.board[pos[1]+c][pos[0]+c]*player < 0 or game.board[pos[1]+c][pos[0]+c] == 0) and check[4] == True:
                result.append((pos[0]+c, pos[1]+c))
                if game.board[pos[1]+c][pos[0]+c]*player < 0 and capture == True:
                    check[4] = False
            else:
                check[4] = False
            if pos[1]+c >= 0 and pos[1]+c <= 7 and pos[0]-c >= 0 and pos[0]-c <= 7 and (game.board[pos[1]+c][pos[0]-c]*player < 0 or game.board[pos[1]+c][pos[0]-c] == 0) and check[5] == True:
                result.append((pos[0]-c, pos[1]+c))
                if game.board[pos[1]+c][pos[0]-c]*player < 0 and capture == True:
                    check[5] = False
            else:
                check[5] = False
            if pos[1]-c >= 0 and pos[1]-c <= 7 and pos[0]+c >= 0 and pos[0]+c <= 7 and (game.board[pos[1]-c][pos[0]+c]*player < 0 or game.board[pos[1]-c][pos[0]+c] == 0) and check[6] == True:
                result.append((pos[0]+c, pos[1]-c))
                if game.board[pos[1]-c][pos[0]+c]*player < 0 and capture == True:
                    check[6] = False
            else:
                check[6] = False
            if pos[1]-c >= 0 and pos[1]-c <= 7 and pos[0]-c >= 0 and pos[0]-c <= 7 and (game.board[pos[1]-c][pos[0]-c]*player < 0 or game.board[pos[1]-c][pos[0]-c] == 0) and check[7] == True:
                result.append((pos[0]-c, pos[1]-c))
                if game.board[pos[1]-c][pos[0]-c]*player < 0 and capture == True:
                    check[7] = False
            else:
                check[7] = False
            if True not in check:
                break
        return result

class Rook:
    def __init__(self):
        self.value = 4
        self.notation = 'R'

    def movement(game, player, pos, capture=True):
        result = []
        check = [True, True, True, True]
        for c in range(1, 8, 1):
            if pos[1]+c >= 0 and pos[1]+c <= 7 and pos[0] >= 0 and pos[0] <= 7 and (game.board[pos[1]+c][pos[0]]*player < 0 or game.board[pos[1]+c][pos[0]] == 0) and check[0] == True:
                result.append((pos[0], pos[1]+c))
                if game.board[pos[1]+c][pos[0]]*player < 0 and capture == True:
                    check[0] = False
            else:
                check[0] = False
            if pos[1]-c >= 0 and pos[1]-c <= 7 and pos[0] >= 0 and pos[0] <= 7 and (game.board[pos[1]-c][pos[0]]*player < 0 or game.board[pos[1]-c][pos[0]] == 0) and check[1] == True:
                result.append((pos[0], pos[1]-c))
                if game.board[pos[1]-c][pos[0]]*player < 0 and capture == True:
                    check[1] = False
            else:
                check[1] = False
            if pos[1] >= 0 and pos[1] <= 7 and pos[0]+c >= 0 and pos[0]+c <= 7 and (game.board[pos[1]][pos[0]+c]*player < 0 or game.board[pos[1]][pos[0]+c] == 0) and check[2] == True:
                result.append((pos[0]+c, pos[1]))
                if game.board[pos[1]][pos[0]+c]*player < 0 and capture == True:
                    check[2] = False
            else:
                check[2] = False
            if pos[1] >= 0 and pos[1] <= 7 and pos[0]-c >= 0 and pos[0]-c <= 7 and (game.board[pos[1]][pos[0]-c]*player < 0 or game.board[pos[1]][pos[0]-c] == 0) and check[3] == True:
                result.append((pos[0]-c, pos[1]))
                if game.board[pos[1]][pos[0]-c]*player < 0 and capture == True:
                    check[3] = False
            else:
                check[3] = False
            if True not in check:
                break
        return result

class Bishop:
    def __init__(self):
        self.value = 3
        self.notation = 'B'

    def movement(game, player, pos, capture=True):
        result = []
        check = [True, True, True, True]
        for c in range(1, 8, 1):
            if pos[1]+c >= 0 and pos[1]+c <= 7 and pos[0]+c >= 0 and pos[0]+c <= 7 and (game.board[pos[1]+c][pos[0]+c]*player < 0 or game.board[pos[1]+c][pos[0]+c] == 0) and check[0] == True:
                result.append((pos[0]+c, pos[1]+c))
                if game.board[pos[1]+c][pos[0]+c]*player < 0 and capture == True:
                    check[0] = False
            else:
                check[0] = False
            if pos[1]+c >= 0 and pos[1]+c <= 7 and pos[0]-c >= 0 and pos[0]-c <= 7 and (game.board[pos[1]+c][pos[0]-c]*player < 0 or game.board[pos[1]+c][pos[0]-c] == 0) and check[1] == True:
                result.append((pos[0]-c, pos[1]+c))
                if game.board[pos[1]+c][pos[0]-c]*player < 0 and capture == True:
                    check[1] = False
            else:
                check[1] = False
            if pos[1]-c >= 0 and pos[1]-c <= 7 and pos[0]+c >= 0 and pos[0]+c <= 7 and (game.board[pos[1]-c][pos[0]+c]*player < 0 or game.board[pos[1]-c][pos[0]+c] == 0) and check[2] == True:
                result.append((pos[0]+c, pos[1]-c))
                if game.board[pos[1]-c][pos[0]+c]*player < 0 and capture == True:
                    check[2] = False
            else:
                check[2] = False
            if pos[1]-c >= 0 and pos[1]-c <= 7 and pos[0]-c >= 0 and pos[0]-c <= 7 and (game.board[pos[1]-c][pos[0]-c]*player < 0 or game.board[pos[1]-c][pos[0]-c] == 0) and check[3] == True:
                result.append((pos[0]-c, pos[1]-c))
                if game.board[pos[1]-c][pos[0]-c]*player < 0 and capture == True:
                    check[3] = False
            else:
                check[3] = False
            if True not in check:
                break
        return result
    
class Knight:
    def __init__(self):
        self.value = 2 
        self.notation = 'N'

    def movement(game, player, pos, capture=True):
        result = []
        for i in [-1, 1]:
            if pos[0]-i >= 0 and pos[0]-i <= 7 and pos[1]-(2*i) >= 0 and pos[1]-(2*i) <= 7 and (game.board[pos[1]-(2*i)][pos[0]-i]*player < 0 or game.board[pos[1]-(2*i)][pos[0]-i] == 0):
                result.append((pos[0]-i, pos[1]-(2*i)))
            if pos[0]+i >= 0 and pos[0]+i <= 7 and pos[1]-(2*i) >= 0 and pos[1]-(2*i) <= 7 and (game.board[pos[1]-(2*i)][pos[0]+i]*player < 0 or game.board[pos[1]-(2*i)][pos[0]+i] == 0):
                result.append((pos[0]+i, pos[1]-(2*i)))
            if pos[0]-(2*i) >= 0 and pos[0]-(2*i) <= 7 and pos[1]-i >= 0 and pos[1]-i <= 7 and (game.board[pos[1]-i][pos[0]-(2*i)]*player < 0 or game.board[pos[1]-i][pos[0]-(2*i)] == 0):
                result.append((pos[0]-(2*i), pos[1]-i))
            if pos[0]-(2*i) >= 0 and pos[0]-(2*i) <= 7 and pos[1]+i >= 0 and pos[1]+i <= 7 and (game.board[pos[1]+i][pos[0]-(2*i)]*player < 0 or game.board[pos[1]+i][pos[0]-(2*i)] == 0):
                result.append((pos[0]-(2*i), pos[1]+i))
        return result

class Pawn:
    def __init__(self):
        self.value = 1 
        self.notation = ''

    def movement(game, player, pos, capture=True):
        result = []
        init = 1 if player < 0 else 6
        amt = 1 if pos[1] != init else 2
        for i in range(amt):
            if pos[1]-((i+1)*player) >= 0 and pos[1]-((i+1)*player) <= 7 and game.board[pos[1]-((i+1)*player)][pos[0]] == 0:
                result.append((pos[0], pos[1]-((i+1)*player)))
            else:
                break
        if pos[1]-player <= 7 and pos[1]-player >= 0 and pos[0]+1 <= 7 and pos[0]+1 >= 0 and game.board[pos[1]-player][pos[0]+1]*player < 0:
            result.append((pos[0]+1, pos[1]-player))
        if pos[1]-player >= 0 and pos[1]-player <= 7 and pos[0]-1 >= 0 and pos[0]-1 <= 7 and game.board[pos[1]-player][pos[0]-1]*player < 0:
            result.append((pos[0]-1, pos[1]-player))
        if pos[1]-player <= 7 and pos[1]-player >= 0 and pos[0]+1 <= 7 and pos[0]+1 >= 0 and (pos[0]+1, pos[1]-player) == game.en_passant:
            result.append((pos[0]+1, pos[1]-player))
        if pos[1]-player >= 0 and pos[1]-player <= 7 and pos[0]-1 >= 0 and pos[0]-1 <= 7 and (pos[0]-1, pos[1]-player) == game.en_passant:
            result.append((pos[0]-1, pos[1]-player))
        return result