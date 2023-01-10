def FindIntersection(strArr):

  # loop both the arrays at the same time with 2 indexes, moving up in each as the values compare
  a=[int(s) for s in strArr[0].split(',')]
  b=[int(s) for s in strArr[1].split(',')]

  ai = 0
  bi = 0

  res = ""
  while ai < len(a) and bi < len(b):
    if a[ai] == b[bi]:
      if res:
        res = res + ","
      res = res + str(a[ai])
      ai = ai + 1
      bi = bi + 1
    elif a[ai] < b[bi]:
      ai = ai + 1
    else:
      bi = bi + 1

  # code goes here
  return res

# keep this function call here 
print(FindIntersection(input()))