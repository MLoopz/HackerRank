def twoStrings(s1, s2):
    lst_sbstring = []
    substring = ""
    answer = "NO"
    for l in s1:
        if l in s2:
            answer = "YES"
            break
    return answer

print(twoStrings("and","art"))