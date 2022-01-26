import time
import os
from random import randint

starttime = time.time()

i = ''

a = []

a3 = []

a5 = []

a7 = []


def blink():
    i = randint(0, 1)

    if i == 1:

        a.append('*')

    else:

        a.append(' ')


def blink3():
    i = randint(0, 1)

    if i == 1:

        a3.append('*')

    else:

        a3.append(' ')


def blink5():
    i = randint(0, 1)

    if i == 1:

        a5.append('*')

    else:

        a5.append(' ')


def blink7():
    i = randint(0, 1)

    if i == 1:

        a7.append('*')

    else:

        a7.append(' ')


def tree():
    blink()

    blink3();blink3();blink3()

    blink5();blink5();blink5();blink5();blink5()

    blink7();blink7();blink7();blink7();blink7();blink7();blink7()

    print('      |', a[0], "|", '\n')

    print('    |', a3[0], a3[1], a3[2], '|', '\n')

    print('  |', a5[0], a5[1], a5[2], a5[3], a5[4], '|', '\n')

    print('|', a7[0], a7[1], a7[2], a7[3], a7[4], a7[5], a7[6], '|', '\n')

    print('        ||       ')

    print('       ----  ')

    a.clear()

    a3.clear()

    a5.clear()

    a7.clear()


while True:
    tree()
    time.sleep(0.4)
    os.system('clear') or None