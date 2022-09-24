Feature: testing on basic_web_page
  Scenario: visiting some site and checking id
    Given visiting url https://testpages.herokuapp.com/basic_web_page.html
    Then element with id para1 should have text A paragraph of text

  Scenario: visiting some site and checking another id
    Given visiting url https://testpages.herokuapp.com/basic_web_page.html
    Then element with id para2 should have text Another paragraph of text