from typing import List, Tuple, Set

from helpers import rotate, mirror


def nqueens(n: int) -> Tuple[int, int]:
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
    return nqueensaccu(n, [], [], [], set())


def nqueensaccu(n: int, placed: List[int], left: List[int], right: List[int], alreadyseen: Set) -> Tuple[int, int]:
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
    :param alreadyseen: a mutable set which stores all solutions we saw already
    :return: a tuple with the number of all and all unique solutions
    """

    def updateSet(placed: Tuple[int,...]) -> bool:
        """
        Updates the alreadyseen set with the given combination
        simple approach now, keeping space for other datastructures
        :param placed: the list of queen positions
        :return if the combination is already known
        """
        if placed in alreadyseen:
            return False
        alreadyseen.add(placed)
        return True

    # Found a combintation. Juhay!
    if len(placed) == n:
        # We can ignore all mutations if one of them is already known.
        if tuple(placed) not in alreadyseen:
            mutations = getMutations(n, tuple(placed))
            for a in mutations:
                updateSet(a)
            # return the number of combinations and a new uniqe combination if it is one.
            # A combination is unique, when there is no mutation of this combination already found.
            return (len(mutations), 1)
        return (0, 0)

    # move diagonal blocklists. Maybe we should use a binary shift operation here...
    left = list(map(lambda i: i - 1, left))
    right = list(map(lambda i: i + 1, right))

    # fields which are not already threatened by an other queen.
    unblocked = filter(lambda i: i not in placed and i not in left and i not in right,  # diagonal
                       range(n))
    results = [nqueensaccu(n, placed + [av], left + [av], right + [av], alreadyseen) for av in unblocked]
    results.append((0, 0))
    return tuple(sum(x) for x in zip(*results)) # sum the returned tuples element-wise


def getMutations(n: int, placed: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    """
    Simple approach to identify all mutations of a combination
    :return: all mutations of the current placement by rotation and mirroring.
    """
    ret: Set[Tuple[int,...]] = set()  # make sure we take every element only once.
    ret.add(placed)
    ret.add(mirror(n, placed))
    # rotate 3 times and mirror always
    last = placed
    for i in range(3):
        last = rotate(n, last)
        ret.add(last)
        ret.add(mirror(n, last))
    return list(ret)
