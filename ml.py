from keras.models import Sequential
from keras import layers

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# model = LogisticRegression()
# model.fit(X_train, Y_train)
# result = model.score(X_test, Y_test)


model = Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(1))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

model.fit(X_train, Y_train, epochs=5, batch_size=1)
mse5, mae5 = model.evaluate(X_test, Y_test)

model.fit(X_train, Y_train, epochs=20, batch_size=1)
mse20, mae20 = model.evaluate(X_test, Y_test)

print('Training for 5 epochs, mse=%f mae=%f' % (mse5, mae5))
print('Training for 20 epochs, mse=%f mae=%f' % (mse20, mae20))

