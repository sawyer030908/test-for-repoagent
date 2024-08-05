''' 数字炸弹 '''

import random


def boom(min:int, max: int) -> None:
    answer = random.randint(min, max)
    a = 0
    i = min
    j = max

    while a != answer:
        b = int(input(""))
        if b == answer:
            print("boom!")
            return(b)
            break
        elif b > answer:
            print(i,"~",b)
            j = b
        else:
            print(b,"~",j)
            i = b

if __name__ == "__main__":
    print(boom(1,1000))

