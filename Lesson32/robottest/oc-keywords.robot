*** Settings ***
Library  Selenium2Library

*** Keywords ***
Открытие админки опенкарт
    Open browser    https://demo23.opencart.pro/admin   Chrome
    Input Text      id:input-username     demo
    Input Text      id:input-password     demo
    Click Button    css:button[type='submit']
