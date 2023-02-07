def countingValleys(steps, path):
    # Write your code here
    num_valleys = 0
    count_path = [0]
    count = 0
    min = 0

    for i in range(steps):
        if path[i] == 'D':
            count -= 1
        if path[i] == 'U':
            count += 1
        count_path.append(count)

        if count_path[i-1] == 0 and count_path[i] == -1:
            num_valleys+=1
    return num_valleys

print(countingValleys(12,"DDUUDDUDUUUD"))