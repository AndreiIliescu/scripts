from currency_converter import CurrencyConverter


c = CurrencyConverter()

def currency_convertor(amount, from_currency, to_currency):
    return c.convert(amount, from_currency, to_currency)


amount_input = float(input("Enter the amount you want to convert: "))
from_currency_input = input("Enter the currency you want to convert from: ").upper()
to_currency_input = input("Enter the currency you want to convert to: ").upper()

result = round(currency_convertor(amount_input, from_currency_input, to_currency_input), 2)
print(f"{amount_input} {from_currency_input} converted to {to_currency_input} is: {result} {to_currency_input}")
