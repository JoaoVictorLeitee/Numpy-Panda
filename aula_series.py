import numpy as np
import pandas as pd

if __name__ == '__main__':
    list_python = [10,20,30,40,50]
    np_array = np.array(list_python)
    pandas_series = pd.Series(list_python, ["dia1", "dia2", "dia3", "dia4", "dia5"])

    #print(list_python)
    #print(np_array)
    #print(pandas_series)

    #print(pandas_series * 5)
    #print(pandas_series.median())
    #print(type(pandas_series.array))
