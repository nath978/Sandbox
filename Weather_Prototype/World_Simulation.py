# Simulates the world environment, from which data is collected by the weather_station

import datetime
import time

class World_Simulation:

    def __init__(self, weather_types = ["Raining", "Sunny", "Snowing", "Storming"], wind_speed_kmh = 1, air_pressure= 0, sunshine_gauge = 0, visibility_gauge = 0, precipitation_gauge = 0, ground_temperature = 12, air_temperature = 8):
        """ Initializes class parameters"""
        self.weather_types = weather_types
        self.wind_speed_kmh = wind_speed_kmh
        self.air_pressure = air_pressure
        self.sunshine_gauge = sunshine_gauge
        self.visibility_gauge = visibility_gauge
        self.precipitation_gauge = precipitation_gauge
        self.ground_temperature = ground_temperature
        self.air_temperature = air_temperature
        self.current_time = datetime.datetime.now().time().isoformat(timespec = "minutes")
        self.season_types = ["Spring", "Summer", "Autumn", "Winter"]
        self.current_month = datetime.datetime.now().date().month
        self.current_season = self.season_types[3]


    def __str__(self):
        """The string produced when print(World_Simulation) is called"""
        return

    def simulate_seasons(self):
        if  9 <= self.current_month <= 11:
            self.current_season = self.season_types[0]
        elif 3 <= self.current_month <= 5:
            self.current_season = self.season_types[2]
        elif 6 <= self.current_month <= 8:
            self.current_season = self.season_types[3]
        else:
            self.current_season = self.season_types[1]

    def simulate_wind(self):
        if self.current_season == "Spring":
            self.wind_speed_kmh = 20
        elif self.current_season == "Summer":
            self.wind_speed_kmh = 10
        elif self.current_season == "Autumn":
            self.wind_speed_kmh = 25
        else:
            self.wind_speed_kmh = 15

    def simulate_sunshine(self):
        if self.current_season == "Spring":
            self.sunshine_gauge = 20
        elif self.current_season == "Summer":
            self.sunshine_gauge = 10
        elif self.current_season == "Autumn":
            self.sunshine_gauge = 25
        else:
            self.sunshine_gauge = 15

    def update_simulation(self):
        self.simulate_seasons()
        self.simulate_wind()
        time.sleep(1800)