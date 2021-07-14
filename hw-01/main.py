import math


def share_bread(n, k):
    y = k % n
    x = k // n
    return x, y


assert share_bread(n=3, k=14) == (4, 2)
assert share_bread(n=3, k=12) == (4, 0)


def leap_year(year):
    if year % 400 == 0:
        return "YOU SHALL PASS"

    if year % 4 == 0 and year % 100 != 0:
        return "YOU SHALL PASS"

    return "YOU SHALL NOT PASS"


assert leap_year(5) == "YOU SHALL NOT PASS"
assert leap_year(4) == "YOU SHALL PASS"
assert leap_year(300) == "YOU SHALL NOT PASS"
assert leap_year(400) == "YOU SHALL PASS"


def amulet_area(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


assert amulet_area(3, 4, 5) == 6
