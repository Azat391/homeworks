import pytest,playwright
from playwright.sync_api import Page, expect
def test_home_page(home_page):
    expect(home_page.bank_manager_login_button).to_be_visible()
def test_login_as(account_page):
    expect(account_page().logout_button).to_be_visible()
def test_logout(account_page):
    customer_login_page=account_page().logout()
    expect(customer_login_page.change_customer_button).to_be_visible()
def test_deposit(account_page):
    customer_page=account_page()
    customer_page.deposit(50)
    expect(customer_page.deposit_succesfull).to_be_visible()
def test_transaction(account_page):
    transeaction_page=account_page().open_transactions()
    expect(transeaction_page.back_button).to_be_visible()
@pytest.mark.parametrize('name', ['Harry Potter', 'Hermoine Granger'])
def test_login_as_double_customer(account_page, name):
    expect(account_page(name=name).logout_button).to_be_visible()