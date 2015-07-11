import numpy as np
import convolve

def main():
    N = 100
    f = np.arange(N*N, dtype=np.int).reshape((N,N))
    g = np.arange(81, dtype=np.int).reshape((9, 9))
    return convolve.naive_convolve(f, g)

import pstats, cProfile
cProfile.runctx("main()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
