Feature: Spheres
  Scenario: A ray intersects a sphere at two points
    Given r <- ray( point(0,0,-5), vector(0,0,1) )
    And   s <- sphere()
    When xs <- intersect(s,r)
    Then xs.count = 2
    And  xs[0] = 4.0
    And  xs[1] = 6.0
  Scenario: A ray intersects a sphere at a tanget
    Given r2 <- ray( point(0,1,-5), vector(0,0,1))
    And s2 <- sphere()
    When  xs2 = intersect(s2,r2)
    Then xs2.count = 2
    And xs2[0] = 5.0
    And xs2[1] = 5.0
  Scenario: A ray misses a sphere
    Given r3 <- ray( point(0,2,-5), vector(0,0,1))
    And   s3 = sphere()
    When  xs3 = intersect(s3,r3)
    Then  xs3.count = 0
  Scenario: a ray originates inside a sphere
    Given r4 <- ray(point(0,0,0), vector(0,0,1))
    And s4 = sphere()
    When xs4 <- intersect(s4,r4)
    Then xs4.count = 2
    And xs4[0] = -1.0
    And xs4[1] = 1.0
  Scenario: a sphere is behind a ray
    Given r5 <- ray( point(0,0,5), vector(0,0,1) )
    And s5 <- sphere()
    When xs5 <- intersect(s5,r5)
    Then xs5.count = 2
     And xs5[0] = -6.0
     and xs5[1] = -4.0
  Scenario: an intersection encapsulates t and object
    Given s6 <- sphere()
    When i6 = intersection(3.5, s)
    Then i6.t = 3.5
    And i6.obj = s6
  Scenario: A sphere's default transformation
    Given s7 <- sphere()
    Then s7.transform = identity_matrix
  Scenario: Changing a sphere's transformation
    Given s8 <- sphere()
    And   t8 <- translation(2,3,4)
    When  s8.applyTransform(t8)
    Then  s8.transform = t8
  Scenario: Intersection a scaled sphere with a ray
    Given r10 <- ray( (point(0,0,-5), vector(0,0,1) )
    And   s10 <- sphere()
    When S10.applyTransform( scaling(2,2,2))
    And  xs10 <- S10.intersect(r10)
    Then len(xs10) = 2
    And xs10[0].t = 3
    And xs10[1].t = 7
  Scenario: Intersection a translated sphere with a ray
    Given r11 <- ray( point(0,0,-5), vector(0,0,1))
    And   s11 <- sphere()
    When  s11.applyTransform( translation(5,0,0))
    And  xs11 <- s11.intersect(r11)
    Then len(xs11) == 0
