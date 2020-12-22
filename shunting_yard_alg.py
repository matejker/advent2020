from operator import mul, add, sub, truediv, pow


class Operator:

    def __init__(self, name, precedence, associativity, func):
        self.name = name
        self.precedence = precedence
        self.associativity = 1 if associativity == "right" else 0
        self.func = func


operators = {
    "+": Operator("+", 2, "left", add),
    "-": Operator("-", 2, "left", sub),
    "*": Operator("*", 3, "left", mul),
    "/": Operator("/", 3, "left", truediv),
    "^": Operator("^", 4, "right", pow)
}


def has_precedence(a, b):
    return ((operators[b].associativity == 1 and operators[a].precedence > operators[b].precedence) or
            (operators[b].associativity == 0 and operators[a].precedence >= operators[b].precedence))


def evaluate_parenthesis(oprs):
    output = []
    while True:
        o = oprs.pop()
        if o == "(":
            break
        output.append(o)
    return output


def evaluate_for_operator(oprs, name):
    output = []
    while True:
        if not oprs:
            break
        if oprs[-1] not in operators:
            break
        if not has_precedence(oprs[-1], name):
            break
        output.append(oprs.pop())
    return output


def shunting_yard_algorithm(expression):
    operators_queue = []
    output = []
    for e in expression.split(" "):
        if e == "(":
            operators_queue.append(e)
        elif e == ")":
            output.extend(evaluate_parenthesis(operators_queue))
        elif e in operators:
            output.extend(evaluate_for_operator(operators_queue, e))
            operators_queue.append(e)
        elif e.isdigit():
            output.append(e)

    reverse_polish_notation = output + operators_queue[::-1]
    pile = []
    while reverse_polish_notation:
        e = reverse_polish_notation.pop(0)
        if e in operators:
            b = pile.pop()
            a = pile.pop()
            pile.append(operators[e].func(float(a), float(b)))
        else:
            pile.append(float(e))
    return pile[0]


assert shunting_yard_algorithm("( 2 + 2 ) ^ 3 + 5 * 2") == 74


def part2(filename="data/day18.dat"):
    sum = 0
    with open(filename) as fdata:
        for line in fdata:
            sum += shunting_yard_algorithm(line.strip())

    return sum