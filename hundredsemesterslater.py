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
    return nqueensaccu(n, [])


def avcols(n: int, placed: List[int]) -> List[int]:
    """
    Computes the possible cols for the next row.
    :param placed: the positions of the placed queens, beginning at row 0.
    :param n: the n in the n-queens
    :return: the number of possible queen placements with the given initial placement.
    """
    return filter(lambda i: not(i in placed or  # straight
                            i in [p + (len(placed)-idx) for idx,p in enumerate(placed)] or  # diagonal
                            i in [p - (len(placed)-idx) for idx,p in enumerate(placed)]),  # diagonal
                  range(n))


def nqueensaccu(n: int, placed: List[int]) -> int:
    """
    The recursive function to solve the nqueens problem.
    :param placed: the positions of the placed queens, beginning at row 0.
    :param n: the n in the n-queens
    :return: the number of possible queen placements with the given initial placement.
    """
    # Found a compintation. Juhay!
    if len(placed) == n:
        return 1
    return sum(nqueensaccu(n,placed+[av]) for av in avcols(n,placed))
