class IllegalCarError(Exception):
    pass

class Car:
    def __init__(self, pax_count, mass, gear_count):
        if pax_count < 1 or pax_count > 5 :
            raise IllegalCarError('illegal number of passengers!')
        if mass > 2000:
            raise IllegalCarError('Your car is too heavy')
        self.pax_count = pax_count
        self.mass = mass
        self.gear_count = gear_count

    def total_mass(self):
        """calculating total car mass"""
        return self.mass + self.pax_count * 70

