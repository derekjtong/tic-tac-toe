#
# Minimax search for the TTT game
# c dml 2019
#
#
# State[i][j] = i,j element of board ="X", "O" or " "
# Assumes O is the agent and X the opponent
#

import helpers as hp


# minimax MAX step
def maxval(s, decision_count):
    """do max step on s and return value along with updated decision_count"""
    isTerminal, util = hp.terminal(s)
    if isTerminal:
        return util, decision_count
    v = -100  # -ve infinity
    for g in hp.expand(s, "O"):
        decision_count += 1
        mv, decision_count = minval(g, decision_count)
        if mv > v:
            v = mv
    return v, decision_count


# minimmax MIN step
def minval(s, decision_count):
    """do min step on s and return value along with updated decision_count"""
    isTerminal, util = hp.terminal(s)
    if isTerminal:
        return util, decision_count
    v = 100  # +ve infinity
    for g in hp.expand(s, "X"):
        decision_count += 1
        mv, decision_count = maxval(g, decision_count)
        if mv < v:
            v = mv
    return v, decision_count


# minimax decision procedure
# should not already be a winning board
def minimax(s):
    """will return the best move for 'O' in current state"""
    decision_count = 0
    v = -100  # -ve infinity
    move = s
    for g in hp.expand(s, "O"):
        mv, decision_count = minval(g, decision_count)
        if mv > v:
            v = mv
            move = g
    action = hp.extractmove(s, move)
    return action, decision_count
