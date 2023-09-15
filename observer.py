from abc import abstractmethod
from time import sleep


class WeatherData():
    def __init__(self, list_subscribers) -> None:
        self.list_subscribers = list_subscribers
        self.temperature = None
        self.humidity = None

    def notify(self):
        for subscriber in self.list_subscribers:
            subscriber.update(self)
        print()

    def new_data(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify()

class Observer():
    @abstractmethod
    def update(self, weather_data):
        pass

class DisplayObserver(Observer):
    def update(self, weather_data):
        print("Temperatura atual:", weather_data.temperature)
        print("Umidade atual:", weather_data.humidity)

class Statistics(Observer):
    def __init__(self) -> None:
        self.list_temperature = []

    def update(self, weather_data):
        self.list_temperature.append(weather_data.temperature)
        if len(self.list_temperature) >= 3:
            avg_temp = sum(self.list_temperature)/len(self.list_temperature)
            print("Temperatura média:", avg_temp)

display = DisplayObserver()
stats = Statistics()
data = WeatherData([display, stats])
sleep(2)
data.new_data(30, 20)
sleep(2)
data.new_data(20, 50)
sleep(2)
data.new_data(25, 70)
sleep(2)
data.list_subscribers.pop(0)
data.new_data(30,30)


