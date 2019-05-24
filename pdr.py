import pandas_datareader as pdr
import numpy as np
from matplotlib import pyplot as plt
def getData():
    DAX = pdr.data.get_data_yahoo('DAX', '20150626', '20160705', adjust_price=False)
    DAX.rename(columns = {'Adj Close':'index'}, inplace = True)
    DAX['returns'] = np.log(DAX['index']/DAX['index'].shift(1))
    DAX['variance'] = 252 * np.cumsum(DAX['returns'] ** 2 / np.arange(len(DAX)))
    DAX = DAX.dropna()
    return DAX
print(getData())

plt.plot(getData()['returns'])
plt.show()
plt.close()