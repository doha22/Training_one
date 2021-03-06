from reverse_order import reverse_list
from reverse_order import reverse_list2

def test(benchmark):
    assert benchmark(reverse_list,[1,2,3,4]) ==  [4,3,2,1]



def test2(benchmark):
    assert benchmark(reverse_list2, [1,2,3,4]  ) ==  [4,3,2,1]

''''''''''
------------------------------------------------------------------------------------------------ benchmark: 2 tests -------------------------------------------------------------------------
----------------------
Name (time in ns)            Min                       Max                  Mean                 StdDev                Median                   IQR            Outliers  OPS (Kops/s)
    Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------
test2                   564.4763 (1.0)      5,366,527.8260 (2.34)     1,713.7785 (1.0)      24,211.7410 (1.55)     1,180.2687 (1.0)        821.0565 (1.0)      352;3622      583.5060 (1.0)
    173992           8
test                  2,052.6412 (3.64)     2,294,442.3508 (1.0)      3,738.6319 (2.18)     15,602.9289 (1.0)      2,463.1695 (2.09)     2,052.6412 (2.50)      309;806      267.4775 (0.46)
     50748           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================ 2 passed in 12.58 seconds =================================================================================

'''''''''''