def sherlockAndAnagrams(s):
    dic = {}
    total = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            st = ''.join(sorted(s[i : j+1]))
            if st not in dic:
                dic[st] = 1
            else:
                total+=dic[st]
                dic[st] += 1

    return total
        
print(sherlockAndAnagrams("kkkk"))
