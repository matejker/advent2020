from math import radians, sin, cos
import numpy as np


def rain_risk_navigation(filename="data/day12.dat"):
    with open(filename) as fdata:
        position = 0
        coordinates = np.zeros(2)  # (East, North)

        directions = {"E": 0, "N": 90, "W": 180, "S": 270}

        def rotate(d, v, p):
            if d == "R":
                p -= v
            elif d == "L":
                p += v
            return p % 360

        for line in fdata:
            line_split = line.replace("\n", "")
            direction = line_split[0]
            value = int(line_split[1:])

            if direction in ["L", "R"]:
                position = rotate(direction, value, position)
            elif direction in directions:
                p = directions[direction]
                coordinates += np.array([cos(radians(p)), sin(radians(p))]) * value
            else:
                coordinates += np.array([cos(radians(position)), sin(radians(position))]) * value

    return np.round(np.sum(np.abs(coordinates)))


def waypoint_navigation(filename="data/day12.dat"):
    with open(filename) as fdata:
        coordinates = np.array([0, 0])  # (East, North)
        waypoint = np.array([10, 1])

        directions = {"E": np.array([1, 0]), "N": np.array([0, 1]), "W": np.array([-1, 0]), "S": np.array([0, -1])}

        def rotate(d, v, w):
            if d == "R":
                if v == 90:
                    return np.array([w[1], -w[0]])
                elif v == 180:
                    return np.array([-w[0], -w[1]])
                elif v == 270:
                    return np.array([-w[1], w[0]])
            elif d == "L":
                if v == 90:
                    return np.array([-w[1], w[0]])
                elif v == 180:
                    return np.array([-w[0], -w[1]])
                elif v == 270:
                    return np.array([w[1], -w[0]])
            return w

        for line in fdata:
            line_split = line.replace("\n", "")
            direction = line_split[0]
            value = int(line_split[1:])

            if direction in ["L", "R"]:
                waypoint = rotate(direction, value, waypoint)
            elif direction in directions:
                waypoint += directions[direction] * value
            else:
                coordinates += waypoint * value

    return np.round(np.sum(np.abs(coordinates)))


assert rain_risk_navigation(filename="data/day12-t.dat") == 25
assert waypoint_navigation(filename="data/day12-t.dat") == 286

rain_risk_navigation()  # 445
waypoint_navigation()  # 42495
