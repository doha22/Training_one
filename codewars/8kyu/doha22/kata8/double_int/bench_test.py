from double_int import double_integer
from double_int import doubleInteger2

def test(benchmark):
    assert benchmark(double_integer,2) == 4



def test2(benchmark):
    assert benchmark(doubleInteger2, 2) == 4

'''''''''

----------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------
Name (time in us)        Min                   Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.2316 (1.0)        270.9486 (1.0)      1.7099 (1.0)      2.7570 (1.0)      1.6421 (1.0)      0.4105 (1.0)     882;10415      584.8393 (1.0)       97436           1
test2                 1.2316 (1.0)      2,124.8942 (7.84)     2.5951 (1.52)     8.9981 (3.26)     1.6421 (1.00)     1.2316 (3.00)     925;5498      385.3480 (0.66)     152243           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================ 2 passed in 12.16 seconds =================================================================================





''''''''''''''