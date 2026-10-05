#cpe10591
t = int(input())
for t in range(t):
    try:
        num = int(input())
        n = num
        happy = False
        sum = 0
        memory = []
        while n != 1:  
            while n > 0:
                sum += (n % 10) ** 2
                n //= 10
            if sum != 1:
                if sum in memory:
                    happy = False
                    break
                memory.append(sum)
                n = sum
                sum = 0
            else:
                happy = True
                break
        else:
            break
        if happy:
            print(f"Case #{t + 1}: {num} is a Happy number.")
        else:
            print(f"Case #{t + 1}: {num} is an Unhappy number.")
    except EOFError:
        break