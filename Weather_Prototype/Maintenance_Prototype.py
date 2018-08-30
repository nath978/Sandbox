#This system can communicate by satellite with all
#wilderness weather stations to monitor the health of these systems and provide
#reports of problems. It can update the embedded software in these systems. In the
#event of system problems, this system can also be used to remotely control a
#wilderness weather system.

import datetime
import time

class maintenance:

    def __init__(self, battery = 100,max_battery = 100,battery_charge_rate = 1, battery_use_rate = 0.4, station_state = "Fully Operational", is_generator_active = True, damage = 0, damage_state = "Ok", battery_state = "Ok", connection_state = "Connected", system_operation_rating = 100):
        """ Initializes class parameters"""
        self.battery = battery
        self.max_battery = max_battery
        self.battery_charge_rate = battery_charge_rate
        self.battery_use_rate = battery_use_rate
        self.is_generator_active = is_generator_active
        self.damage = damage
        self.system_operation_rating = system_operation_rating
        self.damage_state = damage_state
        self.battery_state = battery_state
        self.connection_state = connection_state
        self.station_state = station_state
        self.current_time = datetime.datetime.now().time().isoformat(timespec = "minutes")

    def __str__(self):
        """The string produced when print(maintenance) is called"""
        return "Remaining Battery:  {} \n Station State: {} \n Generator Active: {} ".format(self.battery, self.station_state, self.is_generator_active)

    def battery_simulate(self):
        hour, minute = self.current_time.split(":")
        if (7 < int(hour) < 18):
            self.battery += self.battery_charge_rate - self.battery_discharge_rate
            print("battery increasing")
        else:
            self.battery -= self.battery_discharge_rate
            print("battery decreasing")

        print("battery: {}".format(int(self.battery)))
        time.sleep(60)
        return self.battery

    def battery_check(self):
        if self.battery <= 10:
            self.battery_state = "Low Battery"
            self.system_operation_rating -= 10
        elif self.battery <= 0:
            self.is_generator_active = False
            self.system_operation_rating = 0
            self.battery_state = "Battery Inactive"


    def damage_check(self):
        if self.damage > 50:
            self.damage_state = "System Physically Damaged"
            self.battery_charge_rate /= 2
            self.system_operation_rating -= 20

    def station_check(self):
        if self.system_operation_rating == 100:
            self.station_state = "Fully Operational"
        elif self.system_operation_rating <= 75:
            self.station_state = "Slight Damaged"
        elif self.system_operation_rating <= 50:
            self.station_state = "Damaged"
        elif self.system_operation_rating <= 20:
            self.station_state = "Severly Damaged"
        elif self.system_operation_rating <= 0:
            self.station_state = "Inactive"
        return self.station_state

    def update_status(self):
        self.current_time = datetime.datetime.now().time().isoformat(timespec = "minutes")
        self.battery_simulate()
        self.damage_check()
        self.battery_check()
        print(self.station_state)
