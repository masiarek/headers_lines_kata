import random
from dataclasses import dataclass
import string
import pytest

random.seed(1)


@dataclass
class H:
    hdr_n: int = 900  # Header Number / key

    def __init__(self, h_desc=None):
        H.hdr_n += 1
        if h_desc is None:
            self.h_desc = "".join(random.choices(string.ascii_letters, k=4))
        else:
            self.h_desc = h_desc
        self.hdr_n = H.hdr_n

    def change_desc(self, hdr_n, new_desc):
        if hdr_n != self.hdr_n:
            raise ValueError("Not a valid header number")
        self.hdr_n = hdr_n
        self.h_desc = new_desc
        
if __name__ == '__main__':
    h1 = H("Desc")
    dict_h = {}
    dict_h[h1.hdr_n] = h1.h_desc
    for _ in range(3):
        temp = H()
        dict_h[temp.hdr_n] = temp.h_desc

    for k, v in dict_h.items():
        print(k, v)
