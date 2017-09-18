# Create binomial series. Column1 = current value Column2 = previous value.
# Column1 is y_hat, predicted by column 2.... Essentially, column 2 is the prediction, column 1 is the actual. The difference is the error.
def persist(var):
    xy = lag(var, 1)
    print xy.columns
    y_hat = xy['%d' % var]
    y = xy['t - 1']
    error = []
    for i in range(len(xy)):
        delta = (y_hat[i] - y[i])
        error.append(delta)
    mae = sum(abs(err) for err in error)/len(error)
    mse = sum(err*err for err in error)/len(error)
    return ('mae = %d mse = %d' % mae, mse)

