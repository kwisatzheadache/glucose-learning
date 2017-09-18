from matplotlib import pyplot
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
from scipy.stats.stats import pearsonr
from math import sqrt
from sklearn.metrics import mean_squared_error

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
# seasonal = seasonal_decompose(series['isig'], model='additive', frequency=10)
# seasonal.plot()
# pyplot.show()
# seasonal = seasonal_decompose(series['glucose'], model='additive', frequency=10)
# seasonal.plot()
# pyplot.show()
