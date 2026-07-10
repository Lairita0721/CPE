row = "1234567890-="
row1 = "qwertyuiop[]\\"
row2 = "asdfghjkl;'"
row3 = "zxcvbnm,./"
mapping = {}
for row in [row, row1, row2, row3]:
    for i in range(2, len(row)):
        mapping[row[i]] = row[i - 2]

text = input().lower()
for ch in text:
    if ch in mapping:
        print(mapping[ch], end = "")
    else:
        print(ch, end = "")
print(end = "\n")