def pileofBoxes(lst_piles):
    for max_removal in range(1,10):
        for pile in lst_piles:
            if pile[0] - max_removal < 0 :
                return max_removal -1   
    return max_removal

print(pileofBoxes([[10],[3],[5]]))


def pileofBoxes(lst_piles):
    for max_removal in range(1,10):
        for pile in lst_piles:
            if pile[0] - max_removal < 0 :
                return max_removal -1   
    return max_removal

print(pileofBoxes([[128],[123],[51]]))