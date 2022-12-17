# 2. Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input('Enter a whole number: '))

is_negative = False
if n < 0:
    is_negative = True
    n = abs(n)

s = int(((n + 1) / 2) * n)

if is_negative:
    s = -s + 1

print(f'The sum is {s}')
