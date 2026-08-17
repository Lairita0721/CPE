# open(0).read() 會一次性讀取所有輸入，效率極高
data = open(0).read().split('\n')

if data:
    t = int(data[0])
    idx = 2  # 跳過 t (data[0]) 與其隨後的空行 (data[1])
    
    first = True

    for _ in range(t):
        specie = {}
        total = 0

        if not first:
            print()
        first = False

        # 讀取當前測試資料
        while idx < len(data):
            s = data[idx]
            idx += 1

            if s == "":  # 遇到空行代表該組測資結束
                break

            if s not in specie:
                specie[s] = 1
            else:
                specie[s] += 1

            total += 1

        # 輸出結果
        for p in sorted(specie):
            percentage = specie[p] / total * 100
            print(f"{p} {percentage:.4f}")