import couchdb
import time
import json
import sys
import pandas as pd


def m_int(month):
    if month == "Jan":
        return 1
    elif month == "Feb":
        return 2
    elif month == "Mar":
        return 3
    elif month == "Api":
        return 4
    elif month == "May":
        return 5
    elif month == "Jun":
        return 6
    elif month == "Jul":
        return 7
    elif month == "Aug":
        return 8
    elif month == "Sep":
        return 9
    elif month == "Oct":
        return 10
    elif month == "Nov":
        return 11
    elif month == "Dec":
        return 12

def ast_relat(data):
    list = ["asthma", "cough", "difficulty breath", "cant breath", "wheezing", "rapid breath", "shortness of breath",
    "short of breath", "chest pain", "chest tight", "sneeze", "respiratory infection", "difficult breath", "can't breath",
    "asthma attack", "pale face", "throat irritation", "breathless", "inhaler", "blue lips", "blue fingernails"]

    if data["text"] is not None:
        text = data["text"]
        for i in list:
            if i in text:
                ast = "Yes"
                return ast
        ast = "No"
        return ast


def key_db(data):
    year = int(data["created_at"][-4:])
    mon = data["created_at"][4:7]
    month = m_int(mon)
    day = int(data["created_at"][8:10])
    key = ["Melbourne", year, month, day]
    return key


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

def ld_data(line):
    line = line.rpartition("}")[0] + "}"
    data = json.loads(line)
    return data


def sub_def(lat, lon):
    with open("vic_polygon.json") as f:
        for line in f:
            data = ld_data(line)
            co = data["geometry"]["coordinates"]
            if len(co) == 1:
                if isInsidePolygon(([lat, lon]), co[0]):
                    name = data["properties"]["Suburb_Name"]
                    return name


def format_data(line):
    if len(line) > 2:
        data = ld_data(line)
        adoc = data
        adoc["_id"] = data["id_str"]
        key = key_db(data)
        adoc["key"] = key
        a = ast_relat(data)
        adoc["related_asthma"] = a
        if data["geo"] is not None:
            co = data["geo"]["coordinates"]
            adoc["suburb"] = sub_def(co[0], co[1])
        else:
            adoc["suburb"] = "null"
        return adoc


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("\nUsage: python cdb.py <db_name> <out_file_path>\n")
    else:
        dbname = sys.argv[1]
        file = sys.argv[2]

        server = couchdb.Server("http://127.0.0.1:5984")

        # Set credentials if necessary
        server.resource.credentials = ("admin", "123456")

        # create db if necessary
        if dbname not in server:
            server.create(dbname)
        db = server[dbname]

        # store data in couchdb
        with open(file) as f:
            for line in f:
                if len(line) > 2:
                    adoc = format_data(line)
                    try:
                        db.save(adoc)
                        time.sleep(1.5)
                    except:
                       continue
