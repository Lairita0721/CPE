import math
while (True):
    try:
        l = list(input().split())
        s = int(l[0]) + 6440
        a = int(l[1])
        d = str(l[2])
        if a > 360:
            a = a % 360
        if a > 180:
            a = 360 - a
        if d == 'min':
            a = a / 60.0
        arc = s * 2 *  math.pi * (a / 360)
        chord = (s * math.cos(math.radians(90 - a / 2))) * 2
        print(f"{arc:.6f} {chord:.6f}", end = "\n")

    except EOFError:
        break