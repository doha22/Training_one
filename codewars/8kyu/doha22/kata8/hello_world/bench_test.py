from hello_world import greet
from hello_world import greet2

def test(benchmark):
    assert benchmark(greet, ) == "hello world!"



def test2(benchmark):
    assert benchmark(greet2,  ) == "hello world!"

''''''''''
--------------------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------
-----------------
Name (time in ns)          Min                     Max                  Mean                StdDev                Median                 IQR              Outliers  OPS (Kops/s)            R
ounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------
test                  821.0565 (1.0)      201,569.3674 (1.0)      1,479.5708 (1.0)      2,091.0993 (1.0)      1,231.5847 (1.0)        0.0000 (1.0)      1256;32044      675.8717 (1.0)      1
35328           1
test2                 821.0565 (1.0)      452,812.6522 (2.25)     1,547.1414 (1.05)     2,278.5710 (1.09)     1,231.5847 (1.0)      410.5282 (>1000.0)  1520;10776      646.3533 (0.96)     1
62393           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================ 2 passed in 13.51 seconds =================================================================================

'''''''''''