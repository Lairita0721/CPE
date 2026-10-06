n = int(input())
num = list(map(int, input().split()))

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

num.sort(key=lambda x: (digit_sum(x), x))

print(*num)

