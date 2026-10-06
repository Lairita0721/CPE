t = int(input())
input()

for _ in range(t):

    species = {}
    c = 0

    while True:
        try:
            tree = input()
        except EOFError:
            break

        if tree == "":
            break

        c += 1

        if tree not in species:
            species[tree] = 1
        else:
            species[tree] += 1

    if _ != 0:
        print()

    for s in sorted(species):
        p = species[s] / c * 100
        print(f"{s} {p:.4f}")