Feature: build Garage


  @garage
  Scenario: create garage
    Given create garage as "garage"
    Given create car with name "skoda"
    When i put car "skoda" in garage "garage"
    Then assert that car "skoda" in garage "garage"