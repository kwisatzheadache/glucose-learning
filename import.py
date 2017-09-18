from pandas import Series
from pandas import concat
from pandas import read_csv
from pandas import to_numeric
from pandas import to_datetime
from pandas import DataFrame

raw = read_csv('./CGM.csv', header=0)
isig = to_numeric(raw['isig'][:39450])
glucose = to_numeric(raw['glucose'][:39450])
datetime = raw['datetime'][:39450]

series = DataFrame({'isig': isig, 'glucose': glucose})
series.index = to_datetime(datetime)

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


def persist(x):
    xy = lag(x, 1)
    col = xy.columns
    y_hat = xy[xy.columns[0]]
    y = xy[xy.columns[1]]
    error = []
    for i in range(len(xy)):
        delta = (y_hat[i+1] - y[i+1])
        error.append(delta)
    mae = sum(abs(err) for err in error)/len(error)
    mse = sum(err*err for err in error)/len(error)
    return (mae, mse)

print('Variables declared: isig, glucose. Functions: lag, persist')
