import random
import numpy as np

# defines the reward/connection graph








def changeq(state, nxtq):
    action = findnext_action(state)
    qmat = nxtq
    print(":::::::::::::::")
    print(q)
    print(":::::::::::::::::::")
    # print(action)
    qmat[state][action] = r[state, action] + LR * max(qmat[action])
    print("xxxxxxxxxx")
    print(q)
    # print(qmat)
    # print("--------------------------------------------------------------------------")

    if action != desired_state:
        nxt = findnext_action(action)
        # print(nxt)
        changeq(nxt, qmat)

    return qmat


def qlearn():
    print(q)
    st = random.randint(0, 5)
    new_q = changeq(st, q)




qlearn()