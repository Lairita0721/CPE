n = int(input())
fib = [1, 2]
while(fib[-1] <= 100000000):
    fib.append(fib[-1] + fib[-2])
lenn = len(fib) - 1
for i in range(n):
    origion = int(input())
    num = origion
    answer = ""
    for i in range(lenn, -1, -1):
        if fib[i] <= num:
            answer += "1"
            num -= fib[i]
            index = i
            break
    for i in range(index - 1, -1, -1):
        if fib[i] <= num:
            answer += "1"
            num -= fib[i]
        else:
            answer += "0"
    print(f"{origion} = {answer} (fib)")
