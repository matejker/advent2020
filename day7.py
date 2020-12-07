import re

GOLD = "shiny gold"


def get_shiny_golds(filename="data/day7.dat"):
    with open(filename) as fdata:

        graph = {}
        gold_parents = set()

        for line in fdata:
            line_split = line.replace("\n", "").split(" bags contain ")
            leaves = line_split[1].split(", ") if line_split[1] != "no other bags." else []

            graph[line_split[0]] = [
                re.sub(r"[0-9] ", "", re.sub(r" (bags|bag)", "", l)).replace(".", "") for l in leaves
            ]

            if GOLD in graph[line_split[0]]:
                gold_parents.add(line_split[0])

        for _ in graph:
            for n in graph:
                if gold_parents.intersection(set(graph[n])):
                    gold_parents.add(n)

    return len(gold_parents)


def individual_bags_per_gold(filename="data/day7.dat"):
    with open(filename) as fdata:
        graph = {}
        weighted_graph = {}

        for line in fdata:
            line_split = line.replace("\n", "").split(" bags contain ")
            leaves = line_split[1].split(", ") if line_split[1] != "no other bags." else []

            graph[line_split[0]] = [
                re.sub(r"[0-9] ", "", re.sub(r" (bags|bag)", "", l)).replace(".", "") for l in leaves
            ]
            weighted_graph[line_split[0]] = [
                (re.sub(r"[0-9] ", "", re.sub(r" (bags|bag)", "", l)).replace(".", ""), int(re.sub(" (.*)", "", l)))
                for l in leaves
            ]

    def get_count(root):
        count = 0
        for parent, num in weighted_graph[root]:
            count += num + (num * get_count(parent))
        return count

    return get_count(GOLD)


assert get_shiny_golds("data/day7-t.dat") == 4
assert individual_bags_per_gold("data/day7-t2.dat") == 126

get_shiny_golds()  # 229
individual_bags_per_gold()  # 6683
