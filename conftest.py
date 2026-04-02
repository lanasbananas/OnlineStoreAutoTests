import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

LANGUAGES = ["ru", "es", "en", "ar", "ca", "cs", "da", "de", "fr", "el", "fi", "it", "ko", "nl", "pl", "pt", "pt_br", "ro", "sk", "uk", "zh-hans"]


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", choices=("chrome", "firefox"),
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", choices=(*LANGUAGES,),
                     help=f"Choose language: {LANGUAGES}")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    browser = None
    if browser_language not in LANGUAGES:
        raise pytest.UsageError("--language is not correct")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name is not correct")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()
