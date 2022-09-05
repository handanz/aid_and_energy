import os
import numpy as np
import pandas as pd
import openpyxl
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.iolib.summary2 import summary_col
from statsmodels.iolib.table import SimpleTable
from statsmodels.tsa.stattools import adfuller

# Set directory path to current directory
dir_path = os.path.abspath('../')
output_path = os.path.abspath('../outputs')

dat = os.path.join(dir_path, 'control_variables.xlsx')

df = pd.read_excel(dat, index_col=0, sheet_name="data")
df = pd.DataFrame(df)

df['log rgen'] = np.log2(df['rgen cumulative']+1)

def adf_test(timeseries):
    print("Results of Dickey-Fuller Test:")
    dftest = adfuller(timeseries, autolag="AIC")
    dfoutput = pd.Series(
        dftest[0:4],
        index=[
            "Test Statistic",
            "p-value",
            "#Lags Used",
            "Number of Observations Used",
        ],
    )
    for key, value in dftest[4].items():
        dfoutput["Critical Value (%s)" % key] = value
    print(dfoutput)
    
for name, group in df.groupby('country'):
    # print(f'This is the ADf test results for {name}\'s cumulative value for aid in energy distribution')
    adf_test(group['log rgen'])