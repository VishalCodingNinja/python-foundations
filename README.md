# Python Foundations: session code

Code for the **Python Foundations** live session on
[The Growth Club](https://www.youtube.com/@TheGrowthClubOfficial) YouTube channel,
presented by Vishal Singh.

Every demo from the slides is here as a runnable file, plus one exercise per module
with a starter file and a worked solution.

## What you need

- Python 3.10 or newer: download it from [python.org](https://www.python.org/downloads/).
  On Windows, tick **"Add python.exe to PATH"** in the installer.
- Any editor. VS Code with the Python extension works well.

Check your install:

```bash
python --version
```

## Run an example

From this folder:

```bash
python 01_data_types_io/tax_calculator.py
```

## What's inside

| Folder | Module | Files |
|---|---|---|
| `01_data_types_io` | 1 · Data Types and Input and Output | `data_types.py`, `tax_calculator.py`, `strings_input_output.py`, `age_calculator.py` |
| `02_conditionals_imports` | 2 · Conditionals and Imports | `conditionals.py`, `operators_booleans.py`, `rock_paper_scissors.py`, `imports_demo.py`, `rock_paper_scissors_random.py` |
| `03_lists_loops` | 3 · Lists and Loops | `lists_loops.py`, `sum_expenses.py`, `range_loops.py`, `loan_calculator.py` |
| `04_dicts_json_pip` | 4 · Dictionaries, JSON, and Pip | `dictionaries.py`, `movie_schedule.py`, `lists_and_dicts.py`, `nested_contacts.py`, `json_basics.py`, `weather_api.py` |
| `05_functions` | 5 · Functions | `functions.py`, `dice_game.py` |
| `06_classes` | 6 · Classes and Objects | `employee.py`, `payroll.py`, `inheritance.py`, `payroll_inheritance.py` |
| `07_files_exceptions` | 7 · Working with Files and Exceptions | `exceptions.py`, `reading_files.py`, `writing_files.py`, `file_manipulation.py`, `file_organizer.py` |
| `exercises` | Your turn | `ex01` to `ex07`: a task and a starter file per module |
| `solutions` | Answers | Worked solutions for `ex01` to `ex07` |

`hello.py` is the classic first program.

## Virtual environment and pip (Module 4)

Only `04_dicts_json_pip/weather_api.py` needs a package from outside Python (`requests`).
Install it into a virtual environment so it stays with this project:

```bash
python -m venv .venv
```

Activate it. On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Then install the packages:

```bash
pip install -r requirements.txt
```

The weather demo also needs a free API key from [openweathermap.org](https://openweathermap.org).
Store it in an environment variable rather than in the code. In PowerShell:

```bash
$env:OPENWEATHER_API_KEY = "your-key"
```

## Exercises

1. Open a file in `exercises/` and read the task at the top.
2. Replace the `TODO` comments with your code and run it.
3. Stuck? Compare with the matching file in `solutions/`.

| Exercise | Module | You practise |
|---|---|---|
| `ex01_tip_calculator.py` | 1 | input(), type conversion, f-strings |
| `ex02_guess_the_number.py` | 2 | random, if / elif / else |
| `ex03_grade_book.py` | 3 | lists, range(), loops |
| `ex04_word_counter.py` | 4 | dictionaries, JSON |
| `ex05_temperature_converter.py` | 5 | functions, return, default values |
| `ex06_bank_account.py` | 6 | classes, inheritance, super() |
| `ex07_notes_app.py` | 7 | files, try / except |

## Safe to experiment

The file demos in `07_files_exceptions` only touch files they create themselves
(`list.txt`, `playground/`, `messy_folder/`). Delete those any time; the scripts
recreate them.
