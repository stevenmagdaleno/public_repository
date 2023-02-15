# defined the main function, to get input, then stk.upper() for formatting, so lower or uppercase inputs
# would work. except main() to push user back to the beginning if they screw it up.

def main():
    try:
        stk = input("Search stock prices by stock ticker symbol:")
        stk = stk.upper()
        output = stocks[stk]
        print(stk,"is currently worth $",output)

    except:
        KeyError
        print("We don't have information on that stock.\n"
              "You can try a different stock if you'd like.\n")
        main()

# adapted from last week's "convert_again()" this will just run the program multiple times with a y/n to quit.

def stocks_again():
    print('Would you like to look up another stock?')
    x = input("Y/N:")

    if x == ('y') or x == ('Y'):
        main()
        stocks_again()

    elif x == ('n') or x == ('N'):
        print('Goodbye.')

    else:
        print('Please enter y for yes, or n for no.')
        stocks_again()

# my dictionary with completely made up information.

stocks = {
    "AAL": 5,
    "AAU": 7,
    "GLE": 8,
    "APP": 65,
    "TWO": 44,
    "MAP": 12,
    "DRO": 4,
    "TOP": 33,
    "SKE": 5,
    "ALW": 44,
    "PTW": 100
}

# calling my functions
main()
stocks_again()

# I also started playing around with dictionaries, and trying some other stuff that might work better in the future.
# i think this is a bit beyond my skill level, but fun none the less
# deep_stocks = {
#     "s1": {
#         "ticker": "AAL",
#         "long_name": "American Airlines",
#         "price": 5,
#     },
#     "s2": {
#         "ticker": "AAU",
#         "long_name": "Almaden Minerals",
#         "price": 7,
#     }
# }
