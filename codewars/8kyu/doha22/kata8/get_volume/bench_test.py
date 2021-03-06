from get_volume import getVolumeOfCubiod
from get_volume import getVolumeOfCubiod2

def test(benchmark):
    assert benchmark(getVolumeOfCubiod,1, 2, 2 ) == 4



def test2(benchmark):
    assert benchmark(getVolumeOfCubiod2, 1, 2, 2 ) == 4

'''''''''''
------------------------------------------------------------------------------------ benchmark: 2 tests -----------------------------------------------------------------------------------
Name (time in us)        Min                   Max              Mean             StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.2316 (1.0)      3,063.3618 (1.0)      2.7231 (1.22)     14.1510 (1.0)      2.0526 (1.25)     1.2316 (1.50)     581;2587      367.2253 (0.82)     128205           1
test2                 1.2316 (1.0)      5,282.6774 (1.72)     2.2297 (1.0)      14.5442 (1.03)     1.6421 (1.0)      0.8211 (1.0)      383;3053      448.4966 (1.0)      152243           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================ 2 passed in 12.73 seconds =================================================================================




'''''''''''