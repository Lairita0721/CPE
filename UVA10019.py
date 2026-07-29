n = int(input())
for i in range(n):
    num = input()
    x1 = int(num)
    x2 = int(num, 16)
    b1 = bin(x1).count("1")
    b2 = bin(x2).count("1")
    print(b1, b2, end = "\n")