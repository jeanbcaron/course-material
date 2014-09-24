def draw_n_squares(m):
    n = 2*m
    for i in range(n):
            if i % 2 == 0:
                print('+---'*m + '+')
            else:
                print('|   '*m + '|')
    print('+---'*m + '+')
