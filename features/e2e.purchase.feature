Feature: Purchase products

  Scenario Outline: Purchase two random products
    Given I am using <browser>
    When I navigate to the demoblaze home page
    And I add two random products to the cart
    And I visualize the cart
    And I the place order with the following data
      | Field   | Value     |
      | Name    | John Doe  |
      | Country | USA       |
      | City    | New York  |
      | Card    | 1234 5678 |
      | Month   | 12        |
      | Year    | 2024      |
    Then I should see the successful purchase screen

    Examples:
      | browser  |
      | Chrome   |