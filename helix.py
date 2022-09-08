def helix(seq, point):
    p1 = seq[:point]
    p2 = seq[point:]
    return p1+p2
            
print(helix([3, 2, 1, 4, 5], 4))