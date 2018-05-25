import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


twi = pd.read_csv('twitter_asthma.csv', low_memory=False)
twi_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
time = twi["rows_doc_created_at"].values

for i in time:
    hour = int(i[11:13])
    for j in range(0,24):
        if hour == j:
            twi_list[j] += 1

x = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00',
    '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
yt = twi_list
plt.figure(figsize=(30,4)) 
plt.plot(x,yt,color = "b",label= 'twitter',linewidth=1) 
plt.plot(x,yt,'ob')
plt.xlabel("Time(s) of day") 
plt.ylabel("Tweet(s)")
plt.title("Asthma Tweets vs Times") 
plt.legend()
plt.show() 
