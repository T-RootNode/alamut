# Session 02 — if / else / elif

## Status
Done.

## Concept for this session
Making decisions in code with `if`, `else`, and `elif`.

## What I already know (going in)
- `int`, `float`, `str`, `bool` and how to convert between them
- `type()` to inspect a variable
- `input()` always returns `str`
- Basic conditions from `while` loops (`n < 10`)

## What I learned
- `if`, `elif`, `else` check conditions in order — first match wins, rest is skipped
- `=` assigns a value, `==` compares two values
- `input()` always returns `str` — convert with `int()` before comparing to numbers
- Avoid calling `int(z)` multiple times — convert once, store in a variable, reuse it
- `elif` handles the "in between" case that `if`/`else` alone can't cover

## Code written this session

```python
####################################################
# Thing 02 - 18.05.2025
#
# WHAT I LEARNED:
#   - if / elif / else — branching based on conditions
#   - == is comparison, = is assignment
#   - convert input() result once with int(), then reuse the variable
#
####################################################

z = input("bitte eine zahl ein geben")
x = int(z)
if x > 10:
    print("größer als 10")
elif x == 10:
    print("es ist 10")
else:
    print("kleiner als 10")
```

## Out of scope for this session
- Functions
- Loops over lists (`for`)
- `try` / `except`
- File handling
- Anything Alamut-related

## Next session (rough idea, not committed)
`while` loops revisited, or `for` loops — repeating things properly.

## Notes for next chat
Start of next chat: paste this file + CLAUDE.md + README.md back in,
say "Session 03 starten" and the tutor begins with the first exercise.
