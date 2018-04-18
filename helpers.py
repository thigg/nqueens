import math
from typing import Tuple


def rotate(n, pos: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    rotates the given combination by 90 degree to the right
    :param n: fieldsize
    :param pos: the combination to rotate
    :return: the rotated combination
    """
    ret = list(pos[:])
    c = (n - 1) / 2  # center of the board
    r = -math.pi / 2  # 90 deg
    cosx = math.cos(r)
    sinx = math.sin(r)
    for idx, p in enumerate(pos):
        # naive apporach to rotation, shouldnt be a too large performance bottleneck.
        x = c + (p - c) * cosx - (idx - c) * sinx
        y = c + (p - c) * sinx + (idx - c) * cosx
        ret[round(y)] = round(x)
    return tuple(ret)


def mirror(n, pos: Tuple[int, ...]) -> Tuple[int, ...]:
    """
    mirrors the given combination vertically
    :param n: fieldsize
    :param pos: the combination to mirror
    :return: the vertically mirrored combination
    """
    return tuple(map(lambda i: (n - 1) - i, pos))
