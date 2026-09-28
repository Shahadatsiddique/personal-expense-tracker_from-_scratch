## Day 7 Progress

[![Day 7](https://img.shields.io/badge/Day%207-Input%20Handling%20%26%20Validation-blue)](https://github.com/Shahadatsiddique/personal-expense-tracker_from-_scratch)

Today I focused on improving input handling, validation, error handling, and edge-case testing in my Personal Expense Tracker.

The main goal of Day 7 was to make the application more reliable by handling invalid and unexpected user inputs properly instead of allowing them to interrupt the program.

### Features Added / Improved

- Improved input handling
- Added empty input validation
  - Date cannot be empty
  - Category cannot be empty
  - Description cannot be empty
  - Amount cannot be empty

- Added numeric input validation
  - Invalid amount input
  - Invalid menu input
  - Invalid expense numbers
  - Invalid update choices

- Added positive amount validation
  - Amount must be greater than 0
  - Updated amount must also be greater than 0

- Improved date validation
  - Validates `DD-MM-YYYY` format
  - Rejects invalid calendar dates
  - Validates dates while adding expenses
  - Validates dates while updating expenses
  - Validates dates while filtering expenses

- Improved delete validation
  - Handles invalid expense numbers
  - Handles non-numeric expense numbers

- Improved update validation
  - Validates expense number
  - Validates update choice
  - Validates new date
  - Validates new category
  - Validates new description
  - Validates new amount
  - Allows the user to cancel an update

- Improved error handling
  - Used `try/except` for invalid numeric input
  - Used `return` to stop an operation when validation fails
  - Kept validation inside the appropriate functions

### Existing Features

The project now includes:

- Add expense
- View all expenses
- View total spending
- Delete expense
- Update expense
- Search expense
- Category-wise total
- Date filtering
- Expense summary
- JSON persistence

### Testing

I tested the application with different invalid, empty, boundary, and unexpected inputs.

The testing included:

- Empty date
- Empty category
- Empty description
- Empty amount
- Invalid numeric input
- Zero amount
- Negative amount
- Invalid expense number
- Expense number outside the available range
- Invalid update choice
- Invalid date format
- Invalid calendar dates
- Empty filtering date
- Invalid filtering date
- Date filtering with no matching expense
- Invalid main menu input

The final `filtering_data()` testing also passed the important invalid and boundary cases.

All existing features continued to work after adding the validation and error handling.

### What I Learned

Day 7 helped me understand that making a program work with valid input is not enough.

A reliable application should also handle incorrect and unexpected input safely.

I learned how to:

- Use `try/except` for error handling
- Use `return` to stop an operation when validation fails
- Validate different types of user input
- Validate dates using `datetime.strptime()`
- Handle boundary cases
- Test invalid inputs
- Place validation inside the appropriate functions

I also learned the importance of testing both normal cases and edge cases.

### Project Completion

With Day 7 completed, I have finished the planned development of my Personal Expense Tracker.

The project has gone through:

- Basic functionality
- Feature development
- Refactoring
- Code organization
- Input validation
- Error handling
- Edge-case testing
- JSON data persistence

The planned version of this project is now complete.

However, my learning does not stop here.

I will continue working on this project to improve my Python skills, problem-solving ability, code quality, and software-development understanding.

As a fresher, my goal is to keep building practical projects, strengthen my technical skills, become more competitive, and prepare myself for a good first opportunity in the software industry.

One project completed, but the learning continues. 🚀
