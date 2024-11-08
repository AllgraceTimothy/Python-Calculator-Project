def product(x, y):
  product = x * y
  print('Product=',product)

def quotient(x, y):
  quotient = x / y
  print('Quotient=',quotient)

def sum(x, y):
  sum = x + y
  print('Sum=',sum)

def difference(x, y):
  difference = x - y
  print('Difference=',difference)

def square(x):
  square = x ** 2
  print('Square=',square)

def square_root(x):
  square_root = x**(1/2)
  print('Square Root=',square_root)

operations = ['1','2','3','4','5','6']

def main():
  while True:
    operation = input("What Operation would you like to carry out Today? \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Squares\n6. SquareRoots\nOption: ").lower()

    if operation not in operations:
      print("Please enter a valid operation.")
      continue

    else:
      x = int(input("X: "))
    if operation not in ['5', '6']:
      y = int(input("Y: "))
    else:
      y = None
    
    if operation == '1':
      sum(x, y)
    elif operation == '2':
      difference(x, y)
    elif operation == '3':
      product(x, y)
    elif operation == '4':
      quotient(x, y)
    elif operation == '5':
      square(x)
    elif operation == '6':
      square_root(x)
    proceed = input("Would you like to carry out another operation? (yes/no)").lower()
    if proceed != 'yes':
      break

if __name__ == '__main__':
  main()
