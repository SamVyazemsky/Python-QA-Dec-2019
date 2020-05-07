*** Settings ***
Documentation    Suite description
Resource  oc-keywords.robot
Library  SeleniumLibrary

*** Test Cases ***
Тест админки
    Открытие админки опенкарт
    Close Browser