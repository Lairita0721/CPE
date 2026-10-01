#1022
row0 = "1234567890-="
row1 = "qwertyuiop[]\\"
row2 = "asdfghjkl;'"
row3 = "zxcvbnm,./"
mapping = {}
for row in [row0, row1, row2, row3]:
    for i in range(2, len(row)):
        mapping[row[i]] = row[i - 2]

text = input().lower()
for c in text:
    if c in mapping:
        print(mapping[c], end = "")
    else:
        print(c, end = "")
print(end = "\n")