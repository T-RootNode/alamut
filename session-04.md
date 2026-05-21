# Session 04 — Functions: Define and Call

## Status
Done.

## Concept for this session
Functions — defining reusable blocks of code and calling them.

## What I already know (going in)
- `int`, `float`, `str`, `bool` and type conversion
- `input()` always returns `str`
- `if`, `elif`, `else`
- `while True` with `break`

## What I learned
- `def` defines a function — like declaring a variable, but for actions
- The function must be defined before it is called (Python reads top to bottom)
- `()` are always required — both when defining and when calling
- Calling a function by name alone (without `()`) does nothing
- A function that prints handles its own output — no `print()` needed at the call site

## Code written this session

```python
####################################################
# Thing 04 - 21.05.2026
#
# WHAT I LEARNED:
#   - def defines a function, must come before the loop
#   - name() calls the function — () are required
#
####################################################

def show_menu():
    print("===Alamut===")
    print("1 = Backup starten")
    print("2 = Status anzeigen")
    print("3 = Beenden")

while True:
    show_menu()
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
- Functions with parameters
- Return values
- `for` loops
- `try` / `except`
- File handling

## Next session (rough idea, not committed)
Functions with parameters — passing data in.

## Notes for next chat
Start of next chat: paste this file + CLAUDE.md + README.md back in,
say "Session 05 starten" and the tutor begins with the first exercise.
