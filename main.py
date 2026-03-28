from expense_manager import add_expense, view_expenses, delete_expense, total_expense, category_summary

def menu():
    while True:

        print("\nSmart Expense Tracker")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Delete Expense")
        print("4 Total Spending")
        print("5 Category Summary")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Travel/etc): ")
            note = input("Enter note: ")

            add_expense(amount, category, note)
            print("Expense added!")

        elif choice == "2":
            expenses = view_expenses()

            if not expenses:
                print("No expenses found")
            else:
                for i, exp in enumerate(expenses):
                    print(f"{i}. {exp['amount']} | {exp['category']} | {exp['note']}")

        elif choice == "3":
            index = int(input("Enter index to delete: "))

            if delete_expense(index):
                print("Deleted successfully")
            else:
                print("Invalid index")

        elif choice == "4":
            print("Total spending:", total_expense())

        elif choice == "5":
            summary = category_summary()

            for cat, amt in summary.items():
                print(cat, ":", amt)

        elif choice == "6":
            break

        else:
            print("Invalid choice")

menu()