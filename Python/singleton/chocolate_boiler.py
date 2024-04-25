class ChocolateBoiler:
    __empty: bool
    __boiled: bool
    __uniqueInstance = None

    def __init__(self):
        self.__empty = True
        self.__boiled = False

    @staticmethod
    def getinstance():
        if ChocolateBoiler.__uniqueInstance is None:
            print("Creating unique instance of Chocolate Boiler")
            ChocolateBoiler.__uniqueInstance = ChocolateBoiler()
        print("Returning instance of Chocolate Boiler")
        return ChocolateBoiler.__uniqueInstance

    def fill(self) -> None:
        if self.isEmpty():
            self.__empty = False
            self.__boiled = False

    def drain(self) -> None:
        if not self.isEmpty() and not self.isEmpty():
            self.__empty = True

    def boil(self) -> None:
        if not self.isEmpty() and not self.isBoiled():
            self.__boiled = True

    def isEmpty(self) -> bool:
        return self.__empty

    def isBoiled(self) -> bool:
        return self.__boiled

