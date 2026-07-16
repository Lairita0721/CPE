text = []

while True:
    try:
        text.append(input())
    except EOFError:
        break

max_len = max(len(s) for s in text)

for col in range(max_len):
    result = ""

    for row in range(len(text)-1, -1, -1):
        if col < len(text[row]):
            result += text[row][col]
        else:
            result += " "

    print(result)