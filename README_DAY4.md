## Day 4 Progress

Today I continued improving my CLI Expense Tracker by adding expense analysis, date filtering, and summary functionality.


### Features Added

- Category-wise total spending
  - Calculate total spending for a selected category
  - Search through stored expenses by category
  - Handle cases where no matching category is found
- Date-based expense filtering
  - Filter expenses using a specific date
  - Validate the entered date using `datetime`
  - Display matching expenses
  - Handle cases where no expense is found for the selected date
- Expense summary
  - Display total number of expenses
  - Calculate total amount spent
  - Calculate average expense amount
  - Handle cases where no expenses are recorded
- Improved expense handling
  - Used accumulator variables for total calculations
  - Used a `found` flag while searching and filtering
  - Used `datetime.strptime()` for date validation


### Testing

I tested the application with:

- Calculating total spending for an existing category
- Searching for a non-existing category
- Multiple expenses under the same category
- Filtering expenses using an existing date
- Filtering using a date with no matching expense
- Invalid date format
- Expense summary with multiple expenses
- Expense summary when no expenses are recorded


### What I Learned

Day 4 helped me understand how stored expense data can be processed to generate useful information instead of only adding, updating, and displaying records.

I also learned how to calculate category-wise totals, filter records based on a date, and generate a summary using total and average calculations.


### Next — Day 5

I will start working on data persistence using JSON:

- Create and use a JSON file for storing expenses
- Load existing expenses when the program starts
- Save new expenses to the JSON file
- Save updated expenses to the JSON file
- Save deleted expenses to the JSON file
- Test whether data remains available after restarting the program

The goal of Day 5 is to make the expense tracker persistent so that the stored expenses are not lost when the program is closed.
