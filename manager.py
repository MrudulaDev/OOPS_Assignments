class Manager:
    def __init__(self, manager_account_name, manager_account_password, bank_id):
        self.manager_account_name = manager_account_name
        self.manager_account_password = manager_account_password
        self.bank_id = bank_id
        self.manager_id = id(self)
