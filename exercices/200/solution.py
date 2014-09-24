def is_prime(a):
    b = 0
    for i in range(int(pow(a, 0.5))):
        if a % (i+2) == 0:
            if a != (i+2):
                b = 1
    if b == 1:
        return False
    if b != 1:
        return True
