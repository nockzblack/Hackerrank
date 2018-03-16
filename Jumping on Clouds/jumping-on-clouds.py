#!/usr/local/bin/python3

import sys

def jumpingOnClouds(c):
    # Complete this function
    n_jumps = jumping(0,0,c)
    return n_jumps


"""
    The algorithm works:
    on where is the player and
    if there is cloud available two jumps ahead
    if no just jump one
    and evaluate again!
"""
def jumping(pos, jumps, clouds):
    # get the last cloud the player can jump in 
    last = len(clouds)-1
    # if the player is on the last cloud return n jumps so far
    if pos == last:
        return jumps
    # if not, means  there are more coulds ahead
    else:
        # is there an ordinary cloud 2 jumps ahead?
        if pos + 2 <= last and clouds[pos+2] != 1:
            return jumping(pos+2, jumps+1, clouds)
        else:
            # 'cause there is always a way to win, will be an available cloud
            return jumping(pos+1, jumps+1, clouds)
        
    

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c)
    print(result)

