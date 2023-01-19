Feature: checking working of maintenance mode
  Scenario: trying to activate maintenance mode
    When logging in with username and password for admin
    When entering admin panel and trying to activate maintenance mode
    Then maintenance mode will be on, based on displaying text
  Scenario: trying to deactivate maintenance mode
    When entering admin panel and trying to activate maintenance mode
    Then maintenance mode will be off, based on displaying text