expenses = []

food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))
shopping = float(input("Enter shopping expense: "))

expenses.append(food)
expenses.append(travel)
expenses.append(shopping)

total = sum(expenses)

print("Expenses:", expenses)
print("Total expense:", total)