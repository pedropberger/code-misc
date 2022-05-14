#n=10
#data=[64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]

n=int(input())
data=list(map(float, input().split()))

#print(n)
#print(data)
type(data)


#mean
mean=sum(data)/n
print(mean)

#median
x=0
for i in data:
  x=1+x

data.sort()


num=x/2
num=round(num)
#print(num)
num2 = num - 1
#print(num2)
#print(data[num])
median = (data[num] + data[num2])/2
print(median)

#mode - most dificult without a function
from scipy import stats
print(stats.mode(data)[0][0])
