Feature: Triangle Classifier Application

  Scenario: Classify Equilateral Triangle
    Given the input is "1 1 1"
    When the program processes the input
    Then the output should be "Equilateral"

  Scenario: Classify Isosceles Triangle
    Given the input is "2 2 3"
    When the program processes the input
    Then the output should be "Isosceles"

  Scenario: Handle Missing Inputs
    Given the input is "1"
    When the program processes the input
    Then the output should be "Error: Two sides missing"

  Scenario: Quit Application
    Given the input is "Quit"
    When the program processes the input
    Then the application should exit
