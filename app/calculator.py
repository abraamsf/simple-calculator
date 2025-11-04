import argparse

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    args = parser.parse_args()

    if args.operation == "add":
        print(add(args.x, args.y))
    elif args.operation == "sub":
        print(subtract(args.x, args.y))
    elif args.operation == "mul":
        print(multiply(args.x, args.y))
    elif args.operation == "div":
        print(divide(args.x, args.y))
