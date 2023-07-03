class Category:
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.ledger = []

    def deposit(self, amount, description=''):
        self.amount += amount
        self.ledger.append({
            'amount': amount,
            'description': description,
        })

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description,
        })
        self.amount -= amount
        return True

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if not self.withdraw(amount, f'Transfer to {category.name}'):
            return False

        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return self.amount >= amount

    def __str__(self):
        result = self.name.center(30, '*')

        if self.ledger:
            result += '\n'
            result += '\n'.join(
                page['description'][:23].ljust(23) + f"{page['amount']:.2f}".rjust(7)
                for page in self.ledger
            )

        result += f'\nTotal: {self.amount:.2f}'

        return result


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent_amounts.append(sum(-page['amount'] for page in category.ledger if page['amount'] < 0))

    all_spent_amount = sum(spent_amounts)
    percentages = list(map(lambda x: int(x * 10 / all_spent_amount) * 10, spent_amounts))

    result = 'Percentage spent by category\n'
    for p in range(100, -1, -10):
        result += str(p).rjust(3) + '|'
        for percentage in percentages:
            result += f" {' ' if p > percentage else 'o'} "
        result += ' \n'
    result += ' ' * 4 + '-' * 3 * len(percentages) + '-\n'

    name_lines = []
    for idx in range(max(len(category.name) for category in categories)):
        line = ' ' * 4
        for category in categories:
            line += f" {category.name[idx] if idx < len(category.name) else ' '} "
        line += ' '
        name_lines.append(line)

    result += '\n'.join(name_lines)

    return result
