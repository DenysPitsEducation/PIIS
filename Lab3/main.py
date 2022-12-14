import chess
import chess.svg
from algorithms import *

INFINITY = 999999


def get_best_move(depth, board, func: Algorithm):
    moves = board.legal_moves
    best_move = None

    max_score = -INFINITY

    for move in moves:
        board.push(move)

        if func == Algorithm.NEGAMAX:
            score = negamax(depth - 1, board)
        elif func == Algorithm.NEGASCOUT:
            score = negascout(depth - 1, board, -INFINITY, INFINITY)
        else:
            score = pvs(depth - 1, board, -INFINITY, INFINITY)
        print(board)
        print('\na b c d e f g h')
        board.pop()
        if score >= max_score:
            print('Новий кращий хід: ' + str(move.uci()) + '\nБали: ' + str(score))
            max_score = score
            best_move = move
    return best_move


def main():
    board = chess.Board()
    func = Algorithm.PVS

    while 1:
        cpu_move = get_best_move(1, board, func)
        print('Хід: ' + board.san(cpu_move))
        board.push(cpu_move)
        print(board)
        print('\na b c d e f g h')
        board_svg = chess.svg.board(board)
        with open('board.svg', 'w') as file:
            file.write(board_svg)

        move = input("Походіть: ")
        if str(move) == 'score':
            print('Кількість балів: ' + str(get_score(board)))
            move = input("Походіть: ")
        board.push_san(str(move))


if __name__ == "__main__":
    main()
