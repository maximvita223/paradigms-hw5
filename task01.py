import math

def is_prime(i):
    m = min(i, int(math.sqrt(b)))
    l = range(2, m)
    r = map(lambda x: i % x == 0, l)
    return not any(r)
 
a = int(input("Введите начало диапазона = "))
b = int(input("Введите конец диапазона = "))
ls = range(a, b)
_list = list(filter(is_prime, ls))

print(*[ f'{i+1}: {v}' for i, v in enumerate(_list)], sep='\n')