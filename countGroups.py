def countGroups(related):
    #String to array of nums
    rows=[]
    for arr in related:
        rows.append([int(letter) for letter in arr])
    
    count = 0
    length = len(related)
    
    for i in range(length):
        if rows[i][i] == 1:
            #himself create a group
            count +=1
            findFriends(i, length, rows)
    return count

def findFriends(i, size,rows):
    #break recursion
    if rows[i][i] == 0:
        return 
    for j in range(size):
        if rows[i][j]==1:
            #if has a friend clear them to not repeat
            rows[i][j]=0
            findFriends(j,size,rows)

print(countGroups(["1100","1110","0110","0001"]))