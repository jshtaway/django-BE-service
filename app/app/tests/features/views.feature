Feature: Views

    Scenario: Greetings
        When I go to "/greetings"
        Then I get "Hello" in response