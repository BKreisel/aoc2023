from argparse import ArgumentParser
from pathlib import Path

import rich

from aoc2023.template import TEMPLATE


def scaffold(day: int) -> None:
    rich.print(f"🎄 Scaffolding Day: {day:02}")
    puzzles = Path(__file__).parent / "puzzles"
    puzzle_path = puzzles / f"day{day:02}.py"
    if puzzle_path.exists():
        msg = f"Day {day} already exists."
        raise ValueError(msg)
        return

    input_path = Path(__file__).parent / "inputs" / f"{day:02}.txt"
    rich.print(f" - Puzzle : {input_path}")
    rich.print(f" - Input  : {puzzle_path}")

    input_path.touch(exist_ok=True)
    with puzzle_path.open("w") as fd:
        fd.write(TEMPLATE.format(day=day))




def scaffold_cli():
    parser = ArgumentParser()
    parser.add_argument(
        "day",
        help="The aoc day to genereate files for.",
        type=int,
    )

    args = parser.parse_args()
    scaffold(args.day)
