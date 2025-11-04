def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        # Raising an exception for better error handling
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Initialize a list to store the operation history
history = [] 
MAX_HISTORY = 5 # Limit the number of history items displayed

def get_valid_number(prompt):
    """Function to repeatedly prompt for a valid number input."""
    while True:
        try:
            # Use strip() to remove leading/trailing spaces
            return float(input(prompt).strip()) 
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")

def display_history():
    """Displays the most recent operation history."""
    if not history:
        print("History is empty.")
        return
    
    print("\n--- Recent History ---")
    # Display the last 5 operations (or fewer)
    for i, (op_str, res) in enumerate(history[-MAX_HISTORY:], 1): 
        print(f"[{i}]: {op_str} = {res}")
    print("-------------------------\n")

def main():
    print("✨ Welcome to the Interactive Python Calculator! ✨")
    
    # Mapping choices to the corresponding function and symbol
    operations = {
        '1': ("+", add),
        '2': ("-", subtract),
        '3': ("*", multiply),
        '4': ("/", divide)
    }

    while True:
        print("\n=== Calculator Menu ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("H. Show History")
        print("5. Exit")

        choice = input("Choose an operation (1-5, or H): ").upper().strip()

        if choice == '5':
            print("👋 Goodbye! Calculator exited.")
            break
        
        if choice == 'H':
            display_history()
            continue

        if choice not in operations:
            print("⚠️ Invalid choice. Please try again.")
            continue

        # Get the operation function and symbol
        symbol, operation_func = operations[choice]

        try:
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")
            
            # Perform the calculation
            result = operation_func(num1, num2)

            # Create the operation string for history
            op_string = f"{num1} {symbol} {num2}"

            # Display the result with clearer formatting
            print(f"\n✅ Result of {op_string} is: {result}")
            
            # Add to history
            history.append((op_string, result))

        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            # Handle other potential general errors
            print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()