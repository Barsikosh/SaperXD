import random


def Creating_Map(lvl):
    width = 0
    height = 0
    bombs_count = 0
    bombs_max = 0
    if lvl == 0:
        width = 9
        height = 9
        bombs_count = 10
        bombs_max = 4
    elif lvl == 1:
        width = 16
        height = 16
        bombs_count = 40
        bombs_max = 5
    elif lvl == 2:
        width = 30
        height = 30
        bombs_count = 99
        bombs_max = 6

    pool = [[0 for x in range(width)] for y in range(height)]
    for i in range(0, bombs_count):

        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        while not is_Correct(x, y, bombs_max, pool):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

        pool[x][y] = "b"
        counting_Numbers(x, y, pool)

    return pool


def is_Correct(x, y, bombs_max, pool=[[]]):
    height = len(pool)
    width = len(pool[0])
    if pool[x][y] == 'b':
        return False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= x + dx < width and 0 <= y + dy < height:
                if Check(x + dx, y + dy, bombs_max, pool):
                    return False
    return True


def Check(x, y, bombs_max, pool=[[]]):
    height = len(pool)
    width = len(pool[0])
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= x + dx < width and 0 <= y + dy < height:
                if pool[x + dx][y + dy] == 'b':
                    count += 1
    if (count > bombs_max):
        return True
    return False


def counting_Numbers(x, y, pool=[[]]):
    height = len(pool)
    width = len(pool[0])
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= x + dx < width and 0 <= y + dy < height:
                if pool[x + dx][y + dy] != 'b':
                    pool[x + dx][y + dy] += 1