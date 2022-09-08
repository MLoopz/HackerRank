def matchingStrings(strings, queries):
    lst = []
    for query in queries:
        occurs = 0
        for string in strings:
            if query == string:
                occurs+=1
        lst.append(occurs)
    return lst
            
print(matchingStrings(["ab","abc","a"], ["ab","abc", "a"]))