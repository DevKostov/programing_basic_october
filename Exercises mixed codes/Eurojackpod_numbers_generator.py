import random
from datetime import datetime


def generate_euro_numbers():
    """ Generate numbers fitting the euro lottery draw """
    main_numbers = range(1, 50 + 1)
    super_numbers = range(1, 12 + 1)

    random_main_numbers = sorted(random.sample(main_numbers, 5))
    random_super_numbers = sorted(random.sample(super_numbers, 2))
    return random_main_numbers, random_super_numbers


def generate_lotto_numbers():
    """ Generate numbers fitting the 6from49 lottery draw """
    main_numbers = range(1, 49 + 1)

    random_main_numbers_lotto = sorted(random.sample(main_numbers, 6))
    return random_main_numbers_lotto

def generate_lotto_string(lotto=None, euro=None):
    """ Constructs standard string form for lotto and euro numbers
    lotto: List of lotto numbers
    euro: Tuple of two lists of euro and super numbers
    """
    if not lotto and not euro:
        return ''

    lotto_name = 'Lotto 6from49'
    euro_name_1 = 'Eurojackpot Numbers'
    euro_name_2 = 'Eurojackpot Euronumbers'

    date = datetime.now()
    date_format = date.strftime('%d-%m-%Y %H:%M:%S')
    coder = 'Dev.Kostov'

    def to_str_list(arg):
        """
        Convert list to comma separated string
        """
        return ", ".join(map(str, arg))

    out_string = ''
    if lotto:
        out_string += f'{lotto_name}: {to_str_list(lotto)}\n'

    if euro:
        out_string += f'{euro_name_1}: {to_str_list(euro[0])}\n'
        out_string += f'{euro_name_2}: {to_str_list(euro[1])}\n'

    out_string += f'\nGenerated on: {date_format} by {coder}'
    return out_string


def output_numbers(filename=None, lotto=None, euro=None):
    """
    Output lotto and euro numbers either to screen (if no filename) or to filename if provided
    """
    if not filename:
        print(generate_lotto_string(lotto, euro))
    else:
        with open(filename, 'w+') as out_file:
            out_file.writelines(generate_lotto_string(lotto, euro))


if __name__ == '__main__':
    import sys

    LOTTO, EURO = None, None
    # Default to printing to screen
    OUT_FILE = None

    # Naively assume arg 1 is filename (arg[0] is the filename)
    if len(sys.argv) > 1 and sys.argv[1] not in ('lotto', 'euro'):
        OUT_FILE = sys.argv.pop(1)  # Set OUT_FILE to user filename and remove from argument list

    if len(sys.argv) == 1:  # Called without other arguments
        LOTTO = generate_lotto_numbers()
        EURO = generate_euro_numbers()
    else:
        for arg in sys.argv[1:]:
            arg = arg.lower()
            if arg == 'lotto':
                LOTTO = generate_lotto_numbers()
            elif arg == 'euro':
                EURO = generate_euro_numbers()
            else:
                raise ValueError(f'Unrecognised option {arg}, must be "lotto" or "euro".')

    output_numbers(OUT_FILE, lotto=LOTTO, euro=EURO)
    print('\nThe text file was created successfully.')


# import random
#
#
# def generate_eurojackpot_numbers():
#     main_numbers = random.sample(range(1, 51), 5)
#     additional_numbers = random.sample(range(1, 11), 2)
#
#     main_numbers.sort()
#     additional_numbers.sort()
#
#     return main_numbers, additional_numbers
#
#
# main, additional = generate_eurojackpot_numbers()
# print("Основни числа:", main)
# print("Допълнителни числа:", additional)
