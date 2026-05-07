import logging

# ---------------- CONFIGURE LOGGING ----------------
logging.basicConfig(
    filename="app.log",
    filemode="a",                      # append logs
    level=logging.DEBUG,               # log everything
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ---------------- ARITHMETIC FUNCTIONS ----------------
def add(a, b):
    result = a + b
    logging.info(f"ADD: {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logging.info(f"SUBTRACT: {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    logging.info(f"MULTIPLY: {a} * {b} = {result}")
    return result

def divide(a, b):
    try:
        result = a / b
        logging.info(f"DIVIDE: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("DIVISION ERROR: Attempted to divide by zero")
        return "Error: Cannot divide by zero"

# ---------------- MAIN PROGRAM ----------------
def arithmetic_app():
    logging.info("PROGRAM STARTED")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        logging.debug(f"User input → a={a}, b={b}, operation='{op}'")

        if op == "+":
            print("Result:", add(a, b))
        elif op == "-":
            print("Result:", subtract(a, b))
        elif op == "*":
            print("Result:", multiply(a, b))
        elif op == "/":
            print("Result:", divide(a, b))
        else:
            print("Invalid operation")
            logging.warning(f"Invalid operation entered: {op}")

    except ValueError:
        logging.error("INPUT ERROR: User entered non-numeric value")
        print("Please enter valid numbers")

    logging.info("PROGRAM ENDED")


# Run the app
arithmetic_app()
