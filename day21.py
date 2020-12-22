from hopcroftkarp import HopcroftKarp


def gluten_morgen(filename="data/day21.dat"):
    food = []
    total_food = []
    allergens = {}
    with open(filename) as fdata:
        for i, line in enumerate(fdata):
            f, a = line.strip().split(" (contains ")
            total_food.extend(f.split(" "))
            food.append(f.split(" "))
            allgs = a[:-1].split(", ")
            for a in allgs:
                if a in allergens:
                    allergens[a].append(i)
                else:
                    allergens[a] = [i]

    def intersection(*food_chains):
        master_set = set(food[food_chains[0]])
        for f in food_chains:
            master_set &= set(food[f])

        return master_set

    ing = set()
    final_dict = {}
    for a in allergens:
        inter = intersection(*allergens[a])
        final_dict[a] = list(inter)
        ing = ing.union(inter)
    print(final_dict)
    matching = HopcroftKarp(final_dict).maximum_matching(keys_only=True)
    alph = ",".join(matching[a] for a in sorted(matching))
    return len([f for f in total_food if f not in ing]), alph


gluten_morgen(filename="data/day21-t.dat")
gluten_morgen()
