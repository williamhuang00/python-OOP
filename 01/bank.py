class BankAccount:

    def __init__(self, id: int, name: str, amount: float=0.0) -> None:
        self.id = id
        self.name = name
        self.amount = amount
    
    def print_balance(self, comment: str | None = None) -> None:
        if comment:
            print(f"Balance {self.amount} - {comment}")
        else:
            print(f"Balance {self.amount}")
        

    def __str__(self):
        return f"{self.id}, {self.name}, {self.amount}"


if __name__ == "__main__":
    wills_bank = BankAccount(0, 'will', 200.0)
    jackys_bank = BankAccount(1, 'jacky', 50.0)

    print(wills_bank)
    print(jackys_bank)

    wills_bank.print_balance()
    wills_bank.print_balance('this is a lot of money i reckon')