from typing import List


def nqueens(n: int) -> int:
    """
    Computes the solution for the n-queens problem:
    Place n queens on a nxn grid without any two queens threatening each other. Standard chess rules apply.
    A queen must not be placed in the same row, column or diagonally to any other queen.

    The problem is solved with backtracking:
    Starting with the first row, on each position a queen is placed.
    Given that one placed queen, the now remaining available positions are used to place the next queen and so on.
    :param n: The size of the chess grid and the number of queens that are to be placed. Must be a positive integer.
    :raise ValueError: when an integer was passed that is not larger than 0.
    :return: The number of possible combinations where no two queens are threatening each other.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("nqueens can only be solved for positive, non-zero integers.")
    return nqueensaccu(n, [], [], [])


def nqueensaccu(n: int, placed: List[int], left: List[int], right: List[int]) -> int:
    """
    The recursive function to solve the nqueens problem.

    Concept:
    Find all possible fields where a queen can be placed, place one on each separatley and call recursivley.
    Queens block straight and diagonally.
    For straight, we have to consider only one direction, because we iterate over the other.
    Diagonally is handeled by the two lists left and right, which have a marker for each diagonal line in the last row,
    which is moved into the correct direction then to figure out which field is blocked.

    :param placed: the positions of the placed queens, beginning at row 0.
    :param n: the n in the n-queens
    :param left: diagonally blocking to the left in the last row
    :param right: diagonally blocking to the right in the last row
    :return: the number of possible queen placements with the given initial placement.
    """
    # Found a compintation. Juhay!
    if len(placed) == n:
        return 1
    left = list(map(lambda i: i - 1, left))
    right = list(map(lambda i: i + 1, right))
    return sum(nqueensaccu(n, placed + [av], left + [av], right + [av]) for av in
               filter(lambda i: i not in placed and i not in left and i not in right,  # diagonal
                      range(n)))
