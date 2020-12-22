def multiply_vec(vec):
    return sum(i * e for i, e in enumerate(vec[::-1], 1))


def crab_combat(filename="data/day22.dat"):
    player1, player2 = open(filename).read().split("\n\n")
    player1 = [int(i) for i in player1.split('\n')[1:]]
    player2 = [int(i) for i in player2.split('\n')[1:]]

    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)

        price = sorted([p1, p2], reverse=True)

        if p1 > p2:
            player1.extend(price)
        else:
            player2.extend(price)

    return multiply_vec(player2) if player2 else multiply_vec(player1)


def recursive_combat(filename="data/day22.dat"):
    player1, player2 = open(filename).read().split("\n\n")
    player1 = [int(i) for i in player1.split('\n')[1:]]
    player2 = [int(i) for i in player2.split('\n')[1:]]

    def recursive(p1, p2):
        was = set()
        while p1 and p2 and str([p1, p2]) not in was:
            was.add(str([p1, p2]))
            a = p1.pop(0)
            b = p2.pop(0)

            if a <= len(p1) and b <= len(p2):
                tf = recursive(p1[:a], p2[:b])
            else:
                tf = a < b

            if tf:
                p2.extend([b, a])
            else:
                p1.extend([a, b])

        return not p1

    return multiply_vec(player2) if recursive(player1, player2) else multiply_vec(player1)


assert recursive_combat(filename="data/day22-t.dat") == 291
assert crab_combat(filename="data/day22-t.dat") == 306

crab_combat()  # 34255
recursive_combat()