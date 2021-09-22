Feature: Direction
  As a user
  I want to use a calculator to add numbers
  So that I don't need to add myself

  Scenario Outline: Direction of <num>
    Given I have a direction
    When I check <num>
    Then The result should be <result>
   
Examples: sums
    |    num   | result |
    |  0       |   N    |
    |  22.5    |   NNE  |
    |  45      |   NE   |
    |  67.5    |   ENE  |
    |  90      |   E    |
    |  112.5   |   ESE  |
    |  135.0   |   SE   |
    |  157.5   |   SSE  |
    |  180.0   |   S    |
    |  202.5   |   SSW  |
    |  225.0   |   SW   |
    |  247.5   |   WSW  |
    |  270.0   |   W    |
    |  292.5   |   WNW  |
    |  315.0   |   NW   |
    |  337.5   |   NNW  |