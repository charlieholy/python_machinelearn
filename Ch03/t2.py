import trees
a1,a2 = trees.createDataSet()
b1 = trees.splitDataSet(a1,0,1)
print(b1)
c1 = trees.splitDataSet(a1,0,0)
print(c1)