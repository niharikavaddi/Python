hr1,min1=[int(x) for x in input().split()]
hr2,min2=[int(x) for x in input().split()]
if hr2>hr1 and min2>=min1:
  print(hr2-hr1,min2-min1)
elif hr2>hr1 and min1>=min2:
  print(hr2-hr1,min1-min2)
elif hr1>hr2 and min1>=min2:
  print(hr1-hr2,min1-min2)
elif hr1>hr2 and min2>=min1:
  print(hr1-hr2,min2-min1)
