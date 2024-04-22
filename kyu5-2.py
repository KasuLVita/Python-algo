'''
*creator LektorLuigi/KasulVita
------------
04.22.2024
Codewars Kyu 5
'''

n = int(input())
def product_fib(prod):
    fib_n = [0, 1]
    if prod == 0:
        return [0, 1, True]
    a = fib_n[0]
    b = fib_n[1]
    while True:
        c = a + b
        a = b
        b = c
        if a * b >= prod:
            if a * b == prod:
                return [a, b, True]
            else:
                return [a, b, False]

print(product_fib(n)) #e.g n = 714 -> True
