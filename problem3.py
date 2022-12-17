# 3. Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input('Enter a whole number: '))

flag = True
i = 1
while flag:
    i += 1
    if n % i == 0:
        print(f'The smallest divisor for {n} is {i}.')
        flag = False
