import numpy as np
import pandas as pd
import math
from task2 import *
from pseudo_steady_state import *
#%%
pwf = np.linspace(100, 3000, 20)
print(calculate_q(pwf,30, 30, 3000, 2, 1.2, 2000, 0.244, 3))
#%%