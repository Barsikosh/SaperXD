import random


def counting_Numbers(x, y, width, height, pool):
    if x - 1 >= 0 and y - 1 >= 0:
        if pool[x - 1][y - 1] != 'b':
            pool[x - 1][y - 1] += 1
    if y - 1 >= 0:
        if pool[x][y - 1] != 'b':
            pool[x][y - 1] += 1
    if x + 1 < width and y - 1 >= 0:
        if pool[x + 1][y - 1] != 'b':
            pool[x + 1][y - 1] += 1
    if x - 1 >= 0:
        if pool[x - 1][y] != 'b':
            pool[x - 1][y] += 1
    if x + 1 < width:
        if pool[x + 1][y] != 'b':
            pool[x + 1][y] += 1
    if x - 1 >= 0 and y + 1 < height:
        if pool[x - 1][y + 1] != 'b':
            pool[x - 1][y + 1] += 1
    if y + 1 < height:
        if pool[x][y + 1] != 'b':
            pool[x][y + 1] += 1
    if y + 1 < height and x + 1 < width:
        if pool[x + 1][y + 1] != 'b':
            pool[x + 1][y + 1] += 1


def is_Correct(x, y, width, height, max, pool):
    if pool is None:
        pool = [[]]
    if pool[x][y] == 'b':
        return False
    count = 1
    if x - 1 >= 0 and y - 1 >= 0:
        if pool[x - 1][y - 1] == 'b':
            count += 1
    if y - 1 >= 0:
        if pool[x][y - 1] == 'b':
            count += 1
    if x + 1 < width and y - 1 >= 0:
        if pool[x + 1][y - 1] == 'b':
            count += 1
    if x - 1 >= 0:
        if pool[x - 1][y] == 'b':
            count += 1
    if x + 1 < width:
        if pool[x + 1][y] == 'b':
            count += 1
    if x - 1 >= 0 and y + 1 < height:
        if pool[x - 1][y + 1] == 'b':
            count += 1
    if y + 1 < height:
        if pool[x][y + 1] == 'b':
            count += 1
    if y + 1 < height and x + 1 < width:
        if pool[x + 1][y + 1] == 'b':
            count += 1
    if count > max:
        return False
    return True


def Creating_Map(lvl, custom_width=None, custom_height=None):
    width = 0
    height = 0
    bombs_count = 0
    bombs_max = 0

    if custom_width is not None and custom_height is not None:
        width = custom_width
        height = custom_height
        bombs_count = round(0.6 * width * height)
        bombs_max = round(0.04 * width * height)

    else:
        if lvl == 0:
            width = 9
            height = 9
            bombs_count = 18
            bombs_max = 4
        elif lvl == 1:
            width = 16
            height = 16
            bombs_count = 56
            bombs_max = 5
        elif lvl == 2:
            width = 30
            height = 30
            bombs_count = 200
            bombs_max = 6

    pool = [[0 for x in range(width)] for y in range(height)]
    for i in range(0, bombs_count):

        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        while not is_Correct(x, y, width, height, bombs_max, pool):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

        pool[x][y] = "b"
        counting_Numbers(x, y, width, height, pool)

    return pool


