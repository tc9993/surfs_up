<h1>Surfs Up Analysis</h1>

<h2>Purpose</h2>

<h3>Overview of the Analysis</h3>
<p>
  After working with W.Avy on getting all of the temperature data together for Oahu, it was decided that, to determine whether or not a surf and ice cream shop would be a viable business, gathering and analyzing temperature data for June and December would be necessary.
</p>
<p>
  To do this, python, along with Pandas, and SQLAlchemy, was used to retrieve the temperature data via reflecting an SQLite database and leveraging the session.query() method.
</p>
<h2>Results</h2>

<h3>3 Key Differences</h3>
<p align="center">
<img src="https://user-images.githubusercontent.com/78180065/115879182-ff9e6480-a40e-11eb-90e0-a1e439bc1a54.png" alt="June Summary"><br>
  <b>Figure 1.1:</b> June Summary Statistics
</p>
<p align="center">
<img src="https://github.com/tc9993/surfs_up/blob/main/Resources/december_summary.png?raw=true" alt="December Summary"><br>
  <b>Figure 1.2:</b> December Summary Statistics
</p>
<ul>
<li>The difference in average temperature between June and December is only 4 degrees different (75 vs. 71 respectively).  This means there is minimal fluctuation throughout the year in temperature.  Additionally, with the average temperature seemingly in the low to mid 70s year-round ice cream is not out of the question as a treat on an average day in December.</li>
<li>The maximum temperatures for June and December were also very similar at 85 and 83 degrees respectively.  The biggest difference in key summary statistics was the minimum temperature where December had a min of 56deg while June had a min of 64deg.  The minimum temperature in December may impact ice cream sales, however it is also worth considering that over several years of December weather data, 56deg was still the absolute single lowest recorded temperature.  This is still quite temperate for the winter compared to the rest of the United States.</li>
<li>The median of both months is over 70deg (75deg in June, and 71deg in December).  This is important as this means that at least 50% of all days in each month eclipse the 70deg threshold, and important point in determining appetite for ice cream relative to climate.</li>
</ul>

<h2>Summary</h2>

<h3>Summary of Results</h3>
<p>
Overall, the weather between June and December is quite similar with a few differences.  December has a higher standard deviation meaning you are more likely to see more swings in the weather, however more days in both months will be over 70deg than under.  In reviewing the summary statistics, Oahu's climate makes a strong case in favor of opening the surf and ice cream shop there given the temperate year-round climate with minimal drastic fluctuation in daily temperatures.
</p>
<h3>Additional Queries</h3>
<p>
The data analyzed certainly favored opening the surf and ice cream shop, however there are a few other queries that could further bolster or shatter that belief:
<ol>
  <li>Conducting further research into the precipitation levels.  June appeared to have almost +200 precipitation count over December.  Analyzing whether that is due to a few select days during the month where it rains significantly more, or whether each day brings greater rainfall on average would be a point of interest as ice cream may not sound as appetizing if it is raining each day vs. only a select few.</li>
  <li>Determining which weather station is closest to the desired shop location and further analzying that specific data set.  While W.Avy had us initially study the station with the most observations, drilling down into the station closest to the shop location will give us a better idea of what to expect in the physical location we wish to open.</li>
</ol>
