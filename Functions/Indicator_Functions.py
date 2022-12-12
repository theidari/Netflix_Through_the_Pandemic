# SMA (Simple Moving Average) Indicator
# Help
    # df = DataFrame
    # SMA(df, firstperiod=7, secondperiod=14, Column='Close')
def SMA(df, period_1=7, period_2=14, Column='Close'):
    import numpy as np
    import matplotlib.pyplot as plt
    length=len(df['Date'])
    
    # adding SMA indicator
    df['SMA '+str(period_1)]= df[Column].rolling(window=period_1).mean()
    df['SMA '+str(period_2)]= df[Column].rolling(window=period_2).mean()

    # Buy and Sell Signal Define
    df['Signal']=np.where(df['SMA '+str(period_1)]>df['SMA '+str(period_2)], 1, 0)
    df['Position']=df['Signal'].diff()

    df['Buy']=np.where(df['Position']== 1, df['Close'], np.NAN)
    df['Sell']=np.where(df['Position']== -1, df['Close'], np.NAN)

    plt.figure(figsize=(20,10))
    # If plt.figure does not change the size, try placing it before plt.plot!

    plt.plot(df['Date'], df['Close'], color = 'k', alpha=0.5, label='Close Price')
    plt.plot(df['Date'], df['SMA '+str(period_1)], color = 'r', alpha=0.5, label='SMA Month')
    plt.plot(df['Date'], df['SMA '+str(period_2)], color = 'b', alpha=0.5, label='SMA Seasen')
    sizes = [100]
    plt.scatter(df['Date'], df['Buy'], sizes, alpha=1, marker='^', color= 'limegreen')
    plt.scatter(df['Date'], df['Sell'], sizes, alpha=1, marker='v', color= 'red')
    plt.xticks(np.arange(0, length, 50), rotation = 45, rotation_mode = 'anchor', ha = 'right', fontsize='12')
    plt.yticks(fontsize='12')
    plt.xlim(0, length)
    plt.legend(fontsize='12')
    plt.xlabel('Date (yyyy-mm-dd)', fontsize='14')
    plt.ylabel('Closing Price in ($)', fontsize='14')
    plt.title('Netflix Closing Prices from 2019-01-22 to 2022-06-03', fontsize='16')
    plt.show()
    return