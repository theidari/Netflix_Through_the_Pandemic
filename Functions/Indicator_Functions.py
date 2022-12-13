# SMA (Simple Moving Average) Indicator
# Help
# df = DataFrame
# SMA(df, firstperiod=7, secondperiod=14, Column='Close')
def SMA(df, period_1=7, period_2=14, Column='Close'):
    import numpy as np
    import matplotlib.pyplot as plt
    length == len(df['Date'])

    # adding SMA indicator
    df['SMA ' + str(period_1)] = df[Column].rolling(window=period_1).mean()
    df['SMA ' + str(period_2)] = df[Column].rolling(window=period_2).mean()

    # Buy and Sell Signal Define
    df['Signal'] = np.where(df['SMA ' + str(period_1)] > df['SMA ' + str(period_2)], 1, 0)
    df['Position'] = df['Signal'].diff()

    df['Buy'] = np.where(df['Position'] == 1, df['Close'], np.NAN)
    df['Sell'] = np.where(df['Position'] == -1, df['Close'], np.NAN)

    plt.figure(figsize=(20, 10))
    # If plt.figure does not change the size, try placing it before plt.plot!

    plt.plot(df['Date'], df['Close'], color='k', alpha=0.5, label='Close Price')
    plt.plot(df['Date'], df['SMA ' + str(period_1)], color='r', alpha=0.5, \
             label='SMA ' + str(period_1))
    plt.plot(df['Date'], df['SMA ' + str(period_2)], color='b', alpha=0.5, \
             label='SMA ' + str(period_2))
    sizes = [200]
    plt.scatter(df['Date'], df['Buy'], sizes, alpha=1, marker='^', color='limegreen')
    plt.scatter(df['Date'], df['Sell'], sizes, alpha=1, marker='v', color='red')
    plt.xticks(np.arange(0, length, 50), rotation=45, rotation_mode='anchor', \
               ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlim(0, length)
    plt.legend(fontsize=16)
    plt.xlabel('Date (yyyy-mm-dd)', fontsize=18)
    plt.ylabel('Closing Price in ($)', fontsize=18)
    plt.title("Netflix Closing Prices from " + stock_cases['Date'][0] + " to " + \
              stock_cases['Date'][length - 1], fontsize=20)
    plt.savefig(OutputData + "\\" + "SMA" + "_" + str(period_1) + "_" + str(period_2) + ".png", \
                dpi=300, bbox_inches='tight')
    return plt.show()

# IchimokuCloud Indicator
def IchimokuCloud(df):
    high_9 = df['High'].rolling(window= 9).max()
    low_9 = df['Low'].rolling(window= 9).min()
    df['tenkan_sen'] = (high_9 + low_9) /2

    high_26 = df['High'].rolling(window= 26).max()
    low_26 = df['Low'].rolling(window= 26).min()
    df['kijun_sen'] = (high_26 + low_26) /2

    last_index = df.iloc[-1:].index[0]
    last_date = df['Date']

    df['senkou_span_a'] = ((df['tenkan_sen'] + df['kijun_sen']) / 2).shift(26)

    high_52 = df['High'].rolling(window= 52).max()
    low_52 = df['Low'].rolling(window= 52).min()
    df['senkou_span_b'] = ((high_52 + low_52) /2).shift(26)

    df['chikou_span'] = df['Close'].shift(-22)

    plt.figure(figsize=(20,10))
    plt.plot(df['Date'], df['Close'], color = 'k', alpha=0.5, label='Close Price')
    plt.plot(df['Date'], df['senkou_span_a'], color = 'limegreen', alpha=0.5, label='Senkou Span A')
    plt.plot(df['Date'], df['senkou_span_b'], color = 'orangered', alpha=0.5, label='Senkou Span B')
    plt.fill_between(df['Date'], df.senkou_span_a, df.senkou_span_b,where = df.senkou_span_a >=\
                    df.senkou_span_b, color = 'limegreen')
    plt.fill_between(df['Date'], df.senkou_span_a, df.senkou_span_b,where = df.senkou_span_a < \
                    df.senkou_span_b, color = 'orangered')
    plt.xticks(np.arange(0, length, 50), rotation = 45, rotation_mode = 'anchor', ha = 'right', fontsize='12')
    plt.yticks(fontsize='12')
    plt.xlim(0, length)
    plt.legend(fontsize='12')
    plt.xlabel('Date (yyyy-mm-dd)', fontsize='14')
    plt.ylabel('Closing Price in ($)', fontsize='14')
    plt.title("Netflix Closing Prices from "+ stock_cases['Date'][0] +" to "+\
              stock_cases['Date'][length - 1] , fontsize=20)
    plt.savefig(OutputData + "\\" + f"IchimokuCloud Indicator.png",\
               dpi=300, bbox_inches='tight')
    return plt.show()

# Average directional index (ADX)
def ADX(df, period):
    alpha = 1/period

    # TR
    df['H-L'] = df['High'] - df['Low']
    df['H-C'] = np.abs(df['High'] - df['Close'].shift(1))
    df['L-C'] = np.abs(df['Low'] - df['Close'].shift(1))
    df['TR'] = df[['H-L', 'H-C', 'L-C']].max(axis=1)
    del df['H-L'], df['H-C'], df['L-C']

    # ATR
    df['ATR'] = df['TR'].ewm(alpha=alpha, adjust=False).mean()

    # +-DX
    df['H-pH'] = df['High'] - df['High'].shift(1)
    df['pL-L'] = df['Low'].shift(1) - df['Low']
    df['+DX'] = np.where(
        (df['H-pH'] > df['pL-L']) & (df['H-pH']>0),
        df['H-pH'],
        0.0
    )
    df['-DX'] = np.where(
        (df['H-pH'] < df['pL-L']) & (df['pL-L']>0),
        df['pL-L'],
        0.0
    )
    del df['H-pH'], df['pL-L']

    # +- DMI
    df['S+DM'] = df['+DX'].ewm(alpha=alpha, adjust=False).mean()
    df['S-DM'] = df['-DX'].ewm(alpha=alpha, adjust=False).mean()
    df['+DMI'] = (df['S+DM']/df['ATR'])*100
    df['-DMI'] = (df['S-DM']/df['ATR'])*100
    del df['S+DM'], df['S-DM']

    # ADX
    df['DX'] = (np.abs(df['+DMI'] - df['-DMI'])/(df['+DMI'] + df['-DMI']))*100
    df['ADX'+str(period)] = df['DX'].ewm(alpha=alpha, adjust=False).mean()
    del df['DX'], df['ATR'], df['TR'], df['-DX'], df['+DX'], df['+DMI'], df['-DMI']

    return df

fig,(ax1, ax2) = plt.subplots(nrows=2, sharex=True, figsize=(20,10))
# If plt.figure does not change the size, try placing it before plt.plot!

ax1.plot(stock_cases['Date'], stock_cases['ADX30'], color = 'green', label='ADX: Month')
# plt.plot(final_stock_cases['Date'], final_stock_cases['ADX7'], color = 'red', label='Week')
ax2.plot(stock_cases['Date'], stock_cases['ADX14'], color = 'k', label='ADX: 14 Days')
plt.xticks(np.arange(0, len(stock_cases['Date']), 50), rotation = 45, rotation_mode = 'anchor', ha = 'right')
# plt.xlim(0, 598)
ax1.axhline(25, color='orange', linestyle='dotted')
ax2.axhline(25, color='orange', linestyle='dotted')
# ax1.axhline(31, color='orange', linestyle='dotted')
plt.xlabel('Date (yyyy-mm-dd)')
ax1.set_ylabel(f"ADX (%)", fontsize=11)
ax2.set_ylabel(f"ADX (%)", fontsize=11)
ax1.legend()
ax2.legend()
plt.savefig(OutputData + "\\" + f"ADX.png",\
               dpi=300, bbox_inches='tight')
plt.show()

# Stochastic Oscillator
stock_cases['14high'] = stock_cases['High'].rolling(14).max()
stock_cases['14low'] = stock_cases['Low'].rolling(14).min()
stock_cases['%K'] = (stock_cases['Close'] - stock_cases['14low'])*100/\
(stock_cases['14high'] - stock_cases['14low'])
stock_cases['%D'] = stock_cases['%K'].rolling(7).mean()

fig, ax = plt.subplots(figsize=(20,10))
ax.plot(stock_cases['Date'], stock_cases['%K'], color = 'k', alpha=0.5, label='K')
ax.plot(stock_cases['Date'], stock_cases['%D'], color = 'red', label='D')
ax.axhline(20, linestyle='--', color="orange")
ax.axhline(80, linestyle="--", color="orange")
plt.xticks(np.arange(0, length, 50), rotation = 45, rotation_mode = 'anchor', ha = 'right', fontsize='12')
plt.yticks(fontsize='12')
plt.xlim(0, length)
plt.legend(fontsize='12')
plt.xlabel('Date (yyyy-mm-dd)', fontsize=14)
plt.ylabel('Stochastic Oscillator (%)', fontsize=14)
plt.savefig(OutputData + "\\" + f"Stochastic Oscillator.png",\
               dpi=300, bbox_inches='tight')
plt.show()

# Define Exponential Moving Average
def EMA(df,period=7, Column='Close'):
    return df[Column].ewm(span=period, adjust=False).mean()

def RSIIndicator(df, period=14, Column='Close'):
    delta = df[Column].diff(1)
    df['gain'] = delta.clip(lower=0).round(2)
    df['loss'] = delta.clip(upper=0).abs().round(2)
    df['avg_gain'] = df['gain'].rolling(window=period, min_periods=period).mean()[:period+1]
    df['avg_loss'] = df['loss'].rolling(window=period, min_periods=period).mean()[:period+1]
    for i, row in enumerate(df['avg_gain'].iloc[period+1:]):
    # Average Gain
        df['avg_gain'].iloc[i + period + 1] =\
        (df['avg_gain'].iloc[i + period] *(period - 1) +\
         df['gain'].iloc[i + period + 1])\
        / period
    # Average Losses
    for i, row in enumerate(df['avg_loss'].iloc[period+1:]):
        df['avg_loss'].iloc[i + period + 1] =\
        (df['avg_loss'].iloc[i + period] *
         (period - 1) +
         df['loss'].iloc[i + period + 1])\
        / period
        # Calculate RS Values
    df['rs'] = df['avg_gain'] / df['avg_loss']
    # Calculate RSI
    df['rsi'] = 100 - (100 / (1.0 + df['rs']))
    return