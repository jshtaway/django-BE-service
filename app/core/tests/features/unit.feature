Feature: Tests

  Scenario: Test django management commands
    When I wait for db ready
    Then Django starts without error

  Scenario: Test django DB delayed
    When I wait for db delay
    Then Test errors