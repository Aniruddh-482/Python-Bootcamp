from replit import clear
from art import logo

# Calculator
# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2
# Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'exit' to exit: ")
    if choice == 'y':
      num1 = answer
    elif choice == 'n':
      should_continue = False
      clear()
      calculator()
    elif choice == 'exit':
      return

calculator()
