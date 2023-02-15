# This is my vehicle class.
class Vehicle:
    def __init__(self, vehicle_make, vehicle_model):
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
    # I'm not 100% sure these get_vehicle functions actually do anything. The code runs 100% fine without them.
    # In theory I think I understand what they're supposed to do... however I'm not sure how to check if they are
    # actually doing anything in my code.
    def get_vehicle_make(self):
        return self.vehicle_make

    def get_vehicle_model(self):
        return self.vehicle_model

    def set_vehicle_make(self, vehicle_make):
        self.set_vehicle_make = vehicle_make

    def set_vehicle_model(self, vehicle_model):
        self.set_vehicle_model = vehicle_model
    # These display lines spit out a canned statement about the car that was entered. This one actually doesn't do
    # anything, but if I were to put an option 4 for "generic vehicle" or something, these would then be of use.
    def display_vehicle(self):
        print(f'The vehicle make is: {self.set_vehicle_make}\n'
              f'The vehicle model is: {self.set_vehicle_model}')

# This is my car class, the only thing of note here is the super to inherit the functions from the parent, and
# setting all the variables to None. That took me about 5 or 6 hours to figure out. It would run perfectly fine without
# get functions or the init functions, which is how it was running before. When I added the init for the car and the
# truck classes, it was telling me that the variable was undefined. I scoured every place I could find, and eventually
# just figured it out through sheer luck, because nowhere does it say that a variable that you are defining needs
# to be defined...before its defined. It said they were undefined, so I just defined them as none and the code
# worked just fine. Sorry This is a long comment, it was an absolute nightmare, and I spent way too long banging
# my head against this assignment. I had a working code in 30 minutes, and spend 6 hours trying to get these init
# funtions into it.
class Car(Vehicle):
    def __init__(self, car_doors = None):
        super().__init__(vehicle_make = None, vehicle_model = None)
        self.car_doors = car_doors

    def get_car_doors(self):
        return self.car_doors

    def set_car_doors(self, car_doors):
        self.set_car_doors = car_doors

    def display_car(self):
        print(f'The vehicle make is: {self.set_vehicle_make}\n'
              f'The vehicle model is: {self.set_vehicle_model}\n'
              f'The number of doors is: {self.set_car_doors}')

# same thing, but substitute bed length for car doors
class Truck(Vehicle):
    def __init__(self, bed_length = None):
        super().__init__(vehicle_make = None, vehicle_model = None)
        self.bed_length = bed_length

    def get_bed_length(self):
        return self.bed_length

    def set_bed_length(self, bed_length):
        self.set_bed_length = bed_length

    def display_truck(self):
        print(f'The vehicle make is: {self.set_vehicle_make}\n'
              f'The vehicle model is: {self.set_vehicle_model}\n'
              f'The length of the truck bed is: {self.set_bed_length}')

# I made a list here, this is to store the cars until the end when they can be displayed with the goodbye message
# they're appended in the car function. I was going to use a dictionary, but the list was easier, and though it doesn't
# look as nice, I haven't done any lists in the past. Also, I'm not sure how to "append" something to a dictionary
# from an input.
Cars = []
def car_function():
    input_make = input('Enter the make of the car:')
    input_model = input('Enter the model of the car:')
    input_doors = input('Enter the number of doors:')
    new_car = Car()
    new_car.set_vehicle_make(input_make)
    new_car.set_vehicle_model(input_model)
    new_car.set_car_doors(input_doors)
    new_car.display_car()
    Cars.append([new_car.set_vehicle_make,
                 new_car.set_vehicle_model,
                 new_car.set_car_doors])

Trucks = []
def truck_function():
    input_make = input('Enter the make of the truck:')
    input_model = input('Enter the model of the truck:')
    input_length = input('Enter the length of the bed:')
    new_truck = Truck()
    new_truck.set_vehicle_make(input_make)
    new_truck.set_vehicle_model(input_model)
    new_truck.set_bed_length(input_length)
    new_truck.display_truck()
    Trucks.append([new_truck.set_vehicle_make,
                   new_truck.set_vehicle_model,
                   new_truck.set_bed_length])

# my main function, running all the other functions. ifs for the options, else for anything not 1, 2, or 3.
def main():
    x = input('Enter 1, 2, or 3 for the options below...\n'
              '1. Enter a car\n'
              '2. Enter a truck\n'
              '3. Quit\n'
              'Select an option:')

    if x == '1':
        car_function()
        main()

    elif x == '2':
        truck_function()
        main()

    elif x == '3':
        pass

    else:
        print('***INVALID ENTRY***\n'
              'Please enter 1, 2, or 3')
        main()

# a little print list function, to spit out the list that we made with the car and truck entries.
def print_list():
    if Cars == []:
        print('No cars added.')
    else:
        print('You added the following cars\n'
              , Cars)

    if Trucks == []:
        print('No trucks added.')
    else:
        print('You added the following trucks\n'
              , Trucks)
    print('Goodbye!')

main()
print_list()



