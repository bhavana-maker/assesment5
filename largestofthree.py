def maximum(a,b,c):
 if(a>=b) and (a>=c):
  largest=a
 elif(b>=a) and(b>=c):
  largest=b
 else:
  largest=c
 return largest
a=int(input("entera a number"))
b=int(input("entera b number"))
c=int(input("entera c number"))
print(maximum(a,b,c))
