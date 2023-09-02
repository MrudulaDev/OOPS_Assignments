class User:
    account_max_balance = 1000000
    transaction_max_limit = 100000

    def __init__(self, user_account_number, user_password, bank_id, manager_id):
        self.user_account_number = user_account_number
        self.user_password = user_password
        self.bank_id = bank_id
        self.manager_id = manager_id
        self.user_id = id(self)
        self.balance = 0
        self.beneficiary_list = []
        self.transaction_history = []
        self.username = ""
        self.mobile_number = 0
        self.address = ""

    def create_user_profile(self, username, mobile_number, address, user_password):
        self.username = username
        self.mobile_number = mobile_number
        self.address = address
        self.user_password = user_password

    def add_beneficiary(self, beneficiary_account_number):
        if beneficiary_account_number in self.beneficiary_list:
            raise ValueError("This Beneficiary Already Exists")
        else:
            self.beneficiary_list.append(beneficiary_account_number)

    def delete_beneficiary(self, beneficiary_account_number):
        self.beneficiary_list.remove(beneficiary_account_number)

    def make_debit_transaction(self, amount, beneficiary_account_number):
        if amount > type(self).transaction_max_limit:
            raise ValueError("Transaction Limit Exceeded")
        elif beneficiary_account_number in self.beneficiary_list and self.balance >= amount:
            self.balance -= amount
            debit_transaction_details = ("debit", beneficiary_account_number, amount)
            self.transaction_history.append(debit_transaction_details)
        elif beneficiary_account_number in self.beneficiary_list and self.balance < amount:
            raise ValueError("Insufficient Funds!")
        else:
            raise ValueError("Add Beneficiary to make transaction")

    def make_credit_transaction(self, account_number, amount):
        if self.balance + amount > type(self).account_max_balance:
            raise ValueError("Account Max Limit exceeded! Amount cannot be credited")
        else:
            self.balance += amount
            credit_transaction_details = ("credit", account_number, amount)
            self.transaction_history.append(credit_transaction_details)

    def display_balance(self):
        print(self.balance)

    def display_transaction_history(self, transaction_type_filter=""):
        if transaction_type_filter == "":
            list(map(self.printing_items, self.transaction_history))
        elif transaction_type_filter == "debit":
            filtered_list = list(filter(lambda transaction: transaction[0] == "debit", self.transaction_history))
            list(map(self.printing_items, filtered_list))
        elif transaction_type_filter == "credit":
            filtered_list = list(filter(lambda transaction: transaction[0] == "credit", self.transaction_history))
            list(map(self.printing_items, filtered_list))
    @staticmethod
    def printing_items(item):
        print(item)
