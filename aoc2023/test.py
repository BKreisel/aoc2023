import importlib
import traceback
from argparse import ArgumentParser

import rich


def test_cli() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "day",
        help="The day of the puzzle to test.",
        type=int,
    )

    parser.add_argument(
        "part",
        help="The part of the day to test.",
        type=int,
        choices=[1,2],
    )

    args = parser.parse_args()

    try:
        module = importlib.import_module(f"aoc2023.puzzles.day{args.day:02}")
    except ModuleNotFoundError:
        rich.print(f"[red]Error: Day {args.day:02} not found.[/red]")
        return

    rich.print(f"🎄 Testing Day {args.day:02} Part {args.part}:")

    try:
        if args.part == 1:
            module.test1()
        else:
            module.test2()
    except AssertionError as err:
        assertion = traceback.extract_tb(err.__traceback__)[-1].line
        rich.print(f"[red]Test Failed: [/red]{assertion}")


