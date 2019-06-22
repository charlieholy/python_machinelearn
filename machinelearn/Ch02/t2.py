import matplotlib
import matplotlib.pyplot as plt
import kNN
fig = plt.figure()
ax = fig.add_subplot(111)

datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
#print(datingDataMat)
#print(datingLabels)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
plt.show()