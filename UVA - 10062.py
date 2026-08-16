first = True
while (True):
    try:
        s = input()
        s = s.rstrip('\r')
        
        if not first:
            print()
        first = False
        d = {}
        for ch in s:
            ch = ord(ch)
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        for c in sorted(d, key = lambda x:(d[x], -x)):
            print(c, d[c])

    except EOFError:
        break