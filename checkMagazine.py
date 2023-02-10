def checkMagazine(magazine, note):
    # Write your code here
    dict_magazine = {}
    for word in magazine:
        if word in dict_magazine:
            dict_magazine[word] += 1
        else:
            dict_magazine[word] = 1
    
    for word in note:
        if word in dict_magazine and dict_magazine[word] == 0:
            print("No")
            return
        else:
            dict_magazine[word] -=1
    print("Yes")

print(checkMagazine(["two","times","three","is","not","four"],["two","times","two","is","four"]))