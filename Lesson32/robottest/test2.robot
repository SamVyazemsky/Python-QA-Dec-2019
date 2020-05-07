*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}          https://demo23.opencart.pro/admin
# ${BROWSER}      Chrome

*** Keywords ***
The user can open AdminPanel
    [Arguments]      ${BROWSER1}
    Open browser    ${URL}   ${BROWSER1}
    Input Text      id:input-username     demo
    Input Text      id:input-password     demo
    Click Button    css:button[type='submit']
    Title Should Be  Панель состояния
    Close Browser


*** Test Cases ***
The user can open AdminPanel by Chrome
        The user can open AdminPanel  Chrome
The user can open AdminPanel by Firefox
       The user can open AdminPanel  Firefox

