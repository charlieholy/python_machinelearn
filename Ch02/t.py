import kNN
group,lables = kNN.createDataSet();
b = kNN.classify0([0,0],group,lables,3)
print(b)