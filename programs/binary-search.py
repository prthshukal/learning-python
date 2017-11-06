s = [1, 4, 6, 8, 11, 14, 15]
n = 11
start = 0
end = len(s)-1
flag = 0

def binary(s, n, start, end):
  # while(start >= 0 and end <= len(s)-1):
  i = (start + end) / 2
  mid = s[i]
  if (n == mid):
    flag = 1
    return flag, i
  elif n < mid:
    end = i - 1
    return binary(s, n, start, end) 
  elif n > mid:
    start = i + 1
    return binary(s, n, start, end)

result = binary(s, n, start, end)

if (result[0] == 1):
  print "Element found at %s"%(result[1])
else:
  print "Element not found"