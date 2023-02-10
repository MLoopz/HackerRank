def hourglassSum(arr):
    # Write your code here
    lst_hourglass = []
    size = len(arr)
    for x in range(1,size-1):
        for y in range(1,size-1):
            hourglass = (arr[x-1][y-1]+
                        arr[x-1][y]+
                        arr[x-1][y+1]+
                        arr[x][y]+
                        arr[x+1][y-1]+
                        arr[x+1][y]+
                        arr[x+1][y+1])
            lst_hourglass.append(hourglass)
    return max(lst_hourglass)
print(hourglassSum([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]))