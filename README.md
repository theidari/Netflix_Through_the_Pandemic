<p align="center">
<img src="https://github.com/theidari/project1/blob/main/Images//Netflix.png" width="900">
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is no secret that <a href="https://www.netflix.com/"> <b>Netflix, Inc.</b></a> is the champion in the online streaming revolution. Its streaming platform allows users to watch ad-free content anytime and anywhere over the Internet. Its content library includes television shows, documentaries, and feature films covering a wide range of genres and languages. As of now, Netflix has over 208m paid subscribers worldwide, 74m of whom are in the USA. Such unlimited access to digital content has given rise to a growing trend known as “binge-watching”; the consumption of multiple episodes of a show in one sitting. For instance, Nielson has reported that 361,000 Netflix subscribers have seen all nine episodes of Stranger Things season 2 in one sitting within 24 h of its release.


### Project Overview <img src="https://github.com/theidari/project1/blob/main/Images/NetflixLine.png" width="650">




<table border="0px">
  <tr>
  <td colspan="1"><img src="https://github.com/theidari/project1/blob/main//Images/3288524.jpg" width="400"></td>
  <td colspan="1"><b>Project Idea:</b></br> This project explores the impact of COVID-19 on Netflix's stock price from 2019 to 2022 through different indicators. These indicators include variables like the number of daily cases and the number of deaths. </br></br>
<img src="https://github.com/theidari/project1/blob/main/Images/Reason.png" width="600">
</td>
  </tr>
</table>

<table border="0px">
    <td rowspan="5"><img src="https://github.com/theidari/project1/blob/main/Images/Hypothesis.png" width="350">
</td>
    <td colspan="2" align="center"><img src="https://github.com/theidari/project1/blob/main/Images/3567801.jpg" width="200"></br><b>Questions</b>
</td>
  </tr>
  <tr>
    <td><b>Q1</b></td>
    <td>
    Is there a relationship between the stock price vs. number of daily cases/death worldwide?</br>
    </td>
  </tr>
  <tr>
    <td><b>Q2</b></td>
    <td>
    Is there a relationship between the stock price a <b><i>week after</b></i> the case count/death count vs. number of daily cases worldwide?</br>
    </td>
  </tr>
  <tr>
    <td><b>Q3</b></td>
    <td>
    Is there a relationship between the stock price vs. number of daily cases/deaths by <b><i>stock indicator</b></i>?</br>
    </td>
  </tr>
<tr>
    <td><b>Q4</b></td>
    <td>
    Is the price movement an industry-wide trend?</br> 
    <b><i>compare Netflix with their main competitor Disney+</b></i>
    </td>
  </tr>
  </tr>
</table>

#### Methods, Software and Attribution

- The analyses were performed using the <a href="https://ourworldindata.org/grapher/daily-covid-cases-deaths"> Daily confirmed COVID-19 cases and deaths, World </a> and <a href="https://ca.finance.yahoo.com/"> Yahoo<i>!</i> Finance</a>. Also,the correlation checked by Linear Reression method.

- Following programming languages, software, and libraries were used in this project:

<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> `python v.3.9.13`</br>
<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> `jupyter notebook v.6.4.12`
`Visual Studio v.1.73.1`
`PowerPoint v.16.0.14026.20298`</br>
<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> `pandas v.1.4.4`
`SciPy v.1.9.3`
`Matplotlib v.3.6.0`
`yfinance 0.1.89`
`NumPy v.1.23.4`
`plotly 5.11.0` 
`DateTime 4.7`</br>

- The project header GIF has been designed by powerpoint and `photopea.com` using <a href="https://about.netflix.com/en/company-assets">Netflix Logo</a> and assets from `Freepik.com` (include: <a href="https://www.freepik.com/free-vector/questions-concept-illustration_7191139.htm#from_view=detail_author">Questions</a>,
<a href="https://www.freepik.com/free-vector/organic-flat-doctors-nurses-with-medical-masks_13641486.htm#query=doctor%20with%20mask&position=11&from_view=search&track=sph">Doctors / Nurses with Masks</a>, and <a href="https://www.freepik.com/free-vector/conversation-concept-illustration_7118856.htm#from_view=detail_author">Conversation</a>).


<h4 align=left>How to Use</h4>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Before start, you will need install the libraries, for example:

```python
# yahoo finance installation
pip install yfinance
```

<h4>Team Members</h4>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ji Yeol (Eric) Yang</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ali Taghipour Heidari</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hammad Ahmed</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<s>Nimra Wali</s></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<s>Jeremiah Sulunteh</s></br>

<p align="right">
<a href="https://github.com/theidari/project1#project-overview-"><sup>TOP PAGE</sup></a>
</p>

