Feature: Rays
  Scenario: Creating and querying a ray
    Given origin = point(1,2,3)
    And direction = vector(4,5,6)
    When r = ray(origin,direction)
    Then r.origin = origin
    And r.direction = direction

  Scenario: Computing a point from a distance
    Given r2 <- ray( point(2,3,4), vector(1,0,0))
    Then position(r2,0) = point(2,3,4)
    And  position(r2,1) = point(3,3,4)
    And  position(r2,-1) = point(1,3,4)
    And  position(r2,2.5) = point(4.5,3,4)

  Scenario: Translating a ray
    Given  r3<- ray( point(1,2,3), vector(0,1,0) )
    And    m3<- translation(3,4,5)
    When   r4 <- transform(r3, m3)
    Then   r4.origin = point(4,6,8)
    And   r4.direction = vector( 0,1,0)

  Scenario: Scaling a ray
    Given r5 <- ray(point(1,2,3), vector(0,1,0))
    And   m4 <- scaling(2,3,4)
    When r6  <- r5.applyTransform(m4)
    Then r6.origin = point(2,6,12)
    And  r6.direction = vector(0,3,0)
