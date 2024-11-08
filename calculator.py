def product(x, y):
  product = round(x * y, 4)
  print('Product=',product)

def quotient(x, y):
  quotient = round(x / y, 4)
  print('Quotient=',quotient)

def sum(x, y):
  sum = round(x + y, 4)
  print('Sum=',sum)

def difference(x, y):
  difference = round(x - y, 4)
  print('Difference=',difference)

def square(x):
  square = round(x ** 2, 4)
  print('Square=',square)

def square_root(x):
  square_root = round(x**(1/2), 4)
  print('Square Root=',square_root)

operations = ['1','2','3','4','5','6']

def main():
  while True:
    operation = input("What Operation would you like to carry out Today? \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Squares\n6. SquareRoots\nOption: ").lower()

    if operation not in operations:
      print("Please enter a valid operation.")
      continue

    else:
      x = float(input("X: "))
    if operation not in ['5', '6']:
      y = float(input("Y: "))
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
