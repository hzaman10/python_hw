x=input("Enter a value for x : ")
y=input("Enter a value for y : ")

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(int(x)+int(y))
  elif(z=='-'):
    print(int(x)-int(y))
  elif(z=='*'):
    print(int(x)*int(y))
  elif(z=='/'):
    print(int(x)/int(y))
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")