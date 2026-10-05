#cpe11956
t = int(input())
for _ in range(t):
    command = input()
    p = 0
    value = [0] * len(command)
    for c in command:
        if c == ">":
            if p < len(command) - 1:
                p += 1
            else:
                p = 0
        elif c == "<":
            if p > 0:
                p -= 1
            else:
                p = len(command) - 1
        elif c == "+":
            if value[p] < 255:
                value[p] += 1
            else:
                value[p] = 0
        elif c == "-":
            if value[p] > 0:
                value[p] -= 1
            else:
                value[p] = 255
        else:
            pass
    print(f"Case {_ + 1}:" + " ".join(f"{v:02X}" for v in value))    
    print()