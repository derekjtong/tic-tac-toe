#
# Alpha-beta pruning for the TTT game
#
# State[i][j] = i,j element of board ="X", "O" or " "
# Assumes O is the agent and X the opponent
#

import helpers as hp


# alpha beta MAX step
def abp_maxval(s, decision_count, alpha, beta):
    isTerminal, util = hp.terminal(s)
    if isTerminal:
        return util, decision_count
    v = -float("inf")
    for g in hp.expand(s, "O"):
        decision_count += 1
        mv, decision_count = abp_minval(g, decision_count, alpha, beta)
        v = max(v, mv)
        if v >= beta:
            return v, decision_count  # Beta cut-off
        alpha = max(alpha, v)
    return v, decision_count


# alpha beta MIN step
def abp_minval(s, decision_count, alpha, beta):
    isTerminal, util = hp.terminal(s)
    if isTerminal:
        return util, decision_count
    v = float("inf")
    for g in hp.expand(s, "X"):
        decision_count += 1
        mv, decision_count = abp_maxval(g, decision_count, alpha, beta)
        v = min(v, mv)
        if v <= alpha:
            return v, decision_count  # Alpha cut-off
        beta = min(beta, v)
    return v, decision_count


# alpha beta pruning procedure
# should not already be a winning board
def abp_search(s):
    decision_count = 0
    alpha = -float("inf")
    beta = float("inf")
    v = -float("inf")
    move = s
    for g in hp.expand(s, "O"):
        mv, decision_count = abp_minval(g, decision_count, alpha, beta)
        if mv > v:
            v = mv
            move = g
        alpha = max(alpha, v)  # Update alpha to the best found option for max
    action = hp.extractmove(s, move)
    return action, decision_count
