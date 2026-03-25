"""A-Group and N-Token implementation for the Standard-Algorithm 1."""

import math

ENCODING_AGROUP = "UTF-8"

def agroup(lst, lim):
    if (len(lst) == 0):
        return []
    
    v = []

    for vi in range(lim):
        v.append([[str(lst[vi])], ENCODING_AGROUP])

    return v


