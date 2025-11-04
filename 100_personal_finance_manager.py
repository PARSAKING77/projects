class PersonalFinanceManager:
    def __init__(self):
        self.expenses = []
        self.income = 0
        self.budget = 0

    def add_expense(self, amount, category):
        self.expenses.append((amount, category))

    def add_income(self, amount):
        self.income += amount

    def set_budget(self, amount):
        self.budget = amount

    def calculate_total_expenses(self):
        total_expenses = sum([expense[0] for expense in self.expenses])
        return total_expenses

    def calculate_remaining_budget(self):
        remaining_budget = self.budget - self.calculate_total_expenses()
        return remaining_budget

pf_manager = PersonalFinanceManager()
pf_manager.add_expense(50, 'Food')
pf_manager.add_expense(30, 'Transportation')
pf_manager.add_income(1000)
pf_manager.set_budget(500)

total_expenses = pf_manager.calculate_total_expenses()
remaining_budget = pf_manager.calculate_remaining_budget()

print(f"Total expenses: ${total_expenses}")
print(f"Remaining budget: ${remaining_budget}")
