Feature: testing google
  Scenario: visit google and check
    Given site gram.pl
    When we press button with text ZGADZAM SIĘ
    Then it should have a title "Google"