
class Bank:
    def __init__(self, capacity=1000):
        self._capacity = capacity

    def deposit(self, n):
        self._capacity += n

    def withdraw(self, n):
        if self._capacity < n:
            raise ValueError('There is not enough money in the account to withdraw')
        self._capacity -= n

    @property
    def capacity(self):
        return self._capacity

    def __str__(self):
        return f"Your actual deposit is {self.capacity}"



#To prove it works:

#bank = Bank()
#bank.deposit(0)
#bank.withdraw(2000)
#print(bank)
