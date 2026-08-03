t = int(input())
for _ in range(t):
    day = int(input())
    p = int(input())
    pi = [0] * p
    for i in range (p):
        pi[i] = int(input())
    hartal = [False] * (day + 1)
    for i in range(p):
        a = pi[i]
        while a <= day:
            if a % 7 != 6 and a % 7 != 0:
                if hartal[a] == False:
                    hartal[a] = True
            a += pi[i]
    print(hartal.count(True), end = "\n")