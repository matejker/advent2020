"""
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island.
Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of
a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow,
you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579,
 so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply
them together?

Your puzzle answer was 1003971.

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from
a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same
criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together
produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 84035952.
"""

INPUT = [
    1993, 1715, 1997, 1666, 1676, 1830, 1203, 1800, 1125, 1191, 1902, 1972, 1471, 1137, 2003, 1250, 1548, 1070, 1152,
    2004, 1127, 1111, 1898, 1848, 1934, 1236, 1704, 1950, 1387, 1713, 1214, 1266, 1114, 1089, 1677, 1207, 1341, 1689,
    1772, 1901, 1932, 1645, 1285, 1884, 883, 1291, 1543, 1455, 1213, 1088, 1784, 1506, 1879, 1811, 1880, 994, 1021,
    1585, 1662, 1683, 1071, 1643, 1754, 1389, 1124, 1820, 1168, 1875, 1017, 1180, 1375, 1359, 1311, 1357, 1501, 1719,
    1584, 1609, 1977, 1786, 1232, 1263, 1748, 1664, 1693, 1766, 1598, 1053, 1277, 1466, 1877, 1844, 1829, 1165, 1606,
    1298, 1963, 1873, 1911, 1729, 1418, 1372, 1777, 1371, 1588, 1329, 1029, 1931, 1115, 1810, 1595, 1237, 1282, 1838,
    1642, 1937, 1343, 1578, 1425, 1814, 1690, 1129, 1321, 1174, 1863, 1405, 1066, 1220, 1780, 1410, 1156, 1991, 1568,
    1368, 99, 1750, 1280, 1400, 1601, 1804, 1363, 1613, 1252, 1434, 1094, 1867, 1542, 1093, 1926, 1251, 1348, 689,
    1441, 1913, 1969, 1409, 1201, 1459, 1110, 1452, 1051, 1860, 1346, 1537, 1060, 1182, 1386, 1141, 1184, 1989,
    1852, 1097, 1135, 1078, 1587, 1984, 1970, 1259, 1281, 1092, 1294, 1233, 1186, 1555, 1755, 1886, 1030, 1706,
    1313, 1481, 1998, 1181, 1244, 1269, 1684, 1798, 1023, 1960, 1050, 1293
]
INPUT.sort()

def get_two_entries_sum_up(m: int = 2020):
    n = len(INPUT)
    key = (0, n - 1)
    not_solved = True

    while not_solved:
        i, j = key
        partial_sum = INPUT[i] + INPUT[j]

        if partial_sum == m:
            not_solved = False
        elif partial_sum > m:
            key = (i, j - 1)
        else:
            key = (i + 1, n - 1)

        if key[1] == 0:
            return 0, 0, 0, 0

    return INPUT[i], INPUT[j], partial_sum, INPUT[i] * INPUT[j]


def get_three_entries_sum_up(m: int = 2020):
    n = len(INPUT)
    for i in range(n):
        a, b, two_sum, _ = get_two_entries_sum_up(m - INPUT[i])
        if two_sum != 0:
            break

    if two_sum == 0:
        return 0, 0, 0, 0, 0

    return INPUT[i], a, b, INPUT[i] + a + b, INPUT[i] * a * b


"""
Results: 
    In [6]: get_two_entries_sum_up()
    Out[6]: (883, 1137, 2020, 1003971)
    
    In [10]: get_three_entries_sum_up()
    Out[10]: (99, 689, 1232, 2020, 84035952)
"""