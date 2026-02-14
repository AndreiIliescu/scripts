def length_convertor(value, from_unit, to_unit):
    factor = {
        'mm': 0.001,
        'cm': 0.01,
        'dm': 0.1,
        'm': 1,
        'dam': 10,
        'hm': 100,
        'km': 1000,

        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'chain': 20.1168,
        'furlong': 201.168,
        'mile': 1609.344,

        'nautical mile': 1852,
    }

    if from_unit not in factor or to_unit not in factor:
        return 'Invalide unit.'
    return f'{value}{from_unit} converted in {to_unit} is equal to: {value * factor[from_unit] / factor[to_unit]}{to_unit}\n'


def volume_convertor(value, from_unit, to_unit):
    factor = {
        'ml': 0.001,
        'cl': 0.01,
        'dl': 0.1,
        'l': 1,
        'dal': 10,
        'hl': 100,
        'kl': 1000,

        'fl oz': 0.0295735,
        'cup': 0.236588,
        'pint': 0.473176,
        'quart': 0.946353,
        'gal': 3.78541,
        'bbl': 158.987,
        'dry gal': 4.40488,
    }

    if from_unit not in factor or to_unit not in factor:
        return 'Invalide unit.'
    return f'{value}{from_unit} converted in {to_unit} is equal to: {value * factor[from_unit] / factor[to_unit]}{to_unit}\n'


def mass_convertor(value, from_unit, to_unit):
    factor = {
        'mg': 0.001,
        'cg': 0.01,
        'dg': 0.1,
        'g': 1,
        'dag': 10,
        'hg': 100,
        'kg': 1000,
        'q': 100_000,
        't': 1_000_000,

        'oz': 28.3495,
        'lb': 453.592,
        'stone': 6350.29,
    }

    if from_unit not in factor or to_unit not in factor:
        return 'Invalide unit.'
    return f'{value}{from_unit} converted in {to_unit} is equal to: {value * factor[from_unit] / factor[to_unit]}{to_unit}\n'


def main():
    user_input = input('Chose an option (length, volume or mass): ').lower()
    match user_input:
        case 'length':
            value_input = float(input('Enter the value you want to convert: '))
            from_unit_input = input('Enter the unit from witch you want to convert: ').lower()
            to_unit_input = input('Enter the unit to witch you want to convert: ').lower()
            print(length_convertor(value_input, from_unit_input, to_unit_input))

        case 'volume':
            value_input = float(input('Enter the value you want to convert: '))
            from_unit_input = input('Enter the unit from witch you want to convert: ').lower()
            to_unit_input = input('Enter the unit to witch you want to convert: ').lower()
            print(volume_convertor(value_input, from_unit_input, to_unit_input))

        case 'mass':
            value_input = float(input('Enter the value you want to convert: '))
            from_unit_input = input('Enter the unit from witch you want to convert: ').lower()
            to_unit_input = input('Enter the unit to witch you want to convert: ').lower()
            print(mass_convertor(value_input, from_unit_input, to_unit_input))

        case _:
            print('Invalide option. Try again!')


if __name__ == '__main__':
    main()
