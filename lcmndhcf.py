from math import gcd
def lcm(a):
  res=a[0]
  for i in a[1:]:
    res=int(res*i/gcd(res,i))
  return res
def hcf(a):
  count=0
  hcf=1
  for i in range(1,min(a)+1):
    for j in range(0,len(a)):
      if a[j]%i==0:
        count=count+1
      if count==len(a) and hcf<i:
        hcf=i
    count=0
  return hcf

a=list()
a=[int(x) for x in input().split()]
solution1=lcm(a)
solution2=hcf(a)
print('LCM:',solution1,'HCF:',solution2)
