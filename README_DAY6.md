## Day 6 Progress

[![Day 6](https://img.shields.io/badge/Day%206-Refactoring%20%26%20Code%20Structure-blue)](https://github.com/Shahadatsiddique/personal-expense-tracker_from-_scratch)

Today I focused on refactoring my Personal Expense Tracker and improving the overall code structure. I converted repeated and related operations into reusable functions so that the program became easier to read, maintain, and understand without changing its existing functionality.

### Features Added

- Refactored repeated code into reusable functions
  - Created `save_expenses()` for JSON file saving
  - Created `show_menu()` for displaying the application menu
  - Created `add_expense()` for adding new expenses
  - Created `view_expense()` for displaying all expenses
  - Created `view_total_spending()` for calculating total spending
  - Created `delete_expense()` for deleting an expense
  - Created `update_expense()` for editing an existing expense

- Improved code organization
  - Separated different responsibilities into functions
  - Reduced repeated code
  - Made the main program loop cleaner
  - Passed the `expenses` list to functions where required

- Kept existing functionality
  - Add expense
  - View expenses
  - View total spending
  - Delete expense
  - Update expense
  - Search expense
  - Category-wise total
  - Date filtering
  - Expense summary
  - JSON persistence

### Testing

- Tested adding expenses after refactoring
- Tested viewing all expenses
- Tested total spending calculation
- Tested updating expenses
- Tested deleting expenses
- Tested searching expenses
- Tested category-wise totals
- Tested date filtering
- Tested expense summary
- Tested JSON persistence after restarting the application

All existing features continued to work after refactoring.

### What I Learned

Today I learned that refactoring is not about adding new features. It is about improving the internal structure of existing code without changing what the program is supposed to do.

I also learned how functions can be used to divide a larger program into smaller responsibilities, making the code easier to understand, maintain, test, and improve.

###Day 6 code structure

Expense Tracker
│
├── JSON Loading
├── save_expenses()
├── show_menu()
│
├── add_expense()
├── view_expense()
├── view_total_spending()
├── delete_expense()
├── update_expense()
├── search_expense()
├── category_wise_total()
├── filtering_data()
└── expense_summary()


### Next — Day 7

- Improve input handling and validation
- Handle invalid inputs inside the appropriate functions
- Improve error messages
- Test more edge cases
- Continue improving code quality

The main goal is to make the application more reliable while keeping the code simple and understandable.
