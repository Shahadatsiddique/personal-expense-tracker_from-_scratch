# personal-expense-tracker_from-_scratch

# Day 1 — Expense Tracker From Scratch

Today I started building my CLI Expense Tracker from scratch with a focus on **understanding the implementation rather than simply completing the project**.

## 🎯 Goal

The main goal of this project is to understand the code deeply by following this process:

**Understand → Implement → Test → Debug → Improve**

I am building the project step by step and testing each phase before moving to the next one.

## ✅ What I Completed on Day 1

### 1. Basic CLI Menu

Created a menu for:

* Add Expense
* View All Expenses
* View Total Spend
* Exit

### 2. Add Expense

Implemented expense creation using a Python dictionary containing:

* Date
* Category
* Description
* Amount

Expenses are currently stored in a Python list.

### 3. View Expenses

Implemented functionality to display all stored expenses with an expense number.

### 4. Total Spend

Implemented calculation of the total amount spent using a loop.

### 5. Input Validation

Added validation for:

* Amount must be greater than `0`
* Category cannot be empty
* Description cannot be empty
* Date cannot be empty
* Spaces-only input is handled using `.strip()`

### 6. Error Handling

Implemented `try/except` for invalid numeric input.

For example, entering:

```text
abc
```

for the amount is handled without crashing the program.

### 7. Multiple Validation Errors

Instead of stopping at the first validation error, I implemented an `is_valid` flag so multiple invalid fields can be identified before deciding whether the expense should be saved.

## 🧪 Testing Approach

I manually tested different scenarios, including:

* Valid expenses
* Decimal amounts
* Zero amount
* Negative amount
* Non-numeric amount
* Empty category
* Empty description
* Empty date
* Spaces-only input
* Multiple invalid fields at the same time

The goal was to verify the behavior of each feature before moving forward.

## 📚 Concepts Practiced

During Day 1, I worked with:

* Lists
* Dictionaries
* `while` loops
* `for` loops
* `if / elif / else`
* Multiple `if` conditions
* `try / except`
* `ValueError`
* `.strip()`
* `continue`
* `break`
* Boolean validation using an `is_valid` flag

## 🔜 Day 2 Plan

On Day 2, I will continue from the current version and work on:

1. Proper date validation
2. Improving error messages
3. Improving the CLI output
4. Testing the complete Add Expense workflow
5. Gradually adding the next useful expense-tracking feature

The project will continue to evolve step by step rather than adding advanced technologies before I understand the fundamentals.

**Day 1 completed. 🚀**
