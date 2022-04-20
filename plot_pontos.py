import matplotlib.pyplot as plt
import sys
import re

file_name = "mapa.osm.txt"
x = list()
y = list()
with open(file_name) as fp:
    for line in fp:
        points = re.findall(r'[-+]?\d+.\d+', line)
        x.append(float(points[1]))
        y.append(float(points[2]))
print(points)
plt.plot(x, y, 'ro')
plt.show()