from prim_of_num import num_primorial
from prim_of_num import num_prime2


def test(benchmark):
    assert benchmark(num_primorial, 3) == 30


def test2(benchmark):
    assert benchmark(num_prime2, 3) == 30

''''''''''
-------------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------
---
Name (time in us)         Min                   Max               Mean              StdDev             Median                IQR            Outliers  OPS (Kops/s)            Rounds  Iterati
ons
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---
test                  13.1369 (1.0)      1,596.9568 (1.0)      21.4372 (1.0)       23.4670 (1.0)      14.7790 (1.0)      11.4948 (1.0)       619;640       46.6478 (1.0)       22766
  1
test2                 13.5474 (1.03)     9,268.9181 (5.80)     32.1588 (1.50)     127.8420 (5.45)     27.0949 (1.83)     16.0106 (1.39)      168;753       31.0957 (0.67)      18595
  1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 4.54 seconds =================================================================================

'''''''