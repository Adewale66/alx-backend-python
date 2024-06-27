#!/usr/bin/env python3
"""
sum_mixed_list module
"""

import typing


def sum_mixed_list(mxd_lst: typing.Union[int, float]) -> float:
    """sums all values in a mixed list

    Args:
        mxd_lst (typing.Union[int, float]): list of ints and floats

    Returns:
        float: sum of all vlaues
    """
    return sum(mxd_lst)
