import random

def random_item(s):
    inter = int(random.randint(0, len(s)))
    subs = inter - 1
    return s[inter]
