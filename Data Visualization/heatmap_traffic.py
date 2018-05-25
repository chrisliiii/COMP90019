from gmplot import gmplot
import pandas as pd
import numpy as np
import json
from gmplot import gmplot


# Place map
gmap = gmplot.GoogleMapPlotter(-37.8136,144.9631, 9)

twi = pd.read_csv('traffic.csv')

lats = twi['MIDPNT_LAT'].values
lons = twi['MIDPNT_LON'].values

lats = lats[np.logical_not(np.isnan(lats))]
lons = lons[np.logical_not(np.isnan(lons))]

gmap.heatmap(lats,lons)

gmap.draw("traffic_heatmap.html")
