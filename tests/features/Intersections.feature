Feature: Intersections
  Scenario: the hit, when all the intersections have positive t
    Given s1 <- sphere()
    And   i1 <- intersection(1,s1)
    And   i2 <- intersection(2,s1)
    And  xs1 <- intersections(i1, i2)
    When ih1 <- hit(xs1)
    Then ih1 = i1

  Scenario: the hit, when some intersections have negative t
    Given s4 <- sphere()
    And   i3 <- intersection(-1,s4)
    And   i4 <- intersection(1,s4)
    And  xs2 <- intersections(i3,i4)
    When ih2 <- hit(xs2)
    Then ih2 = i4

  Scenario: the hit, when all intersections have negative t
    Given s3 <- sphere()
    And   i5 <- intersection(-2, s3)
    And   i6 <- intersection(-1,s3)
    And  xs3 <- intersections(i5,i6)
    When i <- hit(xs3)
    Then i is nothing
