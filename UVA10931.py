while (True):
    try:
        n = int(input())
        if n == 0:
            break
        s = bin(n).count("1")
        b = bin(n)
        print(f"The parity of {b[2:]} is {s} (mod 2).")
    except EOFError:
        break