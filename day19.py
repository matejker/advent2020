import re


def monster_messages(filename="data/day19.dat", part2=False):
    rules, messages = open(filename).read().split("\n\n")
    rules += "\n8: 42 | 42 8\n11: 42 31 | 42 11 31" if part2 else ""  # Part 2
    rules = {r.split(": ")[0]: r.split(": ")[1] for r in rules.split("\n")}

    def crossover(rule="0", n=0):
        if rules[rule] in ["a", "b"]:
            return rules[rule]
        if n > 30:
            return ""  # Here comes the loop

        return "(" + "|".join(["".join([crossover(ru, n + 1) for ru in r.split()]) for r in rules[rule].split("|")]) + ")"

    regex = re.compile(crossover())
    return len([ms for ms in messages.split() if re.fullmatch(regex, ms)])


assert monster_messages(filename="data/day19-t.dat", part2=False) == 2
assert monster_messages(filename="data/day19-t2.dat", part2=True) == 12

monster_messages()  # 192
monster_messages(part2=True)  # 296

# (((a(b((b(a(b(aa|b(a|b))|a(ab))|b(b(ba|bb)|a(bb|ab)))|a(b((ab)b)|a((aa)b|(ba|ab)a)))b|(a(b(b(ab)|a(aa|bb))|a((ba|ab)a|(ab)b))|b((b(bb|ab)|a(aa|ba))b|(a(ab|(a|b)a)|b(ab))a))a)|a(b((a((aa|bb)a|(ab|(a|b)a)b)|b((aa|bb)a|((a|b)(a|b))b))b|(((aa|ba)a|(aa|bb)b)b|(((a|b)(a|b))b|(bb|ab)a)a)a)|a(a(a((aa|ba)a|(aa|bb)b)|b(b(ab)|a((a|b)(a|b))))|b(a(a(aa|b(a|b))|b(ba|bb))|b(a(aa|bb)|b(bb))))))|b(a(a(((a(a(a|b)|bb)|b(aa|b(a|b)))b|((bb|ab)a)a)b|((a(aa|ba)|b(ba|ab))b|((aa)b|(ba|bb)a)a)a)|b(a(b(b(bb)|a(a(a|b)|bb))|a((bb|ab)a|(ab|(a|b)a)b))|b(b(a(bb)|b(bb))|a(b(bb|ab)|a(ba|bb)))))|b(((a(b(ba|bb)|a(bb|ab))|b(a(ba|bb)|b(aa|ba)))b|(((aa|bb)a|((a|b)(a|b))b)a|(b(a(a|b)|bb)|a(ab))b)a)a|(b(((aa)b|(ab)a)a|(b(aa|bb)|a(bb|ab))b)|a((a(ba|bb)|b(aa|ba))b|(((a|b)(a|b))a|(aa|bb)b)a))b))))((a(b((b(a(b(aa|b(a|b))|a(ab))|b(b(ba|bb)|a(bb|ab)))|a(b((ab)b)|a((aa)b|(ba|ab)a)))b|(a(b(b(ab)|a(aa|bb))|a((ba|ab)a|(ab)b))|b((b(bb|ab)|a(aa|ba))b|(a(ab|(a|b)a)|b(ab))a))a)|a(b((a((aa|bb)a|(ab|(a|b)a)b)|b((aa|bb)a|((a|b)(a|b))b))b|(((aa|ba)a|(aa|bb)b)b|(((a|b)(a|b))b|(bb|ab)a)a)a)|a(a(a((aa|ba)a|(aa|bb)b)|b(b(ab)|a((a|b)(a|b))))|b(a(a(aa|b(a|b))|b(ba|bb))|b(a(aa|bb)|b(bb))))))|b(a(a(((a(a(a|b)|bb)|b(aa|b(a|b)))b|((bb|ab)a)a)b|((a(aa|ba)|b(ba|ab))b|((aa)b|(ba|bb)a)a)a)|b(a(b(b(bb)|a(a(a|b)|bb))|a((bb|ab)a|(ab|(a|b)a)b))|b(b(a(bb)|b(bb))|a(b(bb|ab)|a(ba|bb)))))|b(((a(b(ba|bb)|a(bb|ab))|b(a(ba|bb)|b(aa|ba)))b|(((aa|bb)a|((a|b)(a|b))b)a|(b(a(a|b)|bb)|a(ab))b)a)a|(b(((aa)b|(ab)a)a|(b(aa|bb)|a(bb|ab))b)|a((a(ba|bb)|b(aa|ba))b|(((a|b)(a|b))a|(aa|bb)b)a))b)))(a((b((a(a(aa|bb)|b((a|b)b|ba))|b((ba|bb)a|(bb|ab)b))a|(a((ab|(a|b)a)a|(bb|ab)b)|b(a(bb|ab)|b(aa|ba)))b)|a(a(b((bb|ab)a|(ba|bb)b)|a(b(ba|bb)|a(bb|ab)))|b(a(b(bb|ab)|a(aa))|b(b(ab)|a(aa|bb)))))a|(b((a((aa|b(a|b))a|((a|b)b|ba)b)|b((aa|b(a|b))a|(aa|ba)b))a|(a((a(a|b)|bb)b|((a|b)b|ba)a)|b((bb|ab)a|(aa)b))b)|a(a(((ab)b|(aa)a)b|(a(ab)|b((a|b)(a|b)))a)|b(((ab)b)b|((a|b)(ba|ab))a)))b)|b((((b(a(ba|ab)|b((a|b)b|ba))|a(a((a|b)(a|b))|b(bb|ab)))b|((b(ba|bb)|a(a(a|b)|bb))a|(a(bb)|b(bb))b)a)a|(a(((ba|ab)a)b|((aa)b)a)|b(a((aa|b(a|b))b|(aa)a)|b(a(aa|ba)|b(ba|ab))))b)b|(((b(((a|b)b|ba)a|(bb)b)|a((aa|bb)a|((a|b)(a|b))b))b|(((aa|ba)b|(ba|bb)a)a|((ba|ab)a|(ab)b)b)a)b|((((ab)b|(aa)a)b|((a(a|b)|bb)a|(ba|ab)b)a)a|((a((a|b)b|ba)|b(a(a|b)|bb))a|(b(ab)|a((a|b)(a|b)))b)b)a)a))))