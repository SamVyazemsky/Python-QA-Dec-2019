*** Settings ***
Documentation    Suite description
Library  RequestsLibrary

*** Variables ***
${BaseUrl}  https://petstore.swagger.io/v2/pet

*** Test Cases ***
Тест нахождения неизвестного животного
    create session  GetHeaders  ${BaseUrl}
    ${response} =  get request  GetHeaders   1/
    log to console  ${response.status_code}
    log to console  ${response.content}
    Should Be Equal As Strings	${response.status_code}	404

Открыть сайт  "yandex.ru"
Открыть сайт  "google.com"


*** Keywords ***
Открыть сайт  ${url}
    Open Browser  $url