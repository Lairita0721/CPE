grid = list(map(int, input().split()))
m = grid[0]
n = grid[1]
d = ['E', 'S', 'W', 'N']
lose = []  # 存放氣味座標，格式為 [(x1, y1), (x2, y2)]

while True:
    try:
        p = list(input().split())
        x = int(p[0])
        y = int(p[1])
        direction = p[2]
        lo = False
        instructions = input().strip()  # 直接取得指令字串

        for i in instructions:
            if i == "L":
                index = d.index(direction)
                direction = d[(index - 1) % 4]
            elif i == 'R':
                index = d.index(direction)
                direction = d[(index + 1) % 4]
            elif i == 'F':
                # 先計算移動後的目標座標
                nx, ny = x, y
                if direction == "E":
                    nx += 1
                elif direction == "W":
                    nx -= 1
                elif direction == "N":
                    ny += 1
                elif direction == "S":
                    ny -= 1

                # 檢查目標座標是否超出地圖邊界
                if nx < 0 or nx > m or ny < 0 or ny > n:
                    # 如果當前位置有氣味，忽略這次走出邊界的指令
                    if (x, y) in lose:
                        continue
                    else:
                        # 掉出邊界，記錄氣味並標記 LOST
                        print(f"{x} {y} {direction} LOST")
                        lose.append((x, y))
                        lo = True
                        break  # 掉落後終止執行剩餘指令
                else:
                    x, y = nx, ny

        if not lo:
            print(x, y, direction)

    except EOFError:
        break