import random

start = 5

def even_odd(num):
    if num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))

while start > 0 :
    valor = int(random.randint(1, 99))
    even_odd(valor)
    start -= 1
