## Day 2 Progress

Today I improved the reliability and usability of my CLI Expense Tracker.

### Features Added

* Date validation using Python's `datetime` module
* Amount validation

  * Rejects non-numeric input
  * Rejects zero
  * Rejects negative values
* Category and description validation
* Delete expense functionality
* Improved expense display
* Formatted amounts using two decimal places
* Improved error handling with `try/except`

### Testing

I tested the application with:

* Valid expenses
* Invalid dates
* Impossible dates
* Invalid amounts
* Zero and negative amounts
* Empty category and description
* Deleting valid expenses
* Invalid expense numbers
* Empty expense list scenarios

### What I Learned

Day 2 helped me understand that input validation and error handling are important even in a small CLI application. A program should not only work with correct input but should also handle incorrect input without crashing.

**Next:** Update/Edit Expense and Search functionality.
