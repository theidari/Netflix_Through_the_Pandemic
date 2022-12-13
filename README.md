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
<a href="https://github.com/theidari/pymaceuticals#overview-of-project-"><sup>TOP PAGE</sup></a>
</p>

### Results <img src="https://github.com/theidari/project1/blob/main/Images/NetflixLine.png" width="742">
</br>
<h4>First Observation</h4>
<img src="https://github.com/theidari/project1/blob/main/OutputData/StockChart.png" width="800"></br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/COVID-19Chart.png" width="800"></br>

Stock price vs. Number of daily cases showed weak negative correlation with statistical insignificance.Stock price vs. Number of deaths showed positive correlation with statistical significance.</br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22%20New%20Casesmain.png" width="390"><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22%20New%20Deathsmain.png" width="405"></br>

Stock price a week after vs. Number of daily cases showed weak negative correlation with statistical insignificance.Stock price a week after vs. Number of deaths showed positive correlation with statistical significance.</br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/2020-02-01%20New%20Casesmain.png" width="390"><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-02-01%20New%20Deathsmain.png" width="405"></br>

<h4>Stock Indicator</h4>
<b>1. Simple Moving Average (SMA) Indicator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SMA is the easiest moving average to construct. It is simply the average price over the specified period. The average is called "moving" because it is plotted on the chart bar by bar, forming a line that moves along the chart as the average value changes.</br>
</br>
</br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/SMA_30_90.png" width="800"></br>

<img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2020-11-23_SMAmain.png" width="400"><img src="https://github.com/theidari/project1/blob/main/OutputData/2020-12-29_2021-04-01_SMAmain.png" width="400"></br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/2021-07-15_2021-12-31_SMAmain.png" width="400"><img src="https://github.com/theidari/project1/blob/main/OutputData/2022-01-01_2022-06-09_SMAmain.png" width="400"></br>

<b>2. IchimokuCloud Indicator</b></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The IchimokuKinko Hyo, or Ichimoku for short, is a technical indicator that is used to gauge momentum along with future areas of support and resistance.</br>
</br>
</br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/IchimokuCloud%20Indicator.png" width="800"></br>

<img src="https://github.com/theidari/project1/blob/main/OutputData/2020-01-22_2020-12-31_IchimokuCloudmain.png" width="400"><img src="https://github.com/theidari/project1/blob/main/OutputData/2021-01-01_2021-08-31_IchimokuCloudmain.png" width="400"></br>
<img src="https://github.com/theidari/project1/blob/main/OutputData/2021-09-01_2022-02-01_IchimokuCloudmain.png" width="400"></br>


<table style="width:700">
  <tr>
    <th>Q1</th>
    <td>Stock price vs. Number of daily cases showed weak negative correlation with statistical insignificance.</br>
    Stock price vs. Number of deaths showed positive correlation with statistical significance.</td>
    </th>
  </tr>
  <tr>
    <td>Q2</td>
    <td>Stock price a week after vs. Number of daily cases showed weak negative correlation with statistical insignificance.</br>
    Stock price a week after vs. Number of deaths showed positive correlation with statistical significance.</td>
  </tr>
  <tr>
    <td>Q3</td>
    <td>Result</td>
   <tr>
    <td>Q4</td>
    <td>Netflix's stock movement is oppositely related to Disney's stock movement.</td>
  </tr>
</table>

</p>

### Documents and Reference <img src="https://github.com/theidari/project1/blob/main/Images/NetflixLine.png" width="570">

<h4>Documents</h4>
  - Data Source
  
  <sup>[1]</sup><a href="https://www.kaggle.com/datasets/meetnagadia/netflix-stock-price-data-set-20022022"> Netflix Stock Price Data set 2002-2022 </a></br>
  <sup>[2]</sup><a href="https://ourworldindata.org/grapher/daily-covid-cases-deaths"> Daily confirmed COVID-19 cases and deaths, World </a></br>
  <sup>[3]</sup><a href="https://ca.finance.yahoo.com/"> Yahoo<i>!</i> Finance</a></br>


<h4>Reference</h4>
  
<p align="center">
<img src="https://github.com/theidari/project1/blob/main/Images/NetflixFooter.png" width="900">
</p>

