""" Day 02"""
from dataclasses import dataclass
from enum import Enum
from typing import Self

from aoc2023.lib import assert_int


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

@dataclass
class Round:
    red: int = 0
    blue: int = 0
    green: int = 0

    def add_color(self: Self, color: Color, count: int) -> None:
        setattr(self, color.value, getattr(self, color.value) + count)

    @classmethod
    def parse_line(cls: type[Self], line: str) -> Self:
        instance = Round()
        for item in line.split(","):
            count, color_str = item[1:].split(" ")
            instance.add_color(Color(color_str), int(count))
        return instance


@dataclass
class Game:
    ident: int
    rounds: list[Round]

    @classmethod
    def parse_line(cls: type[Self], line: str) -> Self:
        ident_str, rounds_str = line.split(":")
        return Game(
            ident=int(ident_str.split(" ")[-1]),
            rounds=[Round.parse_line(x) for x in rounds_str.split(";")],
        )

def valid_game(game: Game, bag: dict) -> bool:
    for k, v in bag.items():
       for round_item in game.rounds:
        if getattr(round_item, k.value) > v:
            return False
    return True

def calculate_power(game: Game) -> int:
    val = 1
    for color in Color:
        val *= max([getattr(x, color.value) for x in game.rounds])
    return val

def part1(data: str) -> int:
    """Run part 1 of day 02."""

    bag = {
        Color.RED: 12,
        Color.GREEN: 13,
        Color.BLUE: 14,
    }

    games = [Game.parse_line(x) for x in data.split("\n")]
    return sum([
        x.ident
        for x in games
        if valid_game(x, bag)
    ])


def part2(data: str) -> int:
    """Run part 2 of day 02."""

    games = [Game.parse_line(x) for x in data.split("\n")]
    return sum([
        calculate_power(x)
        for x in games
    ])


TEST_INPUT="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test1() -> None:
    """Test part 1 of day 02."""
    assert_int(8, part1(TEST_INPUT))


def test2() -> None:
    """Test part 2 of day 02."""
    assert_int(2286, part2(TEST_INPUT))

