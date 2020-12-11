import pandas as pd
import numpy as np
from  matplotlib import pyplot as plt



def showcsv(filepath):
    a = pd.read_csv(filepath,names=['high','weight'],sep=',')
    print(a)
    return a 

if __name__ == '__main__':
    #test read_csv
    filepath= './csvtest.csv'
    csv_data = showcsv(filepath)
    
    # test draw
    x = csv_data['high']
    y = csv_data['weight']

    plt.plot(x,y)
    plt.show()
    
    #test dataframe
    data={'a':[1,2,3,4],
    'b':[4,5,6,7]}
    dataframe = pd.DataFrame(data = data,index=range(5,9),columns=['a','b'])
    plt.plot(dataframe['a'],dataframe['b'])
    plt.show()
    print(dataframe)

