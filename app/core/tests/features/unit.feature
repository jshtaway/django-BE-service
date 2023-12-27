Feature: Tests

  Scenario: Test django management commands
    When I wait for db ready
    Then Django starts without error