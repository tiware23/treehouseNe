def disemvowel(word):
    vow = "aeiou"
    my_list = list(word)
    for i in word:
        if i in vow:
            my_list.remove(i)
    word = ''.join(my_list)
    print(word)
        #if i in vo:
            #vo.remove(i)
    #        print(vo)
#        else:
#            print("There is not vowel \n")
#            break


disemvowel(input("Tell me the word! ").lower())
