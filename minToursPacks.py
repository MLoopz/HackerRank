def getMinTours(N, A, k):
 
    # Iterating through each possible
    # value of minimum Items
    for i in range(1, max(A)+1):
        tours = 0
        for j in range(0, len(A)):
            if(A[j]% i == 0):# Perfectly Divisible
                tours += A[j]/i
 
            else:
                # Not Perfectly Divisible means required
                # tours are Floor Division + 1
                tours += A[j]//i + 1
 
        if(tours <= k):
            # Return First Feasible Value found,
            # since it is also the minimum
            return i #minimum number of items needed to be delivered per tour
    return "Not Possible"
 
# Driver Code
N = 10 #numbuckets
A = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] #buckets
k = 50 #maxtours
print(getMinTours(N, A, k))