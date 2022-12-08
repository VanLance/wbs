def feedTheKids(students,sammys):
    sammy,studentDict=sammys[::-1],{}
    for kid in students:
        studentDict[kid]=studentDict.get(kid,0)+1
    while sammy:
        if studentDict[sammy[-1]]==0:
                break
        current=students.pop(0)
        if current == sammy[-1]:
            sammy.pop()
            studentDict[current]-=1
        else:
            students.append(current)
    return len(students)

# print(feedTheKids([1,1,0,0], [0,1,0,1]))
# print(feedTheKids([1,1,1,0,0,1],[1,0,0,0,1,1]))

