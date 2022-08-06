def flipcoins(s):
    num_t = 0
    flips = 0
    for c in s:
        if c == 'T':
            num_t += 1
        else:
            flips = min(flips+1, num_t)     
    return flips

print(flipcoins("HTTHTTHTHH"))