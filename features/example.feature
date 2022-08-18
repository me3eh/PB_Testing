Feature: Valid login
  Scenario: Open Browser To Login Page
    Given visited page mysite.com/login
    When in input username demo
    And in input password mode
    And Submitted Credentials
    Then Welcome Page Should Be Open
  Scenario: