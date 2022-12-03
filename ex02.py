last=1
pen=0
num=0
sum =0
while num<4000000:
    num=last+pen 
    print(num)
    pen=last
    last=num
    if num//2==num/2:
        sum = sum + num
print(sum)