def add (num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


def subtraction(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"


def multiplication(num1, num2):
    return f"{num1} * {num2} = {num1 * num2}"


def division(num1, num2):
    try:
        return f"{num1} / {num2} = {num1 / num2}"
    except ZeroDivisionError:
        return "ERROR !!! You can't divide a number by zero."


def raising_to_power(num1, power):
    return f"{num1} to the power of {power} is {num1 ** power}"


def main():
    user_input = input("Select an operation ('+', '-', '*', '/', '**'): ")
    num1_input = float(input("Enter the 1st number: "))
    num2_input = float(input("Enter the 2nd number: "))
    match user_input:
        case "+":
            print(add(num1_input, num2_input))

        case "-":
            print(subtraction(num1_input, num2_input))

        case "*":
            print(multiplication(num1_input, num2_input))

        case "/":
            print(division(num1_input, num2_input))

        case "**":
            power_input = float(input("Enter the power you want to raise the number: "))
            print(raising_to_power(num1_input, power_input))

        case _:
            print("Invalid option input. Try again!")


if __name__ == "__main__":
    main()
