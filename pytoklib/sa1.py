"""A-Group and N-Token implementation for the Standard-Algorithm 1."""

import math

def agroup(values):
    v = []

    for vi in values:
        v.append([{vi}, list(vi.encode("utf-8"))])

    return v
