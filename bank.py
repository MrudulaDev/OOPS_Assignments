from manager import Manager
from user import User


class Bank:
    banks_list = []
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.bank_id = id(self)
        self.user_accounts = []
        self.manager_accounts = []
        type(self).banks_list.append(self)

    def creating_manager_account(self, bank_id, manager_account_name, manager_account_password):
        manager_account = Manager(manager_account_name, manager_account_password, bank_id)
        self.manager_accounts.append(manager_account)
        return manager_account

    def creating_user_account(self, user_account_number, user_password, bank_id, manager_id):
        user_account = User(user_account_number, user_password, bank_id, manager_id)
        self.user_accounts.append(user_account)
        return user_account


if __name__ == "__main__":
    bank = Bank("SBI")
    manager_obj = bank.creating_manager_account("Manager_1", "Manager_1@1234", bank.bank_id)
    manager_id = manager_obj.manager_id
    user_obj = bank.creating_user_account("SBI1234567", "SBI1234567", bank.bank_id, manager_id)
    user_obj.add_beneficiary("Ramu", "SBI7654321")
    print(user_obj.beneficiary_list)
    print(user_obj.manager_id)
    print(user_obj.balance)
    user_obj.make_credit_transaction("ICICI12345", 50000)
    print(user_obj.balance)
    user_obj.display_transaction_history()
    user_obj.make_debit_transaction(15000, "SBI7654321")
    print(user_obj.balance)
    user_obj.display_transaction_history("debit")
    user_obj.display_transaction_history("credit")
