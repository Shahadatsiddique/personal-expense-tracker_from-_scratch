from datetime import datetime

expenses = []

print("welcome to my expense tracker project")

while True:
    print("___menu___")
    print("1.add expense")
    print("2.view all expenses")
    print("3.view total spend")
    print("4.delete expense")
    print("5.update expenses")
    print("6.search expense")
    print("7.category wise total")
    print("8.filtering data")
    print("9.expense summary")
    print("10.exit")

    try:
        choice = int(input("please enter your choice :"))

        if choice == 1:
            try:
                date = input("enter the spending date? : ").strip()
                datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                print("invalid date, please enter date in DD-MM-YYYY format")
                continue

            category = input("enter the type of item? : ").strip()
            description = input("enter short description related spending : ").strip()

            try:
                amount = float(input("enter the amount : "))
            except ValueError:
                print("invalid amount, please enter a valid number")
                continue

            is_valid = True
            if amount <= 0:
                print("invalid amount, amount must be greater than 0")
                is_valid = False
            if category == "":
                print("category can't be empty")
                is_valid = False
            if description == "":
                print("description can't be empty")
                is_valid = False
            if date == "":
                print("date can't be empty")
                is_valid = False

            if is_valid:
                expense = {
                    "date": date,
                    "category": category,
                    "description": description,
                    "amount": amount
                }
                expenses.append(expense)
                print("\n expenses added successfully")

        elif choice == 2:
            if len(expenses) == 0:
                print("no expense done yet")
            else:
                print("___ this is your expense___")
                count = 1
                for eachexpense in expenses:
                    print(
                        f"expense number {count}\n"
                        f"Date         :{eachexpense['date']}\n"
                        f"Category     :{eachexpense['category']}\n"
                        f"Description  :{eachexpense['description']}\n"
                        f"Amount       :Rs{eachexpense['amount']:.2f}"
                    )
                    print("_________________")
                    count += 1

        elif choice == 3:
            total = 0
            for eachexpenses in expenses:
                total = total + eachexpenses["amount"]
            print("_____Total spend_____")
            print(f"total expense = Rs{total:.2f}")
            print("______________________")

        elif choice == 4:
            if len(expenses) == 0:
                print("no expense to delete")
                continue
            expense_number = int(input("enter expense number to delete : "))
            if expense_number < 1 or expense_number > len(expenses):
                print("invalid expense number")
                continue
            expenses.pop(expense_number - 1)
            print("expense deleted successfully")

        elif choice == 5:
            print("update expense selected")
            if len(expenses) == 0:
                print("no expense yet to update, first create any expense")
                continue
            expense_number = int(input("enter a expense number to update : "))
            if expense_number < 1 or expense_number > len(expenses):
                print("you entered a invalid expense number to update : ")
                continue

            selected_expense = expenses[expense_number - 1]
            print("what you want to update?")
            print("1.date")
            print("2.category")
            print("3.description")
            print("4.amount")
            print("5.cancel")

            update_choice = int(input("please enter what you want to update: "))
            if update_choice < 1 or update_choice > 5:
                print("invalid update choice")
                continue

            if update_choice == 1:
                try:
                    new_date = input("enter new date: ").strip()
                    datetime.strptime(new_date, "%d-%m-%Y")
                except ValueError:
                    print("please enter a valid date format, dd-mm-year")
                    continue
                selected_expense["date"] = new_date

            elif update_choice == 2:
                new_category = input("enter new category : ").strip()
                if new_category == "":
                    print("please enter a valid category")
                    continue
                selected_expense["category"] = new_category

            elif update_choice == 3:
                new_description = input("enter new description : ").strip()
                if new_description == "":
                    print("enter a valid description")
                    continue
                selected_expense["description"] = new_description

            elif update_choice == 4:
                try:
                    new_amount = float(input("enter new amount : "))
                except ValueError:
                    print("please enter a valid amount")
                    continue
                is_valid = True
                if new_amount <= 0:
                    print("please enter a amount greater than 0")
                    is_valid = False
                if is_valid:
                    selected_expense["amount"] = new_amount

            elif update_choice == 5:
                print("now the update option is cancelled")
                continue

            print("expense updated successfully")

        elif choice == 6:
            if len(expenses) == 0:
                print("no expense done yet")
            else:
                search_input = input("enter category to search : ").strip()
                count = 1
                found = False
                for expense in expenses:
                    if expense["category"] == search_input:
                        print(
                            f"expense {count}\n"
                            f"Date         :{expense['date']}\n"
                            f"Category     :{expense['category']}\n"
                            f"Description  :{expense['description']}\n"
                            f"Amount       :Rs{expense['amount']:.2f}"
                        )
                        found = True
                    count += 1
                if found == False:
                    print("you entered search is not matched")

        elif choice == 7:
            category_name = input(
                "enter a category name to calculate amount : "
            ).strip()
            category_total = 0
            found = False
            for expense in expenses:
                if expense["category"] == category_name:
                    category_total = category_total + expense["amount"]
                    found = True
            if found == False:
                print("no category name matched")
            else:
                print(f"total amount of this category is Rs.{category_total:.2f}")

        elif choice == 8:
            try:
                date_to_search = input("enter date to search: ").strip()
                datetime.strptime(date_to_search, "%d-%m-%Y")
            except ValueError:
                print("you entered invalid input.. Please use DD-MM-YYYY format")
                continue

            found = False
            count = 1
            for expense in expenses:
                if expense["date"] == date_to_search:
                    print(
                        f"expense {count}\n"
                        f"Date         :{expense['date']}\n"
                        f"Category     :{expense['category']}\n"
                        f"Description  :{expense['description']}\n"
                        f"Amount       :Rs{expense['amount']:.2f}"
                    )
                    found = True
                count += 1

            if found == False:
                print("no expense found for this date")

        elif choice == 9:
            if len(expenses) == 0:
                print("No expenses recorded yet")
            else:
                total = 0
                for expense in expenses:
                    total = total + expense["amount"]

                average = total / len(expenses)

                print("_____Expense Summary_____")
                print(f"Total expenses  : {len(expenses)}")
                print(f"Total amount    : Rs{total:.2f}")
                print(f"Average expense : Rs{average:.2f}")
                print("________________________")

        elif choice == 10:
            print("thank you for using our system")
            break
        else:
            print("you entered a invalid choice")

    except ValueError:
        print("invalid input")
