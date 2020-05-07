*** Settings ***
Documentation    Suite description
Library      opencart_keywords.py
Library  SeleniumLibrary

*** Test Cases ***
Test title
    [Tags]    Google    Тест    Отус    PythonQA
    Open Google
    Закрыть браузер

*** Keywords ***
Закрыть браузер
    Close browser