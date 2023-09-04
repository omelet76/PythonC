class Car:
    def __init__(self, make=None, model=None, year=None):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year}{self.make}{self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def updata_odometer(self, miles=None):
        if miles > self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('You can not roll back')

    def increment_odometer(self, miles=None):
        self.odometer_reading += miles


class Electricar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self, battery_size=75):

        self.battery_size = battery_size


    def descibe_size(self):
        print(f'this car has a {self.battery_size}-kwh battery')


    def getrange(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} miles')
