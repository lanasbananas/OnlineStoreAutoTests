import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .test_data.generators import UserData

LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]


def generate_links():
    links = []
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    for num in range(0, 10):
        if num == 7:
            links.append(pytest.param(link+str(num), marks=pytest.mark.xfail))
        else:
            links.append(link+str(num))
    return links

@pytest.mark.need_review
@pytest.mark.parametrize("link", generate_links())
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_about_add_to_basket()
    page.should_be_correct_amount()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = LINKS[0]
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = LINKS[0]
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = LINKS[0]
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = LINKS[0]
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LINKS[0]
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        user = UserData.create_random()
        login_page.register_new_user(user.email, user.password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = LINKS[0]
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = LINKS[0]
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_message_about_add_to_basket()
        page.should_be_correct_amount()

