Feature: testing common steps on normal behaviour
  Scenario: testing filling inputs with text, submit clicking, checking title and css finding and matching text inside
    Given visiting url youshstg.myshopify.com
    Given filling input with id password text lailtu
    Given clicking submit button
    Then it should have a title Staging – youshstg
    Then element with css classes explore__header should have text POZNAJ NASZE PRODUKTY

  Scenario: finding element by various css elements splitted by dots
    Given visiting url youshstg.myshopify.com
    When clicking on element with css class explore__product-card.explore__header-image
    Then it should have a title Yoush – youshstg

  Scenario: finding element by various css elements splitted by spaces
    Given visiting url youshstg.myshopify.com
    When clicking on element with css class explore__product-card explore__header-image
    Then it should have a title Yoush – youshstg

  Scenario: clicking on link text
    Given visiting url youshstg.myshopify.com
    When clicking on link with link text O nas
    Then it should have an url https://youshstg.myshopify.com/pages/privacy-policy
