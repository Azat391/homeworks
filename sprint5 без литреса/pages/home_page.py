from pages.customer_login_page import CustomerLoginPage
class HomePage:
    def __init__(self, page):
        self.base_url='https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
        self.page=page
        self.customer_login_button=page.get_by_role('button', name='Customer Login', exact=True)
        self.bank_manager_login_button=page.get_by_role('button', name='Bank Manager Login', exact=True)
    def open(self):
        self.page.goto(self.base_url)
    def open_customer_login(self):
        self.customer_login_button.click()
        return CustomerLoginPage(self.page)
