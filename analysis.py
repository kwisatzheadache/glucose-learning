from pandas import Series
from pandas import concat
from pandas import read_csv
from scipy.stats.stats import pearsonr

raw = read_csv('./CGM.csv', header=0)
# ignoring 'glucose', since it is calculated via 'isig'*k and therefore is correlated at R = 1
isig = raw['isig']

# create training, validation, and test sets
split = int(len(isig)/3)
train = isig[:split]
valid = isig[split:(split*2)]
test = isig[split*2:]

from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas import DataFrame

values = DataFrame(isig.values)
tenshift = concat([values.shift(9), values.shift(8), values.shift(7), values.shift(6), values.shift(5), values.shift(4), values.shift(3), values.shift(2), values.shift(1), values], axis = 1)
tenshift.columns = ['t-8', 't-7', 't-6', 't-5', 't-4', 't-3', 't-2', 't-1', 't', 't+1']

# Function to create lagsets from variable and window-size
def lag(variable, window):
    df1 = DataFrame(variable)
    for i in range(window):
        j = window - i
        df1 = concat([df1, variable.shift(j)], axis=1)
    columns = ['isig']
    for i in range(window):
        j = window - i
        columns.append('t - %d' % j)
    df1.columns = columns
    return df1.iloc[window:]
