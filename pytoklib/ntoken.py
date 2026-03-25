"""A-Group and N-Token implementation."""

def ntoken(lst, alg):
    if (len(lst) == 0):
        return []
    
    return alg.agroup(lst, len(lst))