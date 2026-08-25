t = int(input())
finger = {
    'c':[2,3,4,7,8,9,10],
    'd':[2,3,4,7,8,9],
    'e':[2,3,4,7,8],
    'f':[2,3,4,7],
    'g':[2,3,4],
    'a':[2,3],
    'b':[2],
    'C':[3],
    'D':[1,2,3,4,7,8,9],
    'E':[1,2,3,4,7,8],
    'F':[1,2,3,4,7],
    'G':[1,2,3,4],
    'A':[1,2,3],
    'B':[1,2]
}
for _ in range(t):
    song = input()
    c = [0] * 10
    last = []
    for note in song:
        if note == " ":
            continue
        now = finger[note]
        for f in now:
            if f not in last:
                c[f - 1] += 1
        last = now
    print(*c, end = "\n")