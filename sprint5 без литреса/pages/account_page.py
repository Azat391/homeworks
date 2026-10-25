class TransactionsPage:
    def __init__(self,page):
        self.page=page
        self.back_button=page.get_by_role('button', name='Back', exact=True)
class AccountPage:
    def __init__(self, page):
        self.page=page
        self.transactions_button=page.get_by_role('button', name='Transactions', exact=True)
        self.deposit_button=page.get_by_role('button', name='Deposit', exact=True)
        self.logout_button=page.get_by_role('button', name='Logout', exact=True)
        self.amount=page.get_by_placeholder('amount')
        self.deposit_succesfull=page.get_by_text('Deposit Successful')
    def logout(self):
        self.logout_button.click()
        from pages.customer_login_page import CustomerLoginPage
        return CustomerLoginPage(self.page)
    def deposit(self,amount):
        self.deposit_button.click()
        self.amount.fill(str(amount))
        self.amount.press('Enter')
    def open_transactions(self):
        self.transactions_button.click()
        return TransactionsPage(self.page)



