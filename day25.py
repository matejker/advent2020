def decoder(code):
    i = 0
    number = 1
    while number != code:
        i += 1
        number = (number * 7) % 20201227
    return i


def handshake(loop_size, code):
    return pow(code, loop_size, 20201227)


def combo_breaker():
    door = 240583
    card = 12090988

    card_loop = decoder(door)
    door_loop = decoder(card)

    return handshake(door_loop, door), handshake(card_loop, card)


combo_breaker()  # (3015200, 3015200)
