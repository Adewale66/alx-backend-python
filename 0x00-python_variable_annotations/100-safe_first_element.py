#!/usr/bin/env python3
"""
duck typing
"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[None, typing.Any]:
    if lst:
        return lst[0]
    else:
        return None
