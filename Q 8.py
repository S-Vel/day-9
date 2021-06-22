import math
def trigo(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosine(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)

trigo('sin',30)

trigo('tan',60)

trigo('cos',90)