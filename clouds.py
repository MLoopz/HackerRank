def jumpingOnClouds(c):
    # Write your code here
    string = ""
    jumps = 0
    for i in range(len(c)):
        string+=str(c[i])
    
    chains = string.split("1")
    jumps = len(chains) -1 

    for chain in chains:
        n = len(chain)
        jumps += n//2 

def jumpingOnClouds2(c):
    # Write your code here
    max_moves = 2
    moves = 0
    answer = []
    for i in range(len(c)):
        moves+=1
        if i == 0:
            answer.append(i)  
        elif i > 0 and i < len(c)-1:
            if (c[i-1] != 0 or c[i+1] != 0) or (moves >= max_moves and c[i] == 0):
                answer.append(i) 
                moves = 0
        else:
            if c[i-1] != 0:
                answer.append(i)  
    return len(answer)-1 

#3
print(jumpingOnClouds([0,0,0,1,0,0]))
#46
#print(jumpingOnClouds([0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0]))