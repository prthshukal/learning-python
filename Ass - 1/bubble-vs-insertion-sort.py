import time

sort = [218, 782, 356, 729, 792, 971, 98, 798, 846, 212, 627, 185, 944, 419, 499, 196, 505, 835, 125, 408, 510, 945, 563, 430, 666, 793, 825, 387, 934, 957, 592, 344, 319, 587, 695, 315, 832, 692, 362, 393, 843, 232, 856, 533, 811, 392, 741, 946, 869, 219, 336, 828, 126, 202, 489, 368, 131, 892, 615, 394, 840, 776, 770, 701, 407, 259, 530, 603, 794, 925, 301, 153, 822, 255, 557, 862, 291, 394, 505, 557, 785, 298, 536, 402, 939, 697, 94, 590, 866, 345, 499, 142, 759, 381, 753, 890, 886, 684, 795, 965, 822, 318, 91, 506, 327, 333, 681, 204, 358, 208, 654, 566, 966, 338, 149, 91, 565, 423, 45, 961, 833, 333, 994, 284, 740, 870, 932, 592, 373, 44, 666, 413, 582, 780, 837, 864, 342, 26, 904, 735, 309, 132, 689, 630, 569, 701, 740, 151, 61, 617, 739, 751, 289, 653, 97, 332, 879, 834, 650, 641, 694, 857, 668, 444, 333, 680, 152, 80, 80, 305, 185, 181, 41, 489, 351, 889, 272, 477, 559, 807, 834, 598, 392, 456, 49, 835, 247, 301, 436, 646, 18, 486, 985, 379, 994, 580, 739, 995, 351, 711]

start_bubble = time.time()
def bubble(sort):
  
  for b in range(0, len(sort)-1, ):
    for i in range(0, len(sort)-1):
      if sort[i] > sort[i+1]:
        temp = sort[i]
        sort[i] = sort[i+1]
        sort[i+1] = temp
    
bubble(sort)
print "Bubble Sort"
print sort
print ("Bubble sort takes %s seconds" % (time.time() - start_bubble))
print

start_insertion = time.time()
def insertion(sort):
  for j in range(1, len(sort)):
    key = sort[j]
    i = j-1
    while (i >= 0 and sort[i] > key):
      sort[i+1] = sort[i]
      i = i - 1
      sort[i+1] = key
     
insertion(sort)
print "Insertion Sort"
print sort
print ("Insertion sort takes %s seconds" % (time.time() - start_insertion))


# import time

# sort = [218, 782, 356, 729, 792, 971, 98, 798, 846, 212, 627, 185, 944, 419, 499, 196, 505, 835, 125, 408, 510, 945, 563, 430, 666, 793, 825, 387, 934, 957, 592, 344, 319, 587, 695, 315, 832, 692, 362, 393, 843, 232, 856, 533, 811, 392, 741, 946, 869, 219, 336, 828, 126, 202, 489, 368, 131, 892, 615, 394, 840, 776, 770, 701, 407, 259, 530, 603, 794, 925, 301, 153, 822, 255, 557, 862, 291, 394, 505, 557, 785, 298, 536, 402, 939, 697, 94, 590, 866, 345, 499, 142, 759, 381, 753, 890, 886, 684, 795, 965, 822, 318, 91, 506, 327, 333, 681, 204, 358, 208, 654, 566, 966, 338, 149, 91, 565, 423, 45, 961, 833, 333, 994, 284, 740, 870, 932, 592, 373, 44, 666, 413, 582, 780, 837, 864, 342, 26, 904, 735, 309, 132, 689, 630, 569, 701, 740, 151, 61, 617, 739, 751, 289, 653, 97, 332, 879, 834, 650, 641, 694, 857, 668, 444, 333, 680, 152, 80, 80, 305, 185, 181, 41, 489, 351, 889, 272, 477, 559, 807, 834, 598, 392, 456, 49, 835, 247, 301, 436, 646, 18, 486, 985, 379, 994, 580, 739, 995, 351, 711]

# start_bubble = time.time()
# def bubble(sort):
  
#   for b in range(0, len(sort)):    #tera ye loop ka use hi nhi ho rha tha...code galat nhi h.....your code was working very correct, but time bohot zyada aarha tha......compare kar tera pehle wala code and maine jo ye abi likha h usko......also ye jo maine likha h wo ek baar pen paper se run karke dekh...u will know the difference
#     for i in range(b+1, len(sort)):   #this is also changed in reference of the above loop
#       if sort[b]  > sort[i]:
#         sort[b],sort[i] = sort[i], sort[b]  #this is a shortcut to swap two values in Python, instead of using a 3rd variable

    
# bubble(sort)
# print "Bubble Sort"
# print sort
# print ("Bubble sort takes %s seconds" % (time.time() - start_bubble))
# print

# start_insertion = time.time()
# def insertion(sort):
#   for j in range(1, len(sort)):
#     key = sort[j]
#     i = j-1
#     while (i >= 0 and sort[i] > key):
#       sort[i+1] = sort[i]
#       i = i - 1
#       sort[i+1] = key
     
# insertion(sort)
# print "Insertion Sort"
# print sort
# print ("Insertion sort takes %s seconds" % (time.time() - start_insertion))
