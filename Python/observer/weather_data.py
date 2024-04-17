from typing import List

from observer import Observer
from subject import Subject


class WeatherData(Subject):
    __observer: List[Observer]
    __temperature: float
    __humidity: float
    __pressure: float

    def __init__(self):
        self.__observer: List[Observer] = []

    def registerObserver(self, o: Observer) -> None:
        self.__observer.append(o)

    def removeObserver(self, o: Observer) -> None:
        self.__observer.remove(o)

    def notifyObserver(self) -> None:
        for observer in self.__observer:
            observer.update(self.__temperature, self.__humidity, self.__pressure)

    def measurementsChanged(self) -> None:
        self.notifyObserver()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementsChanged()

    def getTemperature(self) -> float:
        return self.__temperature

    def getHumidity(self) -> float:
        return self.__humidity

    def getPressure(self) -> float:
        return self.__pressure
