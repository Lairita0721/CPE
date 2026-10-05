#cpe1062
case = 1
while True:
    try:
        ship = input()
        if ship == "end":
            break
        c = 0
        min = []
        for s in ship:
            for i in range(len(min)-1, -1, -1):
                if ord(s) <= ord(min[i]):
                    min[i] = s
                    break
            else:
                c += 1
                min.append(s)
        print(f"Case {case}: {c}", end = "\n")
        case += 1
    except EOFError:
        break