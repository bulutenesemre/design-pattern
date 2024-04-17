from statistics_display import StatisticsDisplay
from weather_data import WeatherData


class WeatherStation:
    @staticmethod
    def main(*args):
        weatherData: WeatherData = WeatherData()
        statisticsDisplay: StatisticsDisplay = StatisticsDisplay(weatherData)

        weatherData.setMeasurements(80.0, 65.0, 30.4)
        weatherData.setMeasurements(82.0, 70.0, 29.2)
        weatherData.setMeasurements(78.0, 90.0, 29.2)

        weatherData.removeObserver(statisticsDisplay)
        weatherData.setMeasurements(62.0, 90.0, 28.1)


if __name__ == "__main__":
    WeatherStation.main()
