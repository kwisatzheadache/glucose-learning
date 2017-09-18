from matplotlib import pyplot
from keras.models import Sequential
from keras import models
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
from scipy.stats.stats import pearsonr
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from statsmodels.tsa.season import seasonal_decompose

(persist_mae, persist_mse) = persist(isig)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

model = Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(1))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

model.fit(X_train, Y_train, epochs=5, batch_size=1)
ml5_mse, ml5_mae = model.evaluate(X_test, Y_test)

model.fit(X_train, Y_train, epochs=20, batch_size=1)
ml20_mse, ml20_mae = model.evaluate(X_test, Y_test)

