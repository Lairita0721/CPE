n = int(input())
count = {}
for i in range(n):
    text = input()
    for ch in text:
        if ch.isalpha():
            ch = ch.upper()
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
for c in sorted(count, key = lambda x:(-count[x], x)):
    print(c, count[c])
