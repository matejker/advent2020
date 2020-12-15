"""
It seems to be that this is a "well know" sequence called "A181391" or Van Eck's sequence [1, 2].
Defined:
    For n >= 1, if there exists an m < n such that a(m) = a(n),
    take the largest such m and set a(n+1) = n-m;
    otherwise a(n+1) = 0.
    Start with a(1)=0.
    References:
    [1] The OEIS Foundation (2010), _Van Eck's sequence_, https://oeis.org/A181391
    [2] Numberphile (2019), _Don't Know (the Van Eck Sequence)_, https://www.youtube.com/watch?v=etMJxB-igrc
"""

TEST_INPUT = [1, 3, 2]
INPUT = [1, 2, 16, 19, 18, 0]


def memory_game(input_data=INPUT, n=2020):
    game = []
    numbers = {}
    m = len(input_data)

    for i in range(m):
        if i > 0:
            numbers[game[-1]] = i - 1
        number = input_data[i]
        game.append(number)

    for i in range(m, n):
        latest_number = game[-1]
        game.append(i - 1 - numbers.get(latest_number, i - 1))
        numbers[latest_number] = i - 1

    return game[-1]


assert memory_game(TEST_INPUT) == 1
assert memory_game([2, 1, 3]) == 10
assert memory_game([3, 1, 2]) == 1836

memory_game()  # 536
memory_game(INPUT, 30000000)  # 24065124
