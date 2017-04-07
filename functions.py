def hows_the_parrot():
	print("Hes pining for flords!")

hows_the_parrot()

def lumberjack(name, pronoum):
		print("{} a lumber and {} OK".format(name, pronoum))

lumberjack("Elaine", "She's")
lumberjack("Thiago", "He's")
lumberjack("Kevin", "they")
lumberjack("El", "they're")

def even(num):
	if num % 2 == 0:
		return True
	else:
		return False

e = even(3)
print(e)

def printer(count):
	print("Hi " * count)

printer(10)
