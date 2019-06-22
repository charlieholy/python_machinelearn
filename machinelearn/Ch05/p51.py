from numpy import *
import logRegres
dataArr,labelMat = logRegres.loadDataSet()
weights = logRegres.stocGradAscent0(array(dataArr),labelMat)
logRegres.plotBestFit(weights)
weights = logRegres.stocGradAscent1(array(dataArr),labelMat,500)
logRegres.plotBestFit(weights)
logRegres.multiTest()
