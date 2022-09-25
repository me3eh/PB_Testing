Feature: testing another site
  Scenario: lmao
    Given visiting url https://only-testing-blog.blogspot.com/2014/01/textbox.html
    Then element with id hidden1 should not be visible
    Then input with name To Hide should be visible