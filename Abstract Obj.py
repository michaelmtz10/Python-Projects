from abc import ABC, abstractmethod

class Computer(ABC):
    def storage(self, amount):
        print("the storage available is: ", amount)

        @abstractmethod
        def software(self, amount):
            pass


class ddr4(Computer):
    def calc(self, amount):
        print('THe storage amount of this computer is {}'.format(amount))

samsung = ddr4()
samsung.storage("250GB")
samsung.calc("250GB")


