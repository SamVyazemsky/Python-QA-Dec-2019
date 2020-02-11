from selenium import webdriver


def test_example():
    """
    First test
    """
    wd = webdriver.Firefox()
    wd.get("https://otus.ru/")
    assert wd.title == 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    wd.quit()
