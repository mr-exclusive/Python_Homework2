# 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.

# 0 - heads
# 1 - tails

coins = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0]

heads_count = 0

for coin in coins:
    if coin == 0:
        heads_count += 1

print('Minimum number of coins to turn is', heads_count if heads_count < len(coins) / 2 else len(coins) - heads_count)
