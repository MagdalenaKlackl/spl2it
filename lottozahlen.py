import random

def kugel():
    return random.randrange(1,46)

def ziehung():
    zahlen = set()
    while len(zahlen) < 7:
        zahlen.add(kugel())
    return list(zahlen)