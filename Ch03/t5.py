import treePlotter
import trees
a1,a2 = trees.createDataSet()
b1 = trees.createTree(a1,a2)
treePlotter.createPlot(b1)