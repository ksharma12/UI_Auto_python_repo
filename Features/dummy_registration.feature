Feature: Dummy Registration


  @ChromeOnly
  Scenario Outline: Dummy Registration Form
    Given User navigated to url
    When Verify user successfully landed on home page
    Then User moved to resources option
    Then User clicked on resources option
    Then Verify landed on dummy registration page
    Then User fill "<name>" in dummy registration form
    Examples:
      | name |
    | Keshav     |
