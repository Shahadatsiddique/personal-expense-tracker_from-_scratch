## Day 3 Progress

Today I continued improving my CLI Expense Tracker by adding Update/Edit and Search functionality.

### Features Added

- Update/Edit expense functionality
  - Update date
  - Update category
  - Update description
  - Update amount
  - Cancel an update operation

- Search expense functionality
  - Search expenses by category
  - Display matching expenses
  - Handle cases where no matching category is found

- Improved expense handling
  - Select an expense using its expense number
  - Added validation while updating expense details
  - Used a `found` flag to handle search results
  - Maintained correct expense numbering while searching

### Testing

I tested the application with:

- Updating date
- Updating category
- Updating description
- Updating amount
- Cancelling an update
- Invalid expense numbers
- Invalid dates
- Invalid amounts
- Empty category and description
- Searching existing categories
- Searching non-existing categories
- Searching with multiple expenses

### What I Learned

Day 3 helped me understand how to modify existing data stored inside a list of dictionaries instead of only adding and displaying data.

I also learned how to search through stored records using conditions and how a `found` flag can be used to handle cases where no matching data exists.

**Next:** Expense analysis and reporting — category-wise total spending, date-based filtering, and better expense summaries.
