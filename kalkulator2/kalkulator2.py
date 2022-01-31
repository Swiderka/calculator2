import logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
  logging.info(f"Dodaje: {a} i {b}.")
  return a + b 
def sub(a, b ):
  logging.info(f"Odejmuje: od {a} odejmuje {b}.")
  return a - b 
def multi(a, b ):
  logging.info(f"Mnoze: {a} z {b}.")
  return a * b
def div(a, b ):
  logging.info(f"Dziele: {a} przez {b}.")
  return a / b

operations = {
    "1": add,
    "2": sub,
    "3": multi,
    "4": div
}

def get_data():
    a = float(input("Podaj skladnik 1:"))
    b = float(input("Podaj skladnik 2:"))
    return operations, a, b

def calculator():
    operations, a, b = get_data()
    result = operations[op](a, b)


# def calculator(a, b, action):
#     if operations == 1:
#         return add(a, b)
#     elif operations == 2:
#         return sub(a, b)
#     elif operations == 3:
#         return multi(a, b)
#     elif operations == 4:
#         return div(a, b)
#     else:
#         return ValueError

if __name__ == "__main__":
    action = int(input("Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie:"))
    print(f"Wynik to: {calculator(get_data())}")

