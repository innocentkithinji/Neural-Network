import random
import numpy as np

r = [[-1, -1, -1, -1, 0, -1],
     [-1, -1, -1, -1, -1, 100],
     [-1, -1, -1, 0, -1, -1],
     [-1, 0, 0, -1, 0, -1],
     [0, -1, -1, 0, -1, 100],
     [-1, 0, -1, -1, 0, 100]]
q = ([0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0])
new_q = []

desired_state = 5
LR = 0.8



def chang(x, z):
    action = findnext_action(x)
    mat = z
    mat[x][action] = r[x][action] + (LR * max(mat[action]))

    # if action != desired_state:
    #     nxt = findnext_action(action)
    #     # print(nxt)
    #     chang(nxt, qmat)

    print(z)

    # return mat


def findnext_action(point):
    possibles = []
    for i in range(len(r[point])):
        if r[point][i] != -1:
            possibles.append(i)

    return random.choice(possibles)

if __name__ == '__main__':
    z = q
    print(z)
    print("--------------")
    print(q)
    print("--------------")
    chang(1,q)
    print("--------------")
    print(z)