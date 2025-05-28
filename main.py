monthly_budget = input("Enter amount you earn monthly: ")
fixed_expenses = {"Housing" : 0, "Transportation" : 0, "Groceries" : 0, "Debt" : 0, "Savings & investments" : 0}
def input_expenses():
    for name in fixed_expenses:
        expense = input(f"Enter a value for {name}")
        fixed_expenses[name] = int(expense)
    print(fixed_expenses)       
input_expenses()
def math_fixed_expenses():
    answer = 0
    for values in fixed_expenses.values():
        answer += values
    print(answer)
math_fixed_expenses()        
# worry_free_money = {"Selfcare" : 0, "Entertainment" : 0, "Miscellaneous" : 0}
# make category function
# def list_category():
#     for name in budget_categories:
#         print(name)
# list_category() 
# for names, money_value in budget_categories.items():
#     print(f"{names} : {money_value}") 
