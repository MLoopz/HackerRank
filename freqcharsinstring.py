def getMaxFreqDeviation(s):
    # Write your code here
    listOfFreq = []
    listOfSubstrings = substrInString(s)
    for substr in listOfSubstrings:
        listOfFreq.append(getDifFreq(substr))
    return max(listOfFreq)
        
def getDifFreq(substr):
    dictio = getOccuringCharDict(substr)
    cmax = max(dictio, key=dictio.get)
    lmax= dictio[cmax]
    cmin = min(dictio, key=dictio.get)
    lmin= dictio[cmin]
    return lmax - lmin
def getOccuringCharDict(s):
    freq_dict = {}
    for c in s:
        if c in freq_dict:
            freq_dict[c]+=1
        else:
            freq_dict[c] = 1
    return freq_dict

def substrInString(s):
    listOfSubstr = []
    for i in range (len(s)):
        for j in range(i+1, len(s)+1):
            listOfSubstr.append(s[i:j])
    return listOfSubstr

print(getMaxFreqDeviation("bbacccabab"))