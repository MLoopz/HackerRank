def minimumBribes(q):
    # Write your code here
    q_sorted = sorted(q)
    num_jumps = {}
    while q != q_sorted:
        for i in range(1, len(q)):
            if q[i-1] >  q[i]:
                t = q[i]
                q[i] = q[i-1]
                q[i-1] = t
                if q[i] not in num_jumps:
                    num_jumps[q[i]] = 1
                else:
                    num_jumps[q[i]] += 1
    if max(num_jumps.values()) > 2:
        print("Too chaotic")
    else:
        print(sum(num_jumps.values()))

minimumBribes([2,1,5,3,4])
'''

2 1 5 3 4
3
'''