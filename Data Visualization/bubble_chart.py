import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


twi_valu = [100, 100, 100, 300, 100, 100, 100, 100, 200, 300, 100, 100, 300, 100, 100, 200, 100, 300, 300, 700, 100, 100]
tr_valu = [5950.0, 12138.08695652174, 6714.285714285715, 10926.829268292682, 8323.076923076924, 7634.782608695652, 11859.09090909091, 24001.639344262294, 11497.560975609756, 9014.814814814816, 5150.0, 10017.0, 7543.90243902439, 10234.896551724138, 7564.285714285715, 11907.017543859649, 8125.909090909091, 10144.444444444445, 14197.263157894737, 10865.432098765432, 9390.413793103447, 12036.923076923076]
air_valu = [51.466316596814735, 46.98444424703679, 51.70371296359616, 48.62468675520485, 48.40920958948554, 50.737191151515184, 47.305929432789355, 48.53334704147819, 48.25999201321427, 48.24650638020838, 48.38617544415206, 45.738686270022896, 53.79654395604396, 46.96926168450683, 49.321017842323656, 47.51319420254403, 51.29279305555556, 48.78472228235594, 49.82282663964333, 51.04928482579502, 49.311718240620955, 46.137562302158294]
province = ['Brighton', 'Prahran', 'Beaumaris', 'McKinnon', 'SouthMelbourne', 'CaulfieldNorth', 'Caulfield\nEast', 'SouthYarra', 'Southbank', 'WestMelbourne', 'Richmond', 'Toorak', 'Northcote', 'NorthMelbourne', 'HawthornEast', 'Cheltenham', 'StKilda', 'Parkville', 'Bentleigh', 'Hawthorn', 'GlenIris', 'Carlton']

N=22

# Choose some random colors
colors=cm.rainbow(np.random.rand(N))

# Use those colors as the color argument
plt.scatter(air_valu,tr_valu,s=twi_valu,color=colors)
for i in range(N):
    plt.annotate(province[i],xy=(air_valu[i],tr_valu[i]),fontsize= 8)
plt.xlabel('Air pollution index (AirBeam-PM (μg/m³))')
plt.ylabel('Average Daily traffic volume')

# Move title up with the "y" option
plt.title('Relationship between the number of tweets and air index and traffic flow',y=1.05)
plt.show()
