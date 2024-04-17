package observer

import (
	"fmt"
)

type Observer interface {
	Update(temp, humidity, pressure float64)
}

type CurrentConditionDisplay struct {
	temperature, humidity float64
}

func NewCurrentConditionDisplay() *CurrentConditionDisplay {
	return &CurrentConditionDisplay{}
}

func (ccd *CurrentConditionDisplay) Update(temp, humidity, pressure float64) {
	ccd.temperature = temp
	ccd.humidity = humidity
	ccd.Display()
}

func (ccd *CurrentConditionDisplay) Display() {
	fmt.Printf("Current conditions: %.2f F temperature and %.2f%% humidity \n", ccd.temperature, ccd.humidity)
}

type StatisticsDisplay struct {
	minTemp, maxTemp, avgTemp float64
	temperatureCount int
}

func NewStatisticsDisplay() *StatisticsDisplay {
	return &StatisticsDisplay{}
}

func (sd *StatisticsDisplay) Update(temp, humidity, pressure float64) {
	if sd.temperatureCount == 0 {
		sd.minTemp = temp
		sd.maxTemp = temp
		sd.avgTemp = temp
	} else {
		if temp < sd.minTemp {
			sd.minTemp = temp
		}
		if temp > sd.maxTemp {
			sd.maxTemp = temp
		}
		sd.avgTemp = (sd.avgTemp* float64(sd.temperatureCount) + temp) / float64(sd.temperatureCount+1)
	}

	sd.temperatureCount++
	sd.Display()
}

func (sd *StatisticsDisplay) Display() {
	fmt.Printf("Temperature statistics: Min %.2f F, Max %.2f F, Avg %.2f F\n", sd.minTemp, sd.maxTemp, sd.avgTemp)
}