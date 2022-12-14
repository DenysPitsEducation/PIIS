from enum import Enum

from score import get_score


def negamax(depth, board):
    if depth == 0:
        final_eval = get_score(board)
        if final_eval is None:
            return 0
        return -final_eval
    max_value = -99999
    legal_moves = board.legal_moves
    for move in legal_moves:
        board.push(move)
        score = -negamax(depth - 1, board)
        board.pop()
        if score > max_value:
            max_value = score
    return -max_value


def negascout(depth, board, alpha, beta):
    best_score = -99999
    b = beta
    if depth == 0:
        final_eval = get_score(board)
        if final_eval is None:
            return 0
        return -final_eval

    for move in board.legal_moves:
        board.push(move)
        score = -negascout(depth - 1, board, -b, -alpha)
        if score > best_score:
            if alpha < score < beta:
                best_score = max(score, best_score)
            else:
                best_score = -negascout(depth - 1, board, -beta, -score)

        board.pop()
        alpha = max(score, alpha)
        if alpha > beta:
            return alpha
        b = alpha + 1
    return best_score


def pvs(depth, board, alpha, beta):
    best_score = -99999
    b = beta
    if depth == 0:
        final_eval = get_score(board)
        if final_eval is None:
            return 0
        return -final_eval

    for move in board.legal_moves:
        board.push(move)
        score = -pvs(depth - 1, board, -b, -alpha)
        if score > best_score:
            if alpha < score < beta:
                best_score = max(score, best_score)
            else:
                best_score = -pvs(depth - 1, board, -beta, -score)

        board.pop()
        if alpha > beta:
            return alpha
        b = alpha + 1
    return best_score


class Algorithm(Enum):
    NEGAMAX = 1
    NEGASCOUT = 2
    PVS = 3
