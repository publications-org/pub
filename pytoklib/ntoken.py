"""A-Group and N-Token implementation."""

def ntoken(sequence, alg):
    res = alg.agroup(sequence)
    return res