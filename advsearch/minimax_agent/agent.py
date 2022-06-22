import random

from advsearch import timer

n=8
min_eval_board = -1 # min - 1
max_eval_board = n * n + 4 * n + 4 + 1 # max + 1
def minmax(board, color, depth, alpha, beta):
    # LIMITE DA PROFUNDIDADE
    possible_moves = board.legal_moves(color)

    if depth == 5 or len(possible_moves)==0 :
        return board.piece_count['B']
    else:
        # MAX
        if depth % 2 == 0:
            v=min_eval_board
            for [x, y] in possible_moves:
                _board = simulate_turn(board, color, x, y)
                v = max(v,minmax(_board, color, depth + 1, alpha, beta))
                alpha=max(alpha,v)
                if beta <= alpha:
                    break
            return v
        else:
            v=max_eval_board
            for [x, y] in possible_moves:
                _board = simulate_turn(board, color, x, y)
                v = min(v,minmax(_board, color, depth + 1, alpha, beta))

                beta=min(beta,v)
                if beta <= beta:
                    break
            return v


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
        _alpha = minmax(_board, color, 0, -9999999999999, 99999999999)
        if _alpha and _alpha > best_move_value:
            best_move_idx = idx
    return best_move_idx



def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    legal_moves = the_board.legal_moves(color)
    function_call = timer.FunctionTimer(handle_current_move, [legal_moves, the_board, color])
    idx = function_call.run(5)
    if not idx:
        return random.choice(legal_moves)
    return legal_moves[idx]
