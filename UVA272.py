c = 0
while(True):
    try:
        text = input()
        if len(text) == 0:
            break
        for ch in text:
            if ch == '"':
                if c % 2 == 0:
                    ch = ch.replace('"', '``')
                    c += 1
                else:
                    ch = ch.replace('"', "''")
                    c += 1
            print(ch, end = "")
        print(end = "\n")
    except EOFError:
        break