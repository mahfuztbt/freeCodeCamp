class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.cash_out = 0

    def deposit(self, amount, description=""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.balance - amount < 0:
            return False
        else:
            self.transaction = {"amount": -amount, "description": description}
            self.ledger.append(self.transaction)
            self.balance -= amount
            self.cash_out += amount
            return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, "*")
        total = format(self.balance, '.2f')
        items = ""
        for i in self.ledger:
            description = i['description'][0:23]
            amount = format(i['amount'], '.2f')
            items += f"{description.ljust(23)}{amount.rjust(7)}\n"
        budget = f"{title}\n{items}Total: {total}"
        return budget


def create_spend_chart(categories):
    withdraw = []
    total_withdraw = 0
    percentages = []
    names = []

    for c in categories:
        withdraw_category = c.cash_out
        withdraw.append(float(withdraw_category))
        total_withdraw += float(withdraw_category)
        names.append(c.name)

    for w in withdraw:
        percentage_withdraw = 100 * float(str(w / total_withdraw)[0:3])
        percentages.append(int(percentage_withdraw))

    count = 100
    matrix = "Percentage spent by category\n"
    dash = 3 * len(percentages)
    line = "    -" + (dash * "-")

    while count >= 0:

        if count == 100:
            rows = "100| "
        elif count == 0:
            rows = "  0| "
        else:
            rows = " " + str(count) + "| "
        matrix += rows

        for p in percentages:
            if p >= count:
                matrix += "o  "
            else:
                matrix += "   "
        matrix += "\n"
        count -= 10

    matrix += line

    len_max = len(max(names, key=len))
    categories_equal = []
    for n in names:
        if len(n) < len_max:
            names_equal = (len_max - len(n)) * " "
            categories_equal.append(str(n) + names_equal)
        else:
            categories_equal.append(str(n))

    count = 0
    while count < len_max:
        matrix += "\n     "
        for c in categories_equal:
            matrix += c[count] + "  "
        count += 1

    return matrix
