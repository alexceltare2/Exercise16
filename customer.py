class Account:
    numCreated = 0
    totalDeposits = 0

    def __init__(self, initial):
        self._balance = initial
        Account.numCreated += 1
        Account.totalDeposits += initial

    def deposit(self, amt):
        self._balance += amt
        Account.totalDeposits += amt

    def withdraw(self,amt):
        self._balance -= amt
        Account.totalDeposits -= amt

    def getbalance(self):
        return self._balance

    def add_interest(self, interest):
        pass

    def __str__(self):
        return f"This account's balance: £{self.getbalance()}"

    def __gt__(self, other):
        return self._balance > other.getbalance()

    def __lt__(self, other):
        return self._balance < other.getbalance()

    def __eq__(self, other):
        return self._balance == other.getbalance()

    @classmethod
    def get_total_balance(cls):
        return f"The Bank of Eoghan has reserves of:  ${cls.totalDeposits}"