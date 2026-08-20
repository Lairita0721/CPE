while True:
    try:
        line = int(input())
        if line == 0:
            break
        die = {
            't':1,
            'n':2,
            'w':3,
            'e':4,
            's':5,
            'b':6
        }
        for _ in range(line):
            direction = input()
            if direction == 'north':
                ttmp = die['t']
                ntmp = die['n']
                stmp = die['s']
                btmp = die['b']
                die['t'] = stmp
                die['n'] = ttmp
                die['b'] = ntmp
                die['s'] = btmp
            elif direction == 'south':
                ttmp = die['t']
                ntmp = die['n']
                stmp = die['s']
                btmp = die['b']
                die['t'] = ntmp
                die['n'] = btmp
                die['b'] = stmp
                die['s'] = ttmp
            elif direction == 'east':
                ttmp = die['t']
                wtmp = die['w']
                etmp = die['e']
                btmp = die['b']
                die['t'] = wtmp
                die['w'] = btmp
                die['b'] = etmp
                die['e'] = ttmp
            else:
                ttmp = die['t']
                wtmp = die['w']
                etmp = die['e']
                btmp = die['b']
                die['t'] = etmp
                die['w'] = ttmp
                die['b'] = wtmp
                die['e'] = btmp


        print(die['t'], end = '\n')

    except EOFError:
        break