# Make a function called word_count
# It should be accept a single argument which will be a string
# the function needs to return a dictionary
# the keys in the dic will be each of the words in the string, lower.
# the values will be how many times that particular word appears in the string

def word_count(single_arg):
    d = {}
    for char in single_arg.lower().split():
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    print(d)


    #for i in kwargs:
    #    arg1.append(i)
    #for key in kwargs.values():
        #print(sing_arg.keys())

word_count(str("Hi Hi iam thiago").lower())
