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
y = []
for u in range(10000, 10050):
    if is_prime(u):
        y.append(u)
print(y)
