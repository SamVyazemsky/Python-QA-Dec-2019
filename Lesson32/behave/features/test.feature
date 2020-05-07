Feature: Checking search
Scenario: Сheck some text in search results

  Given website "https://ya.ru"
  When push button with text 'Найти'
  Then page include text 'Задан пустой поисковый запрос'