### Results <img src="https://github.com/theidari/project1/blob/main/Images/NetflixLine.png" width="742"></br>
<img src="https://github.com/theidari/project1/blob/main/Images/FirObs.png" width="180"></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Netflix Close Price from 2019 to end of 2022 and Covid-19 daily cases and deaths at the same time are are shown in figure [1] and figure [2] in order.
<h6 align="center">Fig [1]: Netflix Close Price Pre/During/Post Pandemic</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/StockChart.png" width="700">
</p>
<h6 align="center">Fig [2]: Covid-19 Daily Cases and Deaths</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/COVID-19Chart.png" width="680"></br>
</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stock price vs. Number of daily cases showed weak negative correlation <b>(-0.06)</b> with statistical insignificance <b>(p-value is 0.1129)</b>.But, Stock price vs. Number of deaths showed positive moderate correlation <b>(0.69)</b> with statistical significance.figure [3]</br>
<h6 align="center">Fig [3]: Stock price vs. Number of Cases and Deaths</h4>
<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22%20New%20Casesmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22%20New%20Deathsmain.png" width="350"></td>
</tr>
</table>

Same as pervious result, after a week lagged stock price vs. Number of daily cases showed weak negative correlation <b>(-0.07)</b> with statistical insignificance <b>(p-value is 0.0784)</b>.But, Stock price vs. Number of deaths showed positive moderate correlation <b>(0.69)</b> with statistical significance.figure [4]</br>
<h6 align="center">Fig [4]: Stock price vs. Number of Cases and Deaths a week after lagged</h4>
<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-02-01%20New%20Casesmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-02-01%20New%20Deathsmain.png" width="350"></td>
</tr>
</table>

<img src="https://github.com/theidari/project1/blob/main/Images/StcInd.png" width="180"></br>
<b>1. Simple Moving Average (SMA) Indicator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SMA is the easiest moving average to construct. It is simply the average price over the specified period. The average is called "moving" because it is plotted on the chart bar by bar, forming a line that moves along the chart as the average value changes. figure [5] shows monthly and seasenaly moving average for netflix stock.</br>

<h6 align="center">Fig [5]: Netflix SMA & Buy/Sell signal</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/SMA_30_90.png" width="700"></br>
</p>

For the <i><b>SMA Indicator</b></i> depending on the true buy and sell signal, we broke the time into 4 stages, <ins>2020/01/22 to 2020/11/23 (A), 2020/12/29 to 2021/04/01 (B), 2021/07/15 to 2021/12/31 (C), and 2022/01/01 to 2022/06/09</ins>. From 2020/01/22 to 2020/11/23 (A) Netflix price vs. the Number of daily cases/ deaths, showed a <b>moderate to strong positive</b> correlation (0.75 Cases / 0.67 Deaths) with statistical significance. But this result is not repeated from 2020/12/29 to 2021/12/31 (B, C). in this point, Netflix price vs. the Number of daily cases/ deaths has a <b>negative very-week and week</b> correlation in most parts (B: -0.3 Cases / 0.2 Deaths and C: -0.17 Cases) with statistical insignificance (p-value: 0.116 and 0.059) except (C:-0.57 Deaths) with <b>moderate negative</b> correlation with statistical significance. In the last part (D), Netflix price vs. the Number of daily cases/ deaths showed a <b>strong positive</b> correlation (0.82 Cases / 0.71 Deaths) with statistical significance. Figure [6]

<h6 align="center">Fig [6]: Stock price vs. Number of Cases and Deaths by SMA & Buy/Sell signal</h4>
<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2020-11-23_SMAmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-12-29_2021-04-01_SMAmain.png" width="350"></td>
</tr>
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2021-07-15_2021-12-31_SMAmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2022-01-01_2022-06-09_SMAmain.png" width="350"></td>
</tr>
</table>
</br>
<b>2. IchimokuCloud Indicator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The IchimokuKinko Hyo, or Ichimoku for short, is a technical indicator that is used to gauge momentum along with future areas of support and resistance.</br>

<h6 align="center">Fig [7]: Netflix IchimokuCloud</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/IchimokuCloud%20Indicator.png" width="700"></br>
</p>

For the <i><b>IchimokuCloud Indicator</b></i> depending on gauge momentum, we broke the time into 3 stages, <ins>2020/01/22 to 2020/12/31(A), 2021/01/01 to 2021/08/31 (B), and 2021/09/01 to 2022/02/01 (C)</ins>. From 2020/01/22 to 2020/12/31 (main covid year) Netflix price vs. the Number of daily cases/ deaths showed a <b>strong positive</b> correlation (0.75 Cases / 0.69 Deaths) with statistical significance. But this result is not repeated in the next 2 years (B, C). B has a very-week correlation (-0.05 Cases / 0.06 Deaths) with statistical insignificance (p-value: 0.481 and 0.417) and C has a strong negative correlation for Cases (-0.82) and negative week correlation for deaths (0.49) with statistical significance. Figure [8]

<h6 align="center">Fig [8]: Stock price vs. Number of Cases and Deaths by IchimokuCloud</h4>
<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2020-12-31_IchimokuCloudmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2021-01-01_2021-08-31_IchimokuCloudmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2021-09-01_2022-02-01_IchimokuCloudmain.png" width="350"></td>
</tr>
</table>

</br>
<b>3. Average directional index (ADX) Indicator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ADX stands for Average Directional Movement Index and can be used to help measure the overall strength of a trend. The ADX indicator is an average of expanding price range values. The ADX is a component of the Directional Movement System developed by Welles Wilder.</br>

