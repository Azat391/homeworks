from pages.account_page import AccountPage
class CustomerLoginPage:
    def __init__(self, page):
        self.page=page
        self.change_customer_button=page.locator("#userSelect")
        self.login_button=page.get_by_role('button', name='Login', exact=True)
    def login_as(self, cusstomer):
        self.change_customer_button.select_option(cusstomer)
        self.login_button.click()
        return AccountPage(self.page)
