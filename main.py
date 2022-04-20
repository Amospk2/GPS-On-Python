
from dis import dis
import math
import matplotlib.pyplot as plt
from grafo import Graph
from haversine import haversine
import re


g = Graph()
control_click = []

def get_cost(x1, x2):
  x1 = g.get_vertex(x1)
  x2 = g.get_vertex(x2)
  return haversine([x1.latitude, x1.longitude], [x2.latitude, x2.longitude])

with open("map.osm.txt") as fp: #le o arquivo e adiciona ao grafo
    for line in fp:
      points = re.findall(r'[-+]?\d+.\d+', line)
      g.add_vertex(points[0], float(points[1]), float(points[2]))
    
with open("uesb.adjlist") as file: #adiciona as ligações ao grafo
  for line in file:
    points = re.findall(r'[-+]?\d+', line)
    print(line)
    for index in range(len(points) - 1):
      g.add_edge(points[0], points[index+1], get_cost(points[0], points[index+1]))



def connectpoints(x1, x2):
    pass

def get_caminho(x1, x2):
	pass
    


def mouse_event(event):
    print('x: {} and y: {}'.format(event.xdata, event.ydata))
    
    pass

    

fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)



def plot():
  x = list()
  y = list()
  for elemento in g.get_edges():
    elemento = g.get_vertex(elemento[0])
    x.append(elemento.latitude)
    y.append(elemento.longitude)

  plt.plot(x, y, 'ro')


plot()
plt.show()






      
