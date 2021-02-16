import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def plotWithYAxis(yPoints, yLabel, graphTitle, fileName):
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  ax.plot(yPoints)
  
  plt.ylabel(yLabel)
  plt.title(graphTitle)

  fig.savefig('./graphs/graph{}.png'.format(fileName))
  print("Your graph are done! File: graphs/graph{}.png".format(fileName))


def plotGraph(xPoints,x2Points,xLabel,yPoints, y2Points,yLabel,graphTitle, fileName):
  print("\nCreating graph {} ...".format(fileName))
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  ax.plot(xPoints, yPoints)
  ax.plot(x2Points, y2Points)
  plt.xlabel(xLabel)
  plt.ylabel(yLabel)
  plt.title(graphTitle)

  fig.savefig('./graphs/graph{}.png'.format(fileName))
  print("Your graph are done! File: graphs/graph{}.png".format(fileName))

def plotGraphThree(xPoints,x2Points,x3Points,xLabel,yPoints, y2Points,y3Points,yLabel,graphTitle, fileName):
  print("\nCreating graph {} ...".format(fileName))
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  ax.plot(xPoints, yPoints)
  ax.plot(x2Points, y2Points)
  ax.plot(x3Points, y3Points)
  plt.xlabel(xLabel)
  plt.xticks(rotation=35)
  plt.ylabel(yLabel)
  plt.title(graphTitle)

  fig.savefig('./graphs/graph{}.png'.format(fileName))
  print("Your graph are done! File: graphs/graph{}.png".format(fileName))
