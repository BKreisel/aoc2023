import importlib
from argparse import ArgumentParser
from pathlib import Path

import rich


def run_cli() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "day",
        help="The day of the puzzle to run.",
        type=int,
    )

    parser.add_argument(
        "part",
        help="The part of the day to run.",
        type=int,
        choices=[1,2],
    )

    args = parser.parse_args()

    try:
        module = importlib.import_module(f"aoc2023.puzzles.day{args.day:02}")
    except ModuleNotFoundError:
        rich.print(f"Error: Day {args.day:02} not found.")
        return

    input_path = Path(__file__).parent / "inputs" / f"{args.day:02}.txt"

    with input_path.open() as fd:
        data = fd.read()

    rich.print(f"🎄 Running Day {args.day:02} Part {args.part}:")
    if args.part == 1:
        module.part1(data)
    else:
        module.part2(data)
