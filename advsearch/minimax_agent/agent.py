import random

from advsearch import timer

# alpha é a melhor alternativa para o MAX nesse determinado nó
# beta é a melhor alternativa para o MIN nesse determinado nó

def max_value(possible_moves,board, color, depth, alpha, beta):
    max_score = -999999999
    for [x, y] in possible_moves:
        _board = simulate_turn(board, color, x, y)
        min_score = mini_max(_board, color, depth + 1, alpha, beta)
        max_score = max(max_score, min_score)
        alpha = max(alpha, max_score)
        if beta <= alpha:
            break
    return max_score

def min_value(possible_moves,board, color, depth, alpha, beta):
    min_score = 999999999
    for [x, y] in possible_moves:
        _board = simulate_turn(board, color, x, y)
        max_score = mini_max(_board, color, depth + 1, alpha, beta)
        min_score = min(min_score, max_score)
        beta = min(beta, min_score)
        if beta <= alpha:
            break
    return min_score



def mini_max(board, color, depth, alpha, beta):

    possible_moves = board.legal_moves(color)
    if depth == 4 or len(possible_moves)==0 :
        return board.piece_count['B']

    # OS PARES SÃO PRO MAX
    if depth % 2 == 0:
        return max_value(possible_moves,board, color, depth, alpha, beta)
    else:
        return min_value(possible_moves,board, color, depth, alpha, beta)

def simulate_turn(board, color, x, y):
    from advsearch.othello.board import from_string
    _board = from_string(board.__str__())
    _board.process_move((x, y), color)
    return _board


def handle_current_move(legal_moves, board, color):
    best_move_value = 0
    best_move_idx = 0
    for idx, (x, y) in enumerate(legal_moves):
        _board = simulate_turn(board, color, x, y)
        _alpha = mini_max(_board, color, 0, -9999999999999, 99999999999)
        if _alpha and _alpha > best_move_value:
            best_move_idx = idx
    return best_move_idx



def make_move(the_board, color):

    legal_moves = the_board.legal_moves(color)
    function_call = timer.FunctionTimer(handle_current_move, [legal_moves, the_board, color])
    idx = function_call.run(5)
    if not idx:
        return random.choice(legal_moves)
    print('FOUND SOLUTION')

    return legal_moves[idx]
