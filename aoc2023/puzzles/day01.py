""" Day 01"""
from typing import Iterable

from aoc2023.lib import assert_int

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

digit_strings = list(digits.keys())

def check_str(line: Iterable) -> str | None:
    for digit in digit_strings:
        if line.startswith(digit):
            return digits[digit]
    return None

def get_value_p1(line: str) -> int:
    for char in line:
        if char.isdigit():
            first = char
            break
    for char in reversed(line):
        if char.isdigit():
            last = char
            break
    return int(first + last)

def get_value_p2(line: str) -> int:
    for idx, char in enumerate(line):
        if char.isdigit():
            first = char
            break
        if first := check_str(line[idx:]):
            break

    for idx, char in enumerate(reversed(line)):
        if char.isdigit():
            last = char
            break
        if last := check_str(line[-(idx+1):]):
            break

    return int(first + last)

def part1(data: str) -> int:
    """Run part 1 of day 01."""
    return sum(
        [
            get_value_p1(x)
            for x in data.split("\n")
            if len(x)
        ],
    )

def part2(data: str) -> int:
    """Run part 2 of day 01."""
    return sum(
        [
            get_value_p2(x)
            for x in data.split("\n")
            if len(x)
        ],
    )


TEST1_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST2_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def test1() -> None:
    """Test part 1 of day 01."""
    assert_int(142, part1(TEST1_INPUT))

def test2() -> None:
    """Test part 2 of day 01."""
    assert_int(281, part2(TEST2_INPUT))
