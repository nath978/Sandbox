import datetime
import time

# battery = 100
# battery_discharge_rate = 0.4
# battery_charge_rate = 1
# battery_change_duration = 1
# current_time = datetime.datetime.now().time().isoformat(timespec="minutes")
# hour,minute = current_time.split(":")
#
# def timeout(battery):
#     # timeout
#     if (7 < int(hour) < 18):
#         battery += battery_charge_rate - battery_discharge_rate
#         print("battery increasing")
#     else:
#         battery -= battery_discharge_rate
#         print("battery decreasing")
#
#     print("battery: {}".format(int(battery)))
#     time.sleep(battery_change_duration)
#     return battery
#
# while True:
#     battery = timeout(battery)
#     print("Current Time: {}".format(current_time))

current_date = datetime.datetime.now().date().month
print(current_date)