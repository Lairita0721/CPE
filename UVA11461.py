square = []
for i in range(1, 317):
    square.append(i * i)
while(True):
    try:
        num = list(map(int, input().split()))
        a = num[0]
        b = num[1]
        if a == 0 and b == 0:
            break
        for i in range(316):
            if square[i] >= a:
                start = i 
                break
        for i in range(start, 317):
            if square[i] > b:
                end = i - 1
                break
        count = end - start
        print(square[start], square[end], count, end = "\n")
    except EOFError:
        break