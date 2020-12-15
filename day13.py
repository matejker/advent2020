TEST_INPUT = [939, "7,13,x,x,59,x,31,19"]

INPUT = [1002578, "19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,751,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"]


def earliest_bus(input_data=INPUT):
    timestamp = input_data[0]
    buslines = [int(line) for line in input_data[1].split(",") if line != "x"]

    departures = [i - timestamp % i for i in buslines]

    return min(departures) * buslines[departures.index(min(departures))]


def get_lcm(input_data=INPUT):
    # Et tu, Brute?
    buslines = [(i, int(line)) for i, line in enumerate(input_data[1].split(",")) if line != "x"]
    multiple = max(i + l for i, l in buslines)

    while True:
        reminders = [(multiple + i) % l == 0 for i, l in buslines]
        if all(reminders):
            return multiple
        multiple += 1
        if multiple > 100000000000000:
            return False


def get_lcm2(input_data=INPUT):
    # Some loong forgotten algebra _Chinese reminder theorem_
    # https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    buslines = [(i, int(line)) for i, line in enumerate(input_data[1].split(",")) if line != "x"]
    buslines.sort(key=lambda tup: -tup[1])  # This method is faster if the moduli have been ordered by decreasing value

    multiple = x = buslines[0][1]
    for t, bus in buslines[1:]:
        while (x + t) % bus:
            x += multiple
        multiple *= bus
    return x


assert earliest_bus(TEST_INPUT) == 295

earliest_bus()  # 5257
get_lcm2()  # 538703333547789
