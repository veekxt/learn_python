import random

cards = [(x, y) for x in range(1, 5) for y in range(1, 14)]
to_del = random.randrange(0, 52)
print('to del is ', cards[to_del])
del cards[to_del]
random.shuffle(cards)


def find_del(cards):
    number = 1378 - sum([(one[0] - 1) * 13 + one[1] for one in cards])
    return (number // 13 + 1, number % 13)


print('find del is ', find_del(cards))
