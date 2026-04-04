import pytest
from .pages.product_page import ProductPage

LINKS = ["http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"]

def generate_links():
    links = []
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    for num in range(0, 10):
        if num == 7:
            links.append(pytest.param(link+str(num), marks=pytest.mark.xfail))
        else:
            links.append(link+str(num))
    return links

@pytest.mark.skip
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


