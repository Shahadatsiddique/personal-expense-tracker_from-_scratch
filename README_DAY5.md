## Day 5 Progress

[![Day 5](https://img.shields.io/badge/Day%205-JSON%20Persistence-blue)](https://github.com/Shahadatsiddique/personal-expense-tracker_from-_scratch/tree/main)

Today I added JSON file handling to my Personal Expense Tracker so that expense data is stored permanently instead of being lost when the program is closed.

### Features Added

- Added JSON file persistence
  - Expense data is saved in `expense_tracker.json`
  - Existing data is loaded automatically when the program starts
  - New expenses are saved after adding
  - Updated expenses are saved after editing
  - Deleted expenses are saved after deletion

- Added file handling
  - Used `open()` to read and write the JSON file
  - Used `json.load()` to load existing expenses
  - Used `json.dump()` to save expenses

- Added missing-file handling
  - If the JSON file does not exist, the program starts with an empty expense list

### Testing

- Added an expense and checked that it was saved
- Closed and restarted the program
- Verified that previous expenses were still available
- Updated an expense and verified the change after restarting
- Deleted an expense and verified the deletion after restarting

### What I Learned

Today I learned how JSON file handling can be used to make application data persistent. I also learned how to load existing data when the program starts and save changes whenever the expense list is modified.

### Next — Day 6

- Refactor the code into reusable functions
- Reduce repeated code
- Improve code structure and readability
- Test the refactored application

The main goal is to make the project more structured without changing its existing functionality.
