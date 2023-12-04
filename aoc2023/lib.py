import rich


def assert_int(expected: int, actual: int) -> None:
    rich.print(f"Expected : {expected}")
    rich.print(f"Actual   : {actual}")
    assert expected == actual
