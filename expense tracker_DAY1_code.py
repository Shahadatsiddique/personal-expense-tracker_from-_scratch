expenses=[]

print("welcome to my expense tracker project")

while True:
    print("___menu___")
    print("1.add expense")
    print("2.view all expenses")
    print("3.view total spend")
    print("4.exit")


    try:
        choice=int(input("please enter your choice :"))

        if (choice==1):
            date=input("enter the spending date ? ").strip()
            category=input("enter the type of item ? ").strip()
            description=input("enter short description related spending ").strip()
            try:
                amount =float(input("enter the amount : "))
            except ValueError:
                print("invalid amount, please enter a valid number")
                continue

            is_valid = True
            if amount<=0:
                print("invalid amount, amount must be greater than 0")
                is_valid = False
            if category=="":
                print("category can't be empty")
                is_valid = False
            if description=="":
                print("description can't be empty")
                is_valid = False
            if date=="":
                print("date can't be empty")
                is_valid = False
            if is_valid:
                expense={
                     "date":date,
                    "category":category,
                    "description":description,
                    "amount":amount
                }

                expenses.append(expense)
                print("\n expenses added successfully")

        elif(choice==2):
            if(len(expenses)==0):
                print("no expense done yet")
            else:
                print("___ this is you expense___")
                count=1
                for eachexpense in expenses:
                    print(f"expense number {count} = {eachexpense['date']}, {eachexpense['category']}, {eachexpense['description']}, {eachexpense['amount']}")
                    count+=1

        elif(choice==3):
            total=0
            for eachexpenses in expenses:
                total=total + eachexpenses["amount"]

            print("\n total expense = ",total)

        elif(choice==4):
            print("thank you for using our system")
            break

        else:
            print("you entered a invalid choice")
            
    except ValueError:
        print("invalid input")
