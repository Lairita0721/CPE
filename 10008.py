#10008
n = int(input())
frequency = {}
for i in range(n):
    text = input()
    for ch in text:
        if ch.isalpha():
            ch = ch.upper()
            if ch not in frequency:
                frequency[ch] = 1
            else:
                frequency[ch] += 1
for c in sorted(frequency, key = lambda x:(-frequency[x], x)):
    print(c, frequency[c])