introduction = ("Welcome!")
greeting = introduction.upper()
print(f"{greeting} Budgeting made worry-free at your service!")
monthly_budget = input("Enter amount you earn monthly: ")
fixed_expenses = {"Housing" : 0, "Transportation" : 0, "Groceries" : 0, "Debt" : 0, "Savings & investments" : 0}
def input_expenses():
    for name in fixed_expenses:
        expense = input(f"Enter a value for {name}: ")
        fixed_expenses[name] = int(expense)
print(fixed_expenses) 
input_expenses()      
def math_fixed_expenses():
    answer = 0
    for values in fixed_expenses.values():
        answer += values
    print(answer)
math_fixed_expenses()        
worry_free_money = {"Selfcare" : 0, "Entertainment" : 0, "Miscellaneous" : 0}
def worry_free_expenses(expenses_dict):
    for title in expenses_dict:
        freefunds = input(f"Enter a value for {title}")   
        expenses_dict[title] = int(freefunds)  
worry_free_expenses(worry_free_money)  
def worry_free_calculations(expenses_dict):
    total = 0
    for values in expenses_dict.values():
        total += values
    print(total)  
worry_free_calculations(worry_free_money)      
# def new_category(worry_free_money):
#     enter_category = input("Add a category: ")
#     if enter_category in worry_free_money:
#         print(f"{enter_category} already exists.")
#     else:
#         worry_free_money[enter_category] = 0
#         print(f"{enter_category} has been added")
    
