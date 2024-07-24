Feature: Register A New User

Scenario: Add a valid new user
    Given I am using "Chrome"
    When I navigate to the demoblaze home page
    And I click on "Sign up" in the header
    And I fill out the sign-up form with a non-existant, valid username and password
    And I click on the "Sign up" button in the sign-up form
    Then I should see the successful user registration dialog


