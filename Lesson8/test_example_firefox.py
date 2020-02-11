import pytest
from selenium import webdriver


def test_example(firefox_browser):
    """
    Example with ChromeOptions
    """
    firefox_browser.get("https://otus.ru/")