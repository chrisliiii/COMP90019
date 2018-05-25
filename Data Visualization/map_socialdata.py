import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import json


def isInsidePolygon(pt, poly):
    c = False
    i = -1
    l = len(poly)
    j = l - 1
    while i < l - 1:
        i += 1
        if ((poly[i][1] <= pt[0] and pt[0] < poly[j][1]) or (
                poly[j][1] <= pt[0] and pt[0] < poly[i][1])):
            if (pt[1] < (poly[j][0] - poly[i][0]) * (pt[0] - poly[i][1]) / (
                    poly[j][1] - poly[i][1]) + poly[i][0]):
                c = not c
        j = i
    return c


def lats_lons(file):
    data = pd.read_csv(file,low_memory=False)

    lats = data['rows_doc_coordinates_coordinates_1'].values
    lons = data['rows_doc_coordinates_coordinates_0'].values

    lats = lats[np.logical_not(np.isnan(lats))]
    lons = lons[np.logical_not(np.isnan(lons))]
    return lats,lons


def dic_suburb(lats,lons):
    dic = {}
    with open("vic_polygon.json") as f:
        for line in f:
            line = line.rpartition("}")[0] + "}"
            data = json.loads(line)
            co = data["geometry"]["coordinates"]
            count = 0
            if len(co) == 1:
                for i in range(0, len(lats)):
                    if isInsidePolygon(([lats[i], lons[i]]), co[0]):
                        count += 1
            name = data["properties"]["Suburb_Name"]
            if count != 0:
                dic[name] = count
     return dic


if __name__ == "__main__":

    if len(sys.argv) != 1:
        print("\nUsage: python map_socaildata.py <csv_in_file_path> \n")
    else:
        file = sys.argv[1]
        
    fig, ax = plt.subplots(figsize=(10,10))
    lats,lons = lats_lons(file)
    dic = dic_suburb(lats,lons)

    m = Basemap(projection = 'mill',
                llcrnrlat=-39,
                llcrnrlon=143,
                urcrnrlat=-37,
                urcrnrlon=146,
                resolution = 'l')

    m.drawmapboundary(fill_color='peachpuff')
    m.readshapefile('viclocalitypolygonshp/VIC_LOCALITY_POLYGON_shp', 'VIC')

    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []

    for info, shape in zip(m.VIC_info, m.VIC):
        for key in dic:
            if info["VIC_LOCA_2"] == key.upper():
                if 0 < dic[key] <= 10:
                    p1.append(Polygon(np.array(shape), True))
                elif 10 < dic[key] <= 50:
                    p2.append(Polygon(np.array(shape), True))
                elif 50 < dic[key] <= 100:
                    p3.append(Polygon(np.array(shape), True))
                elif 100 < dic[key] <= 1000:
                    p4.append(Polygon(np.array(shape), True))
                elif 1000 < dic[key] <= 2000:
                    p5.append(Polygon(np.array(shape), True))


    ax.add_collection(PatchCollection(p1, facecolor='mistyrose', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(p2, facecolor='lightsalmon', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(p3, facecolor='tomato', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(p4, facecolor='orangered', edgecolor='k', linewidths=1., zorder=2))
    ax.add_collection(PatchCollection(p5, facecolor='red', edgecolor='k', linewidths=1., zorder=2))


    plt.title('asthma social data location')
    plt.show()
