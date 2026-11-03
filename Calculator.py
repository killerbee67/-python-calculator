def add(a, b):
  return a + b
def multiply(a,b):
    return a * b
def subtract(a,b):
    return a - b
def divide (a,b):
    if b == 0:
        return 'cannot divide by 0'  
    return a/b
while True: 
  a = int(input("first number: "))
  operator = input("operator(+,-,*,/): ")
  b = int(input("second number: "))

  if operator == '+':
    print(add(a,b))
  elif operator == '-':
    print(subtract(a,b))
  elif operator == '*':
    print(multiply(a,b))
  elif operator == '/':
    print(divide(a,b))
  else :
    print('invalid operator inputed')
  again = input('Again ? yes | no: ' )
  if again == 'yes':
      print ('restarting……')
  else:
      break
