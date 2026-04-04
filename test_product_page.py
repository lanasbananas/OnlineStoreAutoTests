import pytest
from .pages.product_page import ProductPage

LINKS = ["http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"]

def generate_links():
    LINKS = []
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    for num in range(0, 10):
        if num == 7:
            LINKS.append(pytest.param(link+str(num), marks=pytest.mark.xfail))
        else:
            LINKS.append(link+str(num))
    return LINKS

@pytest.mark.parametrize("link", generate_links())
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_about_add_to_basket()
    page.should_be_correct_amount()

