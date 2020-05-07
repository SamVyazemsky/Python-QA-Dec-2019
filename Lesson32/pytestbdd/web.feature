@web @duckduckgo
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then results are shown for "panda"