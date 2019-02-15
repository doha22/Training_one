from jumping_number import jumping_number
from jumping_number import jumping_number2


def test(benchmark):
    assert benchmark(jumping_number, 1) == "Jumping!!"


def test2(benchmark):
    assert benchmark(jumping_number2, 1) == "Jumping!!"

''''''''''
-------------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------
--
Name (time in us)         Min                   Max               Mean             StdDev             Median                IQR            Outliers  OPS (Kops/s)            Rounds  Iteratio
ns
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--
test2                  2.0526 (1.0)        813.2575 (1.0)       3.7276 (1.0)       3.9965 (1.0)       2.8737 (1.0)       2.4632 (1.0)      1079;926      268.2676 (1.0)      105908
 1
test                  19.7054 (9.60)     2,278.4346 (2.80)     33.8293 (9.08)     33.6839 (8.43)     32.4318 (11.29)    17.2422 (7.00)      165;182       29.5602 (0.11)       5679
 1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 3.48 seconds =================================================================================

'''''''''