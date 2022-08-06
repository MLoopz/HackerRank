def minimalHeaviestSetA(arr):
    arr = sorted(arr)
    half = sum(arr) // 2 #divide without decimals (trunking)
    i = len(arr) - 2  # -2 bc the position of the i is 1 more to the left ot the last position. Last position already in A. 
    sum_A = sum(arr[i:])

    while sum_A <= half: #while the sum of A is less or eq than the half of the total sum
        # Max of sum /  divide by the max numbers that can be to the left of arr[i]
        min_steps = max(1, (half - sum_A) // max(1, arr[i]))
        # sum from [arr[i-min_stemps] to arr[i]
        sum_A += sum(arr[i-min_steps:i])
        i -= min_steps
    return arr[i:]
print(minimalHeaviestSetA([5,3,2,4,1,2]))