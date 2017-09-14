from pandas import Series
from pandas import concat
from pandas import read_csv
from pandas import to_numeric
from scipy.stats.stats import pearsonr
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
from scipy.stats.stats import pearsonr
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas import to_datetime

raw = read_csv('./CGM.csv', header=0)

isig = to_numeric(raw['isig'][:39450])
glucose = to_numeric(raw['glucose'][:39450])
datetime = raw['datetime'][:39450]
series = DataFrame({'isig': isig, 'glucose': glucose})
series.index = to_datetime(datetime)
pearsonr(isig, glucose)

# Exploring the data

# Descriptive stats 
isig.describe()
isig.plot()
pyplot.show()

# Skewed toward the higher side
isig.hist()
pyplot.show()
# Significantly autocorrelated as expected.
autocorrelation_plot(isig)
pyplot.show()

# Check for autocorrelation. As expected, isig is directly related to previous values. High autocorrelation.
lag_plot(isig)
pyplot.show()

# Check for seasonality
seasonal = seasonal_decompose(series['isig'], model='additive', frequence=10)
seasonal.plot()
pyplot.show()
seasonal = seasonal_decompose(series['glucose'], model='additive', frequence=10)
seasonal.plot()
pyplot.show()

# Manually shift the series to create window
values = DataFrame(isig.values)
tenshift = concat([values.shift(9), values.shift(8), values.shift(7), values.shift(6), values.shift(5), values.shift(4), values.shift(3), values.shift(2), values.shift(1), values], axis = 1)
tenshift.columns = ['t-8', 't-7', 't-6', 't-5', 't-4', 't-3', 't-2', 't-1', 't', 't+1']

# Function to automate creation of lagged data from variable and window-size
def lag(variable, window):
    df1 = DataFrame(variable)
    for i in range(window):
        j = window - i
        df1 = concat([df1, variable.shift(j)], axis=1)
    columns = [variable.name]
    for i in range(window):
        j = window - i
        columns.append('t - %d' % j)
    df1.columns = columns
    return df1.iloc[window:]

lagged = lag(isig, 10).values
X = lagged[:, 1:]
Y = lagged[:, 0]
test_size = 0.33
seed = 7

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
model = LogisticRegression()
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)


# create training, validation, and test sets
# split = int(len(lagged)/3)
# train = lagged[:split]
# valid = lagged[split:(split*2)]
# test = lagged[split*2:]

# Use train_test_split/4 instead


