# Session 03 — while + if/elif/else: CLI Menu

## Status
Done.

## Concept for this session
No new concept — consolidation. Combining everything learned into real Alamut code.

## What I already know (going in)
- `int`, `float`, `str`, `bool` and type conversion
- `input()` always returns `str`
- `if`, `elif`, `else`
- `while` loops and conditions

## What I learned
- `while True` runs forever until `break` stops it
- Everything that should repeat must be inside the loop
- This is real Alamut code — the main menu skeleton is done

## Code written this session

```python
####################################################
# Thing 03 - 21.05.2026
#
# WHAT I LEARNED:
#   - while True runs forever until break stops it
#   - everything that should repeat must be inside the loop
#
####################################################

while True:
    print("===Alamut===")
    print("1 = Backup starten")
    print("2 = Status anzeigen")
    print("3 = Beenden")
    input_raw = input("bitte eine zahl eingeben:")
    input_as_int = int(input_raw)
    if input_as_int == 1:
        print("gäbe es ein programm würde es nun laufen :)")
    elif input_as_int == 2:
        print("status alles ist hell")
    elif input_as_int == 3:
        break
    else:
        print("leider habe ich die eingabe nicht verstanden bitte nur zahlen 1-3")
```

## Out of scope for this session
- Functions
- `for` loops
- `try` / `except`
- Actually running backups or reading status
- File handling

## Next session (rough idea, not committed)
Functions — putting reusable logic into named blocks.

## Notes for next chat
Start of next chat: paste this file + CLAUDE.md + README.md back in,
say "Session 04 starten" and the tutor begins with the first exercise.
