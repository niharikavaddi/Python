import statistics
array=list()
num=int(input())
array=(int(x) for x in input().split())
array=sorted(array)
print(statistics.median(array))
#if len(array)%2!=0:
 # print(array[int((len(array)/2)-0.5)])
#else:
 # print(((array[int((len(array)/2))])+(array[int((len(array)/2)-1)]))/2)
