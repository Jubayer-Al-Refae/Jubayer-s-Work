class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.al = account_holder
        self.b = balance
        self.pin = pin
        self.attempts = 0
        self.status = "Active"

    def verify_pin(self, entered_pin):
        if self.status != "Active":
            print("Account is blocked")
            return False

        if entered_pin == self.pin:
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            print(f"Wrong PIN! Attempt {self.attempts}/3")

            if self.attempts >= 3:
                self.status = "Blocked"
                print("Account blocked due to 3 wrong PIN attempts")
            return False

    def withdraw(self, amount):
        if self.status != "Active":
            print("Cannot withdraw. Account blocked.")
            return 0

        # Loop for PIN attempts
        while self.attempts < 3:
            entered_pin = int(input("Enter your PIN for withdrawal: "))
            if self.verify_pin(entered_pin):
                break
        else:
            return 0  # account blocked

        before_balance = self.b
        if amount > self.b:
            print("Insufficient balance")
            return 0
        self.b -= amount
        print(f"Withdraw: {amount}")
        print(f"Balance before transaction: {before_balance}")
        print(f"Balance after transaction: {self.b}")
        return amount

    def deposit(self, amount):
        if self.status != "Active":
            print("Cannot deposit. Account blocked.")
            return 0

        # Loop for PIN attempts
        while self.attempts < 3:
            entered_pin = int(input("Enter your PIN for deposit: "))
            if self.verify_pin(entered_pin):
                break
        else:
            return 0  # account blocked

        before_balance = self.b
        self.b += amount
        print(f"Deposit: {amount}")
        print(f"Balance before transaction: {before_balance}")
        print(f"Balance after transaction: {self.b}")
        return amount

    def display_balance(self):
        print(f"{self.al}'s current balance: {self.b}")


# User input
name = input("Enter account holder name: ")
balance = int(input("Enter starting balance: "))
pin = int(input("Set a 4-digit PIN: "))
acc = BankAccount(name, balance, pin)

# Ask for action
action = input("Do you want to Withdraw or Deposit? (W/D): ").strip().upper()

if action == "W":
    amount = int(input("Enter amount to withdraw: "))
    acc.withdraw(amount)
elif action == "D":
    amount = int(input("Enter amount to deposit: "))
    acc.deposit(amount)
else:
    print("Invalid action selected!")
acc.display_balance()

