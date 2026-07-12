while(True):
    try:
        a = list(input())
        b = list(input())
        sub = []
        for ch in a:
            if ch.isalpha():
                for c in b:
                    if c.isalpha():
                        if c == ch:
                            sub.append(c)
                            a.remove(ch)
                            b.remove(ch)
                            break
        sub.sort()
        for s in sub:
            print(s, end = "")
        print(end = "\n")
    except EOFError:
        break