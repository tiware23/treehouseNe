def squared(b):
    try:
        value = int(b)
        print(value ** 2)
    except ValueError:
        value1 = str(b)
        print(value1 * len(value1))

squared(2)
