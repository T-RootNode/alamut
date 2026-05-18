# Session 01 — Data Types

## Status
Done.

## Concept for this session
Data types and what you can do with them.

## What I already know (going in)
- Variables (`n = 1`)
- `while` loop
- Conditions (`n < 10`)
- Reassigning variables (`n = n + 1`)
- f-strings with variable insertion (`f"... {n}"`)
- `print`
- Vague intuition: `5` and `"5"` are different things (int vs string)

## What I should know by the end
- The main types: `int`, `float`, `str`, `bool`
- How to convert between types (`int()`, `str()`, `float()`)
- Why type matters: user input via `input()` is always a string, even when the user types a number
- What happens when you mix types in operations (and why Python sometimes refuses)

## What I learned
- `int`, `float`, `str`, `bool` are the main types
- `type()` shows you what type a variable is
- Python refuses to mix `int` and `str` in operations — TypeError
- `int()` converts a string to an integer — useful for `input()` results
- `input()` always returns a string, even if the user types a number
- `int()` truncates, does not round — `int(3.7)` is `3`, not `4`
- `float` is a number with decimal places
- `bool` has exactly two values: `True` and `False`

## Commands used this session
- `type(x)` — shows the type of a variable
- `int(x)` — converts to integer, truncates decimals
- `float(x)` — converts to float
- `str(x)` — converts to string
- `input("text")` — reads user input, always returns str
- `round(x)` — rounds a number (not used, but good to know)

## How we worked this session
- Tutor (Claude) asks questions and gives small tasks
- I type code, run it, make mistakes
- On errors: I guess first, tutor gives hints, not answers
- No project code, no Alamut — just small exercises in a single `.py` file or the Python REPL
- One new concept per session — stop when my head is full, not when a plan is finished

## Out of scope for this session
- Functions
- Loops over lists (`for`)
- File handling
- Anything Alamut-related

## Next session (rough idea, not committed)
`if` / `else` — making decisions in code.

## Notes for next chat
Start of next chat: paste this file + CLAUDE.md + README.md back in,
say "Session 02 starten" and the tutor begins with the first exercise.
