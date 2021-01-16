def reverse(s):
 str=""
 for i in s:
  str=i+str
 return str
s="pythontraining"
print("the original stringis:",end="")
print(s)
print("The reversed string(using loops)is:",end="")
print(reverse(s))
