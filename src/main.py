dataPath = '../data/iris.csv'
import pandas as pd
import numpy as np
import numpy.linalg as ln
import math

data = pd.read_csv(dataPath)
data = data.sample(frac=1)

l = 0.00004
def createTenSamples():
    lData = math.floor(len(data)/10)
    samples = []
    c = 1
    while(c<len(data)):
        samples.append(data[c:c+lData])
        c = c+lData+1
    return samples

def calculateCorrMatrix(dataSet):
    correlationMatrix = np.zeros((5,5))
    for item in dataSet.values:
        x = []
        for i in item:
            try:
                x.append([float(i)])
            except:
                x.append([1.0])

        x = np.array(x)
        xt = np.transpose(x)
        prod = np.matmul(x,xt)
        correlationMatrix = correlationMatrix+prod
    return correlationMatrix

def calculateYX(dataSet):
    y=[[0,0,0]]
    ss=(y[0][1])
    sum = np.zeros((5,3))
    for item in dataSet.values:
        x = []
        for i in item:
            try:
                x.append([float(i)])
            except:
                if(i=='setosa'):
                    y[0][0] = 1.
                elif(i=='versicolor'):
                    y[0][1] = 1.
                else:
                    y[0][2] = 1.
                x.append([1.0])
        temp = np.copy(y)
        y = [[0,0,0]]
        sum = sum+ np.matmul(x,temp)
    return sum


def calculateWeightMatrix(dataSet):
    cMatrix = calculateCorrMatrix(dataSet)
    interim = cMatrix+l
    t = ln.inv(np.array(interim))
    y = calculateYX(dataSet)
    w=np.matmul(t,y)
    print(w)
    item = (samleData[9].values[0,0:5])
    print(item)
    x = []
    for i in item:
        try:
            x.append([float(i)])
        except:
            x.append([1.0])
    print(np.matmul(np.transpose(w),x))
samleData = createTenSamples()
#print(samleData[9])
calculateWeightMatrix(samleData[0])
