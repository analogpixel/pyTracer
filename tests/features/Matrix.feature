Feature: Matrix
  Scenario: Construction and inspecting a 4x4 matrix
    Given the following 4x4 matrix M:
      |  1  |  2  |  3  |  4  |
      |  5.5| 6.5 | 7.5 | 8.5 |
      | 9   | 10  | 11  | 12  |
      | 13.5| 14.5| 15.5| 16.5|
    Then M[0,0] = 1
     And M[0,3] = 4
     And M[1,0] = 5.5
     And M[1,2] = 7.5
     And M[2,2] = 11
     And M[3,0] = 13.5
     And M[3,2] = 15.5
  Scenario: Matrix equality with identical matrices
    Given the following 4x4 matrix A:
      |  1  |  2  |  3  |  4  |
      |  5.5| 6.5 | 7.5 | 8.5 |
      | 9   | 10  | 11  | 12  |
      | 13.5| 14.5| 15.5| 16.5|
    And the following 4x4 matrix B:
      |  1  |  2  |  3  |  4  |
      |  5.5| 6.5 | 7.5 | 8.5 |
      | 9   | 10  | 11  | 12  |
      | 13.5| 14.5| 15.5| 16.5|
    Then A = B

  Scenario: Matrix equality with different matrices
    Given the following 4x4 matrix A:
      |  1  |  2  |  3  |  4  |
      |  5.5| 6.5 | 7.5 | 8.5 |
      | 9   | 10  | 11  | 12  |
      | 13.5| 14.5| 15.5| 16.5|
    And the following 4x4 matrix C:
      |  1  |  2  |  3  |  0  |
      |  5.5| 6.5 | 7.5 | 8.5 |
      | 9   | 10  | 11  | 12  |
      | 13.5| 14.5| 15.5| 16.5|
    Then A != C

  Scenario: Multiplying two matrices
    Given the following matrix D:
        | 1 | 2 | 3 | 4 |
        | 5 | 6 | 7 | 8 |
        | 9 | 8 | 7 | 6 |
        | 5 | 4 | 3 | 2 |
      And the following matrix E:
        | -2 | 1 | 2 |  3 |
        |  3 | 2 | 1 | -1 |
        |  4 | 3 | 6 |  5 |
        |  1 | 2 | 7 |  8 |
    Then D * E is the following 4x4 matrix:
        | 20|  22 |  50 |  48 |
        | 44|  54 | 114 | 108 |
        | 40|  58 | 110 | 102 |
        | 16|  26 |  46 |  42 |

  Scenario: A matrix multiplied by a tuple
  Given the following matrix F:
      | 1 | 2 | 3 | 4 |
      | 2 | 4 | 4 | 2 |
      | 8 | 6 | 4 | 1 |
      | 0 | 0 | 0 | 1 |
    And b ← Tuple(1, 2, 3, 1)
    Then F * b = Tuple(18, 24, 33, 1)

  Scenario: Multiplying a matrix by the identity matrix
    Given the following matrix G:
      | 0 | 1 |  2 |  4 |
      | 1 | 2 |  4 |  8 |
      | 2 | 4 |  8 | 16 |
      | 4 | 8 | 16 | 32 |
    Then G * identity_matrix = G

  Scenario: Multiplying the identity matrix by a tuple
    Given tg ← Tuple(1, 2, 3, 4)
    Then identity_matrix * tg = tg

  Scenario: Transposing a matrix
    Given the following matrix H:
      | 0 | 9 | 3 | 0 |
      | 9 | 8 | 0 | 8 |
      | 1 | 8 | 5 | 3 |
      | 0 | 0 | 5 | 8 |
    Then transpose(H) is the following matrix:
      | 0 | 9 | 1 | 0 |
      | 9 | 8 | 8 | 0 |
      | 3 | 0 | 5 | 5 |
      | 0 | 8 | 3 | 8 |

  Scenario: Transposing the identity matrix
    Given I ← transpose(identity_matrix)
    Then I = identity_matrix

