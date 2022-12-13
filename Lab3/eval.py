import os

import chess
import chess.engine

def getEval(board):
    engine = chess.engine.SimpleEngine.popen_uci(r'/Users/d.pits/Documents/Education/PIIS/Lab3/stockfish-8-mac/Mac/stockfish-8-64')
    score = engine.analyse(board, chess.engine.Limit(time=0.01))['score'].black().score()
    engine.quit()

    return score
