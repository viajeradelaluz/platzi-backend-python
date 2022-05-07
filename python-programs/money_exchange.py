#!/usr/bin/python3
""" Money Exchange:

    Convert your local currency (Colombian, Mexican 
    or Argentine Pesos) to dollars.
    """


def money_exchange(option):

    if option == 1:
        currency = 'Colombian'
        exchange_rate = 3973
    elif option == 2:
        currency = 'Mexican'
        exchange_rate = 21
    elif option == 3:
        currency = 'Argentine'
        exchange_rate = 106
    else:
        money_exchange(int(input("Select a valid option >> ")))

    amount = int((input(f"{currency} Pesos Amount: ")))
    dolar = str(round(amount / exchange_rate, 2))
    print(f"--> ${dolar} USD")
    exit()


# Entry point
if __name__ == "__main__":
    menu = """
    +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
··· |M|o|n|e|y| |E|x|c|h|a|n|g|e| ···
    +-+-+-+-+-+ +-+-+-+-+-+-+-+-+

I want to convert from:
    [1] - Colombian Peso (COP)
    [2] - Mexican Peso (MXN)
    [3] - Argentine Peso (ARS)
>> """

    OPTION = int(input(menu))
    money_exchange(OPTION)
