import math

# Name of file
FILE_NAME = 'input.txt' 
# Number of K clusters
K_CLUSTERS = 2

# Read file and input values into array
with open(FILE_NAME) as f:
    array = [[int(x) for x in line.split()] for line in f]

ARRAY_LEN = len(array)
BIG_NUMBER = math.pow(10, 10)
ITERATIONS = 1000  # Keeps algorithm from looping infinitely

data = [] #Array for new points
centroids = [] #array for centroids

class DataPoint:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def set_x(self, x):
        self.x = x
        
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    
    def get_cluster(self):
        return self.clusterNumber

class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_y(self, y):
        self.y = y
    
    def get_y(self):
        return self.y
    
# Calculate Euclidean distance.
def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + 
                     math.pow((centroidX - dataPointX), 2))

# initialize centroids  
def initialize_centroids():
    for i in range(K_CLUSTERS):
        centroids.append(Centroid(array[i][0], array[i][1]))    
    return


def recalculate_centroids():
    for j in range(K_CLUSTERS):
        totalX = 0.0
        totalY = 0.0
        totalInCluster = 0.0
        
        for k in range(len(data)):
            if(data[k].get_cluster() == j):
                totalX += float(data[k].get_x())
                totalY += float(data[k].get_y())
                totalInCluster += 1.0
        
        if(totalInCluster > 0):
            centroids[j].set_x(totalX / totalInCluster)
            centroids[j].set_y(totalY / totalInCluster)
    
    return

# Add in new data, one at a time, recalculating centroids with each new one.
def initializeDatapoints():
    for i in range(ARRAY_LEN):
        newPoint = DataPoint(array[i][0], array[i][1])
        
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        
        for j in range(K_CLUSTERS):
            distance = get_distance(0, len(array), centroids[j].get_x(), 
                                    centroids[j].get_y())
            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j
        
        newPoint.set_cluster(currentCluster)
        
        data.append(newPoint)
        
        recalculate_centroids()
    
    return

def update_clusters():
    isStillMoving = 0
    
    for i in range(ARRAY_LEN):
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        
        for j in range(K_CLUSTERS):
            distance = get_distance(data[i].get_x(), data[i].get_y(), 
                                    centroids[j].get_x(), centroids[j].get_y())
            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j
        
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
            data[i].set_cluster(currentCluster)
            isStillMoving = 1
    
    return isStillMoving

def kmeans():
    isStillMoving = 1
    count = 0
    
    initialize_centroids()
    initializeDatapoints()
    
    while isStillMoving and count < ITERATIONS:
        recalculate_centroids()
        isStillMoving = update_clusters()
        count += 1
    
    return

def output():
    for j in range(ARRAY_LEN):
        for i in range(K_CLUSTERS):
            if(data[j].get_cluster() == i):
                print data[j].get_x(), data[j].get_y(), i + 1
    

kmeans()
output()

