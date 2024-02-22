import minimax as mx
import alphabetapruning as abp


def search(state):
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == " ":
                return (i, j), True
    return (0, 0), False  # no move


def mmsearch(state):
    act, decision_count = mx.minimax(state)
    print("Minimax chooses ", act)
    if act != None:
        return act, True, decision_count
    return (0, 0), False, decision_count  # no move


def alpha_beta_search(state):
    act, decision_count = abp.abp_search(state)
    print("Alpha-Beta chooses ", act)
    if act != None:
        return act, True, decision_count
    return (0, 0), False, decision_count  # no move
