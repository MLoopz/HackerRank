
def repeatedString(s, n):
    # Write your code here
    count = n // len(s) * s.count('a')
    extra =  s[:n % len(s)].count('a')
    return count + extra

print(repeatedString("aba",10))