
newarr = []
def missing(arr):
  for i in range(1,len(arr)+2):
    newarr.append(i)
  for el in newarr:
    if el not in arr:
      print(el)
