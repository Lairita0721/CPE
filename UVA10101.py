import sys

def convert_bangla(n):
    # 如果是 0，直接回傳空清單（由主程式在最外層防守）
    if n == 0:
        return []
    
    result = []
    
    # 處理 kuti (千萬)
    if n >= 10000000:
        # 遞迴處理超過千萬的部分，並在後面加上 kuti
        result.extend(convert_bangla(n // 10000000))
        result.append("kuti")
        n %= 10000000
        
    # 處理 lakh (十萬)
    if n >= 100000:
        result.append(f"{n // 100000}")
        result.append("lakh")
        n %= 100000
        
    # 處理 hajar (千)
    if n >= 1000:
        result.append(f"{n // 1000}")
        result.append("hajar")
        n %= 1000
        
    # 處理 shata (百)
    if n >= 100:
        result.append(f"{n // 100}")
        result.append("shata")
        n %= 100
        
    # 處理剩下的個位/十位數 (必須大於 0 才印，避免結尾多出 0)
    if n > 0:
        result.append(f"{n}")
        
    return result

def main():
    index = 1
    # 使用 sys.stdin.read 可以一次讀完所有測資，比 input() 更安全、不容易爆掉
    lines = sys.stdin.read().splitlines()
    
    for line in lines:
        if not line.strip(): # 避免讀到空行
            continue
            
        num = int(line)
        
        # 特判：如果輸入本身就是 0
        if num == 0:
            print(f"{index:4}. 0")
        else:
            words = convert_bangla(num)
            # 用單個空格把所有單字接起來
            print(f"{index:4}. {' '.join(words)}")
            
        index += 1

if __name__ == "__main__":
    main()