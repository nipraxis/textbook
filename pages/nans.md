# Not a number

>>> import numpy as np
>>> np.nan
nan
>>> np.array(0) / 0
nan
>>> np.nan == 0
False
>>> np.nan == np.nan
False
>>> np.isnan(\[0, np.nan\])
array(\[False,  True\], dtype=bool)
