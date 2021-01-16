def getsum(n):
 sum=0
 for digit in str(n):
   sum+=int(digit)
 return(sum)
n=12345
print(getsum(n))
rev=0
while(n>0):
 dig=n%10
 rev=rev*10+dig
 n=n//10
 print("reverse of the number:",rev)
