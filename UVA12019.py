n = int(input())
for i in range(n):
    md = list(map(int, input().split()))
    mouth = md[0]
    date = md[1]
    date += 7
    if mouth == 1:
        day = (date - 10) % 7
    elif mouth == 2:
        day = abs(date - 21) % 7
    elif mouth == 3:
        day = abs(date - 7) % 7
    elif mouth == 4:
        day = abs(date - 4) % 7
    elif mouth == 5:
        day = abs(date - 9) % 7
    elif mouth == 6:
        day = abs(date - 6) % 7
    elif mouth == 7:
        day = abs(date - 11) % 7
    elif mouth == 8:
        day = abs(date - 8) % 7
    elif mouth == 9:
        day = abs(date - 5) % 7
    elif mouth == 10:
        day = abs(date - 10) % 7
    elif mouth == 11:
        day = abs(date - 7) % 7
    else:
        day = abs(date - 12) % 7
    
    if day == 0:
        print("Monday")
    elif day == 1:
        print("Tuesday")
    elif day == 2:
        print("Wednesday")
    elif day == 3:
        print("Thursday")
    elif day == 4:
        print("Friday")
    elif day == 5:
        print("Saturday")
    else:
        print("Sunday")