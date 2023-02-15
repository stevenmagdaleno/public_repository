class Vehicle:
    def __init__(self, vehicle_make, vehicle_model):
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model

    def get_vehicle_make(self):
        return self.vehicle_make

    def get_vehicle_model(self):
        return self.vehicle_model

    def set_vehicle_make(self, vehicle_make):
        self.set_vehicle_make = vehicle_make

    def set_vehicle_model(self, vehicle_model):
        self.set_vehicle_model = vehicle_model

    def display_vehicle(self):
        print(f'The vehicle make is: {self.set_vehicle_make()}\n'
              f'The vehicle model is: {self.set_vehicle_model()}')


class Car(Vehicle):
    def __init__(self, vehicle_make, vehicle_model, car_doors):
        self.car_doors = car_doors

    def get_car_doors(self):
        return self.car_doors

    def set_car_doors(self, car_doors):
        self.set_car_doors = car_doors

    def display_car(self):
        print(f'The vehicle make is: {self.set_vehicle_make}\n'
              f'The vehicle model is: {self.set_vehicle_model}\n'
              f'The number of doors is: {self.set_car_doors}')


class Truck(Vehicle):
    def __init__(self, vehicle_make, vehicle_model, bed_length):
        self.bed_length = bed_length

    def get_bed_length(self):
        return self.bed_length

    def set_bed_length(self, bed_length):
        self.set_bed_length = bed_length

    def display_truck(self):
        print(f'The vehicle make is: {self.set_vehicle_make}\n'
              f'The vehicle model is: {self.set_vehicle_model}\n'
              f'The length of the truck bed is: {self.set_bed_length}')


def car_function():
    input_make = input('Enter the make of the car:')
    input_model = input('Enter the model of the car:')
    input_doors = input('Enter the number of doors:')
    new_car = Car()
    new_car.set_vehicle_make(input_make)
    new_car.set_vehicle_model(input_model)
    new_car.set_car_doors(input_doors)
    new_car.display_car()


def truck_function():
    input_make = input('Enter the make of the truck:')
    input_model = input('Enter the model of the truck:')
    input_length = input('Enter the length of the bed:')
    new_truck = Truck()
    new_truck.set_vehicle_make(input_make)
    new_truck.set_vehicle_model(input_model)
    new_truck.set_bed_length(input_length)
    new_truck.display_truck()


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
        print('Goodbye!')

    else:
        print('***INVALID ENTRY***\n'
              'Please enter 1, 2, or 3')
        main()


main()