<h6 align="center">Fig [9]: Netflix ADX</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/ADX.png" width="700"></br>
</p>

For the <i><b>Average directional index (ADX) Indicator </i></b> depending on ADX of less than 25% because it is not used by traders and the trend is not strong enough, we had 3 steps around the covid year, ADX 14 Days < 25% (A), ADX Month < 25% (B), and Both ADX < 25% (C). All these steps showed <b>moderate</b> correlation with statistical significance.Figure [10]

<h6 align="center">Fig [10]: Stock price vs. Number of Cases and Deaths by ADX</h4>
<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_ADX14main.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_ADX30main.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_ADX1430main.png" width="350"></td>
</tr>
</table>
</br>

<b>4. Stochastic Oscillator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The stochastic oscillator is a momentum indicator that is widely used in forex trading to pinpoint potential trend reversals. This indicator measures momentum by comparing the close price to the trading range over a given period.</br>

<h6 align="center">Fig [11]: Netflix Stochastic Oscillator</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/Stochastic%20Oscillator.png" width="700"></br>
</p>

For the <i><b>Stochastic Oscillator</b></i> Indicator depending on the trading range, we had 2 steps around the covid year, 20%<oscillator< 80% (A), 20%>oscillator> 80% (B). Both oscillators showed a moderate <ins>positive correlation (A: 0.5 and B:0.68) in Death with statistical significance</ins>.

<h6 align="center">Fig [12]: Stock price vs. Number of Cases and Deaths by Stochastic Oscillator</h4>

<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_SOinmain.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_SOoutmain.png" width="350"></td>
</tr>
</table>
</br>

<b>5. Relative Strength Index(RSI) Indicator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Readings below 30 generally indicate that the stock is oversold, while readings above 70 indicate that it is overbought. Traders will often place this RSI chart below the price chart for the security, so they can compare its recent momentum against its market price.</br>

<h6 align="center">Fig [11]: Netflix RSI</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/rsi.png" width="700"></br>
</p>
For <i><b>RSI Indicator</b></i> depending on the trader’s behavior, we had 2 steps around the covid year, regular 30%<oscillator< 70% (A), oversold/buy 30%>oscillator> 70% (B). similar to stochastic oscillator behaviors showed a <ins>moderate to strong positive correlation (A: 0.5 and B:0.7) in Death with statistical significance</ins>.

<h6 align="center">Fig [14]: Stock price vs. Number of Cases and Deaths by RSI</h4>

<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_RSIinmain.png" width="400"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2022-06-01_RSIoutmain.png" width="400"></td>
</tr>
</table>
</br>

<img src="https://github.com/theidari/project1/blob/main/Images/netd.png" width="180"></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Netflix's stock closing price is more than Disney's stock closing price.</br>
<h6 align="center">Fig [15]: Netflix stock price vs. Disney's stock price</h4>

<table align="center">
<tr>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/netvsdis.png" width="350"></td>
<td><img src="https://github.com/theidari/project1/blob/main/OutputData/boxnetdis.png" width="350"></td>
</tr>
</table>
</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Netflix's stock movement is oppositely related to Disney's stock movement.</br>
<h6 align="center">Fig [16]: Netflix vs. Disney's Movement</h4>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/OutputData/corrnetdis.png" width="400"></br>
</p>
</br>

### Documents and Reference <img src="https://github.com/theidari/project1/blob/main/Images/NetflixLine.png" width="570">

<h4>Documents</h4>


<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> <i>Data Source</i></br>
<sup>[1]</sup><a href="https://www.kaggle.com/datasets/meetnagadia/netflix-stock-price-data-set-20022022"> Netflix Stock Price Data set 2002-2022 </a></br>
<sup>[2]</sup><a href="https://ourworldindata.org/grapher/daily-covid-cases-deaths"> Daily confirmed COVID-19 cases and deaths, World </a></br>
<sup>[3]</sup><a href="https://ca.finance.yahoo.com/"> Yahoo<i>!</i> Finance</a></br>

<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> <i>Code</i></br>
<sup>[1]</sup><a href="https://github.com/theidari/project1/tree/main/Functions">Functions</a></br>
<sup>[2]</sup><a href="https://github.com/theidari/project1/tree/main/Code">Main Code</a></br>

<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> <i>Result Output</i></br>
<sup>[1]</sup><a href="https://github.com/theidari/project1/tree/main/OutputData">Figures</a></br>

<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/red.png" width="10"> <i>Result DataFrame</i></br>
<sup>[1]</sup><a href="https://github.com/theidari/project1/blob/main/OutputData/stock_analaysis.csv">Stock Analaysis</a></br>

<h4>Reference</h4>
<sup>[1]</sup><a href="https://www.ig.com/en/trading-strategies/10-trading-indicators-every-trader-should-know-190604">10 Trading Indicators Every Trader Should Know</a></br>
<sup>[2]</sup><a href="https://www.investopedia.com/articles/trading/07/adx-trend-indicator.asp">ADX</a></br>


<p align="right">
<a href="https://github.com/theidari/project1#project-overview-"><sup>TOP PAGE</sup></a>
</p>
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/Images/NetflixFooter.png" width="900">
</p>

