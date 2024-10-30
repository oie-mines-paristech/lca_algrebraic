import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import brightway2 as bw
import bw2data
import bw2io
import SALib
from tabulate import tabulate
from sympy import *
from scipy.stats import binned_statistic
import seaborn as sns
from IPython.display import HTML, display

# +
# Custom utils defined for inter-acv
import lca_algebraic as agb

# from lca_algebraic.params import FixedParamMode
# from lca_algebraic.stats import *
# from lca_algebraic.stats import _generate_random_params, _compute_stochastics
# -

from IPython.display import HTML, display

# Larger space in notebook for large graphs
display(HTML("<style>.container { width:70% !important; }</style>"))

# Some options for pandas formatting
pd.options.display.max_rows = 200
pd.options.display.float_format = "{:,.3g}".format