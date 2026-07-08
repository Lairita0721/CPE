n = int(input())
count = {}
for i in range(n):
    l = input().split()
    country = l[0].capitalize()
    if country not in count:
        count[country] = 1
    else:
        count[country] += 1
for country in sorted(count, key=str.lower):        
    print(f"{country} {count[country]}")