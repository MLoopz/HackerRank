def generate_hashtag(s):
    #p = [q.index(v) if v in q else 99999 for v in vm]
    return '#'+''.join([word.capitalize() for word in s.split(' ')]) if s != '' else False

print(generate_hashtag(""))