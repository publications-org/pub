"""Japanese from the CJK examples."""

import sys
sys.path.append('./')

import pytoklib

if __name__ == '__main__':
    with open('datasets/jp.txt') as f: 
        s = f.read()
        res = pytoklib.ntoken.ntoken(s, pytoklib.sa1)
        for vi in res:
            print(vi[0])
            print(vi[1])
