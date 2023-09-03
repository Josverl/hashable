"""Validate that a type is hashable.
ref: https://github.com/Josverl/micropython-stubs/issues/723
"""

i = 0
d = {i: "a"}


x = {1: "a", 2: "b"}

y = {"foo": "bar"}