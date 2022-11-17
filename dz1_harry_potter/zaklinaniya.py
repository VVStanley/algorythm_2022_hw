"""Квадратные заклинания"""


def cast_a_spell() -> None:
    """Произнести заклинание"""
    result = ''

    for x in range(25):
        for y in range(25):
            spell = not x or not y
            result += '# ' if spell else '* '
        result += '\n'

    print(result)


if __name__ == '__main__':
    cast_a_spell()

    found_spells = {
        1: "x < y",
        2: "x == y",
        3: "x == 24 - y",
        4: "30 - x > y",
        5: "x == y // 2",
        6: "x in range(10) or y in range(10)",
        7: "x not in range(16) and y not in range(16)",
        8: "not x or not y",
        9: "x < y - 10 or x - 10 > y",
        11: "x in (1, 23) or y in (1, 23)",
        13: "19 - x < y and x < 29 - y",
        15: "x - 10 > y and x - 21 < y or x < y - 10 and x > y - 21",
        16: "x - 9 < y and x > y - 11 and 13 - x < y and x < 33 - y",
        19: "x in (0, 24) or y in (0, 24)",
        20: "any([i - x == y + 1 for i in range(1, 50, 2)])",
        22: "any([i - x == y + 1 for i in range(1, 50, 3)])",
        24: "x == y or x == 24 - y",
        25: "x % 6 == 0 or y % 6 == 0",
    }
