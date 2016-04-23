

class Vehicle:

    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print ('The {} {} goes VROOOM!'.format(
                self.color, self.manuf)
        else:
            print ('The {} {} sputters out of gas '.format(
                self.color, self.manuf


class Car(Vehicle):

    def radio(self):
        print('rockin tunes')


class Motorcycle(Vehicle):

        def helment(self):
            print('nice and safe')
