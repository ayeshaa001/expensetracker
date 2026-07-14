FILE_NAME = "expenses.txt"

expenses = []

try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            expenses.append(float(line.strip()))
except FileNotFoundError:
    open(FILE_NAME, "w").close()

while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            expense = float(input("Enter Expense Amount: "))

            if expense <= 0:
                print("Expense must be greater than 0.")
            else:
                expenses.append(expense)

                with open(FILE_NAME, "a") as file:
                    file.write(str(expense) + "\n")

                print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpenses")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense}")

    elif choice == "3":
        total = sum(expenses)
        print(f"\nTotal Spent = {total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("Invalid choice.")