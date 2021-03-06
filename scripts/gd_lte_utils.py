bitspsym = [ 0.1647619 ,  0.21428571,  0.26380952,  0.34,  0.43142857,
        0.52285714,  0.61428571,  0.73809524,  0.82952381,  0.95142857,
        0.95142857,  1.04285714,  1.18      ,  1.36285714,  1.54285714,
        1.68      ,  1.81714286,  1.81714286,  1.95428571,  2.18285714,
        2.31952381,  2.54571429,  2.72857143,  3.03047619,  3.25904762,
        3.37333333,  3.64      ,  3.77428571]

qfactor = [2,2,2,2,2,
          2,2,2,2,2,
          4,4,4,4,4,
          4,4,6,6,6,
          6,6,6,6,6,
          6,6,6]

turbo_iter = 2


def mcs_to_turbo(mcs):
    return int(bitspsym[mcs]*96.8)

def mcs_to_time(mcs, num_ants):
    dl_time = 0
    return int(bitspsym[mcs]*96.8*turbo_iter + 43.9*qfactor[mcs] + 93.0*num_ants + 28.4 + dl_time)

def mcs_to_throughput(mcs):
    return int(bitspsym[mcs]*(14*12*50)*1.0/10**3)

