def twoStacks(maxSum, a, b):
    # Write your code here
    moves = []
    score = {}
    options = {}
    for x in a:
        for y in b:
            score
            score[len(x)] = sum(x)
            if score[len(x)] > maxSum:
                options[len(x)] = score[len(x)]

    return min(options)

print(twoStacks(10, [1,2,3,4,5],[6,7,8,9]))