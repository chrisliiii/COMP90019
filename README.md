# COMP90019 Asthma Analytics Project
This is for COMP90019 distributed computing project.
It starts from data collection from Twitter and Instagram and store each data into CouchDB. Then map and charts are used for data visualization. 

# Data Crawling
```sh
$ python streaming_twitter.py [<GEOBOX>] > <json_in_file_path>

$ python search_twitter.py <json_in_file_path> <out_file_path>
```

# Data Storage
```sh
$ python cdb.py <db_name> <out_file_path>
```
Default admin name and password: admin, 123456

# Data Visualization
This part only includes bubble chart for air quality data and traffic flow data, heatmap for traffic flow data, map for social media data and tweets line chart.
Since pollen data are not public.

For map of social data:
```sh
$ python map_socaildata.py <csv_in_file_path>
```
Twitter_asthma.csv and Instagram_asthma.csv are available to use.
