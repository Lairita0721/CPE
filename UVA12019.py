n = int(input())
for i in range(n):
    md = list(map(int, input().split()))
    mouth = md[0]
    date = md[1]
    date += 21
    if mouth == 1:
        day = (date - 10) % 7
    elif mouth == 2:
        day = (date - 21) % 7
    elif mouth == 3:
        day = (date - 7) % 7
    elif mouth == 4:
        day = (date - 4) % 7
    elif mouth == 5:
        day = (date - 9) % 7
    elif mouth == 6:
        day = (date - 6) % 7
    elif mouth == 7:
        day = (date - 11) % 7
    elif mouth == 8:
        day = (date - 8) % 7
    elif mouth == 9:
        day = (date - 5) % 7
    elif mouth == 10:
        day = (date - 10) % 7
    elif mouth == 11:
        day = (date - 7) % 7
    else:
        day = (date - 12) % 7
    
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