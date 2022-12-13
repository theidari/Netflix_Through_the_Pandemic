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
    Relationship between the stock price vs. number of daily cases/death worldwide</br>
    </td>
  </tr>
  <tr>
    <td><b>Q2</b></td>
    <td>
    Relationship between the stock price a week after vs. number of daily cases/deaths worldwide</br>
    </td>
  </tr>
  <tr>
    <td><b>Q3</b></td>
    <td>
    Relationship between the stock price vs. number of daily cases/deaths by stock indicator</br>
    </td>
  </tr>
<tr>
    <td><b>Q4</b></td>
    <td>
    Is the price movement an industry-wide trend? Compare Netflix with their main competitor Disney +</br>
    </td>
  </tr>
  </tr>
</table>

#### Methods, Software and Attribution

- The analyses were performed using the [OpenWeatherMap Weather](https://api.openweathermap.org/data/2.5/weather?) API in metric units and [Geoapify Place](https://api.geoapify.com/v2/places) API by `accommodation.hotel` category, and correlation checked by Linear Reression method.

- Following programming languages, software, and libraries were used in this project:

<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/redcube.png" width="10"> `python v.3.9.13`</br>
<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/bluecube.png" width="10"> `jupyter notebook v.6.4.12`
`Visual Studio v.1.73.1`
`PowerPoint v.16.0.14026.20298`</br>
<img src="https://github.com/theidari/python-api-challenge/blob/main/Design/yellowcube.png" width="10"> `pandas v.1.4.4`
`SciPy v.1.9.3`
`Matplotlib v.3.6.0`
`citipy v.0.0.5`
`NumPy v.1.23.4`
`GeoViews v.1.9.5` 
`bokeh v.3.0.2`
`hvplot v.0.8.2`</br>

- The project header GIF has been designed by powerpoint and `photopea.com` using <a href="https://about.netflix.com/en/company-assets">Netflix Logo</a> and assets from `Freepik.com` (include: <a href="https://www.freepik.com/free-vector/questions-concept-illustration_7191139.htm#from_view=detail_author">Questions</a>,
<a href="https://www.freepik.com/free-vector/organic-flat-doctors-nurses-with-medical-masks_13641486.htm#query=doctor%20with%20mask&position=11&from_view=search&track=sph">Doctors / Nurses with Masks</a>, and <a href="https://www.freepik.com/free-vector/conversation-concept-illustration_7118856.htm#from_view=detail_author">Conversation</a>).

---

<h3 align=left>How to Use</h3>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Before running <a href="https://github.com/theidari/python-api-challenge/blob/main/WeatherPy/WeatherPy.ipynb">WeatherPy</a> and <a href="https://github.com/theidari/python-api-challenge/blob/main/VacationPy/VacationPy.ipynb">VacationPy</a>, you will need API keys. Create an <b>api_keys.py</b> file in the same directory containing:

```python
# OpenWeatherMap API Key
weather_api_key = "YOUR KEY HERE"

# Geoapify API Key
geoapify_key = "YOUR KEY HERE"
```


<p align="right">
<a href="https://github.com/theidari/pymaceuticals#overview-of-project-"><sup>TOP PAGE</sup></a>
</P>

<h4>Team Members</h4>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ji Yeol (Eric) Yang</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ali Taghipour Heidari</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hammad Ahmed</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nimra Wali</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jeremiah Sulunteh</br>


</p>

### Results <img src="https://github.com/theidari/project1/blob/main/Images/NetflixLine.png" width="742">
</p>

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

