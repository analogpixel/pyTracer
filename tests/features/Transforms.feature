Feature: Transforms
  Scenario: Multiply by a translation matrix
    Given transform = translation(5,-3,2)
    And   p = point(-3,4,5)
    Then  transform * p = point(2,1,7)
  Scenario: Multiply by the inverse of a translation matrix
    Given transform = translation(5,-3,2)
    And inv = inverse(transform)
    And p = point(-3,4,5)
    Then inv * p = point(-8,7,3)
  Scenario: Translation does not affect vectors
    Given transform = translation(5,-3,2)
    And   v = vector(-3,4,5)
    Then transform * v = v
  Scenario: A scaling matrix applied to a point
    Given t2 = scaling(2,3,4)
    And   p2 = point(-4,6,8)
    Then  t2 * p2 = point(-8,18,32)
  Scenario: A scaling matrix applied to a vector
    Given t2 = scaling(2,3,4)
    And v2 = vector(-4,6,8)
    Then t2 * v2 = vector(-8,18,32)
  Scenario: Multiplying by the inverse of a scaling matrix
    Given t2 = scaling(2,3,4)
    And  inv2  = inverse(t2)
    And v2 = vector(-4,6,8)
    Then inv2 * v2 = vector(-2,2,2)
  Scenario: Reflection is scaling by a negative value
    Given t3 = scaling(-1,1,1)
    And p3 = point(2,3,4)
    Then t3 * p3 = point(-2,3,4)
  Scenario: Rotating a point around the x axis
    Given p4 = point(0,1,0)
    And half_quarter = rotation_x( pi / 4)
    And full quarter = rotation_x( pi /2)
    Then half_quarter * p4 = point (0, sqrt(2)/2, sqrt(2)/2)
    and full_quarter * p4 = point(0,0,1)
  Scenario: Rotating a point around the y axis
    Given p5 = point(0,0,1)
      And half_quarter_y = rotation_y( pi / 4)
      And full_quarter_y = rotation_y( pi /2)
    Then half_quarter * p = point(sqrt(2)/2, 0, sqrt(2)/2)
      And full_quarter * p = point(1,0,0)
  Scenario: Rotating a point around the z axis
    Given p6 = point(0,1,0)
    And half_quarter_z = rotation_z(pi/4)
    And full_quarter_z = rotation_z(pi /2)
    Then half_quarter_z * p6 = point(-sqrt(2)/2, sqrt(2)/2, 0)
    And full_quarter * p = point(-1,0,0)

  Scenario: A shearing transformation moves x in proportion to y
    Given transform_s1 ← shearing(1, 0, 0, 0, 0, 0)
      And p7 ← point(2, 3, 4)
    Then transform_s1 * p7 = point(5, 3, 4)

  Scenario: A shearing transformation moves x in proportion to z
    Given transform_s2 ← shearing(0, 1, 0, 0, 0, 0)
      And p7 ← point(2, 3, 4)
    Then transform_s2 * p7 = point(6, 3, 4)

  Scenario: A shearing transformation moves y in proportion to x
    Given transform_s3 ← shearing(0, 0, 1, 0, 0, 0)
      And p7 ← point(2, 3, 4)
    Then transform_s3 * p7 = point(2, 5, 4)

  Scenario: A shearing transformation moves y in proportion to z
    Given transform_s4 ← shearing(0, 0, 0, 1, 0, 0)
      And p7 ← point(2, 3, 4)
    Then transform_s4 * p7 = point(2, 7, 4)

  Scenario: A shearing transformation moves z in proportion to x
    Given transform_s5 ← shearing(0, 0, 0, 0, 1, 0)
      And p7 ← point(2, 3, 4)
    Then transform_s5 * p7 = point(2, 3, 6)

  Scenario: A shearing transformation moves z in proportion to y
    Given transform_s6 ← shearing(0, 0, 0, 0, 0, 1)
      And p7 ← point(2, 3, 4)
    Then transform_s6 * p7 = point(2, 3, 7)
