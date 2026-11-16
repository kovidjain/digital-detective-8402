# Mission 5 — Numbers and data

## Mission title

Numbers and data.

## Task / objective

I needed to explain how computers represent numbers and text, compare decimal, binary, and hexadecimal notation, and show how text can be encoded as data. I also completed the small number-converter program included in this mission.

## Work completed

- Explained the place-value systems used by decimal, binary, and hexadecimal numbers.
- Converted example values between bases.
- Described bits, bytes, and text encoding.
- Added a reusable Python number converter with input validation.
- Kept examples general and included no personal or device-specific data.

## Commands / tools used

- Python — implemented and tested the number converter.
- Markdown — wrote the number-system and encoding notes.
- Git — tracked the Mission 5 changes.
- GitHub — stored and reviewed the completed mission.

## My understanding

Computers use bits with two possible states, so binary is a natural way to represent data internally. Decimal is convenient for people, while hexadecimal is a shorter way to write groups of binary digits. Text is also stored as numeric codes through an encoding such as UTF-8.

## Difficulties faced

The main difficulty was keeping the direction of a conversion clear and handling invalid digits, such as a decimal digit appearing in a binary value.

## How I resolved them

I separated the source base from the target base in the converter's function, validated the allowed range before converting, and used Python's standard base-conversion support after validation.

## Evidence / files

- [`number-systems.md`](number-systems.md) — base systems, bits, bytes, and text encoding.
- [`number_converter.py`](number_converter.py) — tested Python converter for bases 2, 10, and 16.

## Commit details

Commit message: `Explain numbers and data representation`

Only Mission 5 files are included in this mission commit.
