import random

from advsearch import timer


def minmax(board, color, depth, alpha, beta):
    # LIMITE DA PROFUNDIDADE
    if depth == 50:
        return board.piece_count['B']
    else:
        # MAX
        if depth % 2 == 0:
            possible_moves = board.legal_moves(color)
            for [x, y] in possible_moves:
                _board = simulate_turn(board, color, x, y)
                _alpha = minmax(_board, color, depth + 1, alpha, beta)
                if _alpha > alpha:
                    alpha = alpha
            return alpha
        else:
            # MIN
            possible_moves = board.legal_moves(color)
            for [x, y] in possible_moves:
                _board = simulate_turn(board, 'W', x, y)
                _beta = minmax(_board, 'W', depth + 1, alpha, beta)
                if _beta < beta:
                    beta = _beta
            return beta


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
        print('FOUND SOLUTION')
        return random.choice(legal_moves)
    return legal_moves[idx]
