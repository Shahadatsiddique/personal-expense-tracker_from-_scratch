Personal Expense Tracker — Built From Scratch

A command-line Personal Expense Tracker built in Python from scratch as a hands-on learning project.

Progress

Day 1

CLI menu

Add expense

View expenses

Total spending

Basic validation

try/except

.strip()

Boolean validation

Day 2

Date validation with datetime.strptime()

DD-MM-YYYY format

Amount formatting with :.2f

Delete expense

Invalid expense-number handling

Edge-case testing

Day 3

Update/edit existing expenses

Update date, category, description, and amount

Cancel update

Category-based search

found Boolean flag

Original expense numbering in search results

Full integration testing

Current Features

Add expense

View all expenses

View total spending

Delete expense

Update expense

Search expense by category

Exit

Data Structure

Each expense is stored as a dictionary inside a list:

{
    "date": "10-02-2026",
    "category": "momos",
    "description": "food",
    "amount": 90.0
}

Concepts Practiced

Lists and dictionaries

if / elif / else

for and while loops

try / except

ValueError

.strip()

datetime.strptime()

Boolean flags

List indexing

append() and pop()

f-strings

Number formatting

Input validation

Menu-driven CLI design

Roadmap

Day 1 — CLI foundation

Day 2 — Validation, formatting, delete

Day 3 — Update and category search

Day 4 — Category-wise totals, date filtering, summary/report

Day 5 — JSON persistence

Day 6 — Refactoring into functions/modules and stronger error handling

Day 7 — Final cleanup, documentation, GitHub, interview preparation

Why I Built This

I am building this project from scratch so that I understand the logic behind every feature instead of simply using ready-made code.

Tech Stack

Python

Standard Library (datetime)

Command Line Interface

Current status: Day 3 completed.
