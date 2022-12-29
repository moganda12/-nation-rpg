"""
    a game
"""

import pygame

pygame.init()

cultures = ['chinese', 'egyptian', 'test']
personalitymad = ['pretty pleas type a choice', 'type one or il stop the program', 
'now I really will', 'error', '[computer fizzles]', 'I exploded']
claims = None
mad = 0
win = False
init = True
turn = 0
prv = [  'velia','terepto','hicroyo','hamming','lester','lancaster','worchester', 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23, 24, 25, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 50, 40, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63
]
prvind = {
    prv[0]: 10,
    prv[1]: 11,
    prv[2]: 15,
    prv[3]: 12,
    prv[4]: 11,
    prv[5]: 15,
    prv[6]: 134,
    prv[7]: 124,
    prv[8]: 129,
    prv[9]: 14,
    prv[10]: 27,
    prv[11]: 56,
    prv[12]: 97,
    prv[13]: 123,
    prv[14]: 1298,
    prv[15]: 15,
    prv[16]: 16,
    prv[17]: 17,
    prv[18]: 18,
    prv[19]: 19
}

def printcurr():
    print('You have ' + str('currs') + ' ' + 'curr' + 's')