import math
sentarr = []
def rev(sentence):
  times = math.ceil(len(sentence)/4)
  l=0
  for i in range(times):
    sentarr.append(sentence[l:l+4])
    l = l + 4
  newsent = ""
  for word in sentarr:
    newsent = newsent + word[::-1]
  print(newsent)
