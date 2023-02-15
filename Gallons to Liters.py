def main():
    intro()

    #calling get_units
    try:
        get_units()

    #My except statement includes a little line to let the user know why it failed.
    except:
        print('An error occured, please try again.\n'
              'Your input can only include whole numbers or decimals.')
        print()
        main()

#['%.2f' % liters] will round to the second decimal point. It helps readability.
def gallons_to_liters(gallons):
    liters = gallons * 3.875
    print(gallons , 'gallons is' , "%.2f" % liters , 'liters.')
#same, but cups
def cups_to_ounces(cups):
    ounces = cups * 8
    print(cups , 'cups is' , '%.2f' % ounces , 'ounces.')

def ounces_to_cups(ounces):
    cups = ounces/8
    print(ounces , 'ounces is' , '%.2f' % cups , 'cups.')

def liters_to_gallons(liters):
    gallons = liters/3.875
    print(liters , 'liters is' , '%.2f' % gallons, 'gallons.')

#I formatted this a little differently so that my wall of text would be broken up a little bit.
def intro():
    print('-Hello, this program will convert gallons to liters.\n'
          'Or this program will convert cups to ounces.\n'
          'Conversion rates:\n'
          '     1 cup = 8 ounces\n'
          '     1 gallon = 3.875 liters')

#This is where things started to get out of hand. I didn't like doing the conversions consecutively
#so this function will ask to choose a conversion, before continuing.
def get_units():
    units = input('What would you like to convert today?\n'
                  '1. Cups to ounces.\n'
                  '2. Gallons to liters.\n'
                  '3. Ounces to cups.\n'
                  '4. Liters to gallons.\n'
                  'Select an option:')

#I put a couple of options in here for an input, so that the program would be more adaptable.
    if units == ('1') or units == ('cups'):
        cups_needed = float(input('Number of cups:'))
        cups_to_ounces(cups_needed)

    elif units == ('2') or units == ('gallons'):
        gallons_needed = float(input('Number of gallons:'))
        gallons_to_liters(gallons_needed)

    elif units == ('3') or units == ('ounces'):
        ounces_needed = float(input('Number of ounces:'))
        ounces_to_cups(ounces_needed)

    elif units == ('4') or units == ('liters'):
        liters_needed = float(input('Number of liters:'))
        liters_to_gallons(liters_needed)

#this else is working as a catch for anything that isn't 1 or 2. I added a bunch of stars and a line break because
#it was pretty tough to find it when it popped up, and I want it to be obvious.
    else:
        print("***That isn't a valid input.***\n")
        main()

#This function allows the user to do multiple consecutive conversions.
#This could probably be pretty easily converted into a function that will repeat
#any program you would like to repeat.
def convert_again():
    print('Would you like to convert another value?')
    x = input("Y/N:")

    if x == ('y') or x == ('Y'):
        main()
        convert_again()

    elif x == ('n') or x == ('N'):
        print('Goodbye.')

    else:
        print('Please enter y for yes, or n for no.')
        convert_again()

main()
convert_again()
