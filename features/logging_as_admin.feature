Feature: login as admin
  Scenario: with correct passes
    When logging in with username and password for admin
    Then user will be logged as admin and redirected to /admin