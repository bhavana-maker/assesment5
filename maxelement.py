def mymax(list):
 max=list[0]
 for x in list:
  if x>max:
    max=x
 return max
list=[10,60,90,8,40]
print("largest element is:",mymax(list))
