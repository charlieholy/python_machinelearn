import  logRegres
from numpy import  *
a1,a2 = logRegres.loadDataSet()
#print(a1)
#print(a2)
b1 = logRegres.gradAscent(a1,a2)
print(b1.getA())
logRegres.plotBestFit(b1.getA())    ###perfect

#c1 = logRegres.stocGradAscent1(array(a1),a2)
#logRegres.plotBestFit(c1)