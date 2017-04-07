template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(lst):
    dic_lst =[]
    for i in lst:
        dic_lst.append(template.format(**i))
    print(dic_lst)
        #print(template.format(**lst2))

string_factory([{"name": "Thiago", "food": "barbecue"}, {"name": "John", "food": "pizza"}])


#def string_factory(dicts):
#    new_list =[]
#    for elem in dicts:
#        new_list.append(template.format(**elem))
#    return new_list
