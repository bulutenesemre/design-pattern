from chocolate_boiler import ChocolateBoiler


class ChocolateController:
    @staticmethod
    def main(*args) -> None:
        boiler: ChocolateBoiler = ChocolateBoiler.getinstance()

        boiler.fill()
        boiler.boil()
        boiler.drain()

        boiler2: ChocolateBoiler = ChocolateBoiler.getinstance()


if __name__ == "__main__":
    ChocolateController.main()
