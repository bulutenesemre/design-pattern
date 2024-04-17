from display_element import DisplayElement
from observer import Observer
from weather_data import WeatherData


class CurrentConditionDisplay(Observer, DisplayElement):
    __temperature: float
    __humidity: float
    __weatherData: WeatherData

    def __init__(self, weatherData: WeatherData):
        self.__weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.display()

    def display(self) -> None:
        print(f"Current conditions: {self.__temperature}F degrees and {self.__humidity}% humidity")
