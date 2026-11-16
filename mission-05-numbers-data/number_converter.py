"""Convert an integer between binary, decimal, and hexadecimal notation."""

import argparse


SUPPORTED_BASES = (2, 10, 16)


def convert_number(value: str, from_base: int, to_base: int) -> str:
    """Return ``value`` converted from one supported base to another."""
    if from_base not in SUPPORTED_BASES or to_base not in SUPPORTED_BASES:
        raise ValueError("bases must be 2, 10, or 16")

    try:
        number = int(value, from_base)
    except ValueError as error:
        raise ValueError(f"{value!r} is not valid base-{from_base} input") from error

    if to_base == 10:
        return str(number)
    if to_base == 2:
        return format(number, "b")
    return format(number, "X")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert an integer between bases 2, 10, and 16."
    )
    parser.add_argument("value", help="the number to convert")
    parser.add_argument(
        "from_base",
        type=int,
        choices=SUPPORTED_BASES,
        help="the input base",
    )
    parser.add_argument(
        "to_base",
        type=int,
        choices=SUPPORTED_BASES,
        help="the output base",
    )
    args = parser.parse_args()
    print(convert_number(args.value, args.from_base, args.to_base))


if __name__ == "__main__":
    main()