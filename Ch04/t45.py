import  bayes
import feedparser
ny = feedparser.parse('https://newyork.craigslist.org/search/stp?format=rss')
aa = ny['entries']
print(aa)
#bayes.spamTest()
bb = len(aa)
print(bb)
sf = feedparser.parse('https://sfbay.craigslist.org/search/stp?format=rss')
bayes.getTopWords(ny,sf)