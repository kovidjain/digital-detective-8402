# Mission 5 — Numbers and data

## 1. Place-value systems

The base of a number system determines how many symbols are available and how each position is weighted.

| System | Base | Digits used | Example |
| --- | ---: | --- | --- |
| Decimal | 10 | `0` to `9` | `245` |
| Binary | 2 | `0` and `1` | `11110101` |
| Hexadecimal | 16 | `0` to `9` and `A` to `F` | `F5` |

In decimal, the number `245` means `(2 × 10²) + (4 × 10¹) + (5 × 10⁰)`. In binary, `11110101` means `(1 × 2⁷) + (1 × 2⁶) + (1 × 2⁵) + (1 × 2⁴) + (0 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)`, which equals decimal `245`. The hexadecimal form `F5` also equals decimal `245`.

## 2. Bits and bytes

A bit is one binary digit and can hold either `0` or `1`. A byte is commonly eight bits. Grouping bits into bytes makes it easier to store and transfer values, text, colours, and instructions.

For example:

```text
11110101  =  F5  =  245
```

Hexadecimal is useful because one hexadecimal digit represents four binary bits. Two hexadecimal digits can therefore represent one byte.

## 3. Text encoding

Computers store text as numeric code points that are represented as bits and bytes. ASCII covers a basic set of characters, while Unicode provides code points for a much wider range of writing systems and symbols. UTF-8 is a common Unicode encoding that uses one to four bytes per character.

The character `A` has the same value in ASCII and Unicode, and its UTF-8 byte is `01000001`. A character outside the basic ASCII range can require more than one UTF-8 byte. Decoding uses the same encoding rule in reverse so that the stored bytes become readable text.

## 4. Why the representation matters

The same underlying value can be displayed in different bases without changing the value. This is useful in different contexts:

- Decimal is familiar for quantities and everyday calculations.
- Binary matches the two-state representation used by digital hardware.
- Hexadecimal makes long binary values easier to read, especially in programming and debugging.
- Text encodings let software exchange written information consistently.

The representation must still be interpreted with the correct base or encoding. Reading a binary value as decimal, or decoding UTF-8 bytes with the wrong character encoding, produces a different result.
