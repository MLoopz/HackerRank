#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY parcels as parameter.
#

def getMinimumDays(parcels):
    # Write your code here
    days = 0
    length = len(parcels)
    while length > 0:
        nmax=max(parcels)
        nmin =min(parcels)
        dispatching = nmax - nmin
        for i in range(length):
            if parcels[i] >= dispatching:
                parcels[i] -= dispatching
            else:
                parcels.remove(parcels[i])
                length-=1
        days +=1
        
    return days
             
getMinimumDays([4,2,3,4])