from .pages.login_page import LoginPage


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.login_to_account()

    browser.save_screenshot('screen1.png')
