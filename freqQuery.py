def freqQuery(queries):
    answers = []
    dic = {}
    for t, n in queries:
        if t == 1:
            #insert
            dic[n] = dic.get(n, 0) + 1
        elif t == 2:
            #delete
            if n in dic and dic[n] > 0:
                dic[n] = dic.get(n, 0) - 1
        elif t == 3:
            #check if k in dict n times
            lst = []
            if n in set(dic.values()):
                answers.append(1)
            else:
                answers.append(0)
        else:
            return
    return answers

print(freqQuery([(1,5),(1,6),(3,2),(1,1),(1,1),(1,6),(2,5),(3,2)]))