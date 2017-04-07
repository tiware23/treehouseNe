def num_teachers(string):
    count = int(0)
    for i in string.keys():
        count += 1
    print(count)


def num_courses(courses):
    count = int(0)
    for i in courses.values():
        for e in i:
            count +=1
    print(count)

def courses(single_list):
    course = []
    for i in single_list.values():
        for e in i:
            course.append(e)
    print(course)

def most_courses(most):
    max_count = 0
    for teacher, courses in most.items():
        if len(courses) > max_count:
            max_count = len(courses)
            max_teacher = teacher
    print(max_teacher)

def stats(lists):
    list_final = []
    list_final1 = []
    for keys in lists:
        qtd = len(lists[keys])
        list_final.append(keys)
        list_final.append(qtd)
        list_final1.append(list_final)
        list_final = []
    print(list_final1)





stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})
