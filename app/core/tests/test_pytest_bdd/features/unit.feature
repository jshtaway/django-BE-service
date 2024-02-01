Feature: Tests

  Scenario: Test django management commands
    When I wait for db ready

  Scenario: Inject db not ready errors
    When I wait for db delay
    Then Django starts after waiting
  
  Scenario: Test models
    