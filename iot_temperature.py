
import csv
import random
import statistics
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# COS 324 - IoT Temperature Monitoring System
# Name: JIMOH FAWAZ OKIKIOLA
# Matric Number: 252007CYB006

temperatures = []
timestamps = []
temperature = 28.0
start_time = datetime.now()

for i in range(50):
    temperature += random.uniform(-0.8, 0.8)
    temperature = max(22, min(35, temperature))
    temperatures.append(round(temperature, 2))
    timestamps.append(
        (start_time + timedelta(minutes=i*10)).strftime("%Y-%m-%d %H:%M:%S")
    )

with open("temperature_readings.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading Number", "Timestamp", "Temperature (Celsius)"])
    for i in range(50):
        writer.writerow([i+1, timestamps[i], temperatures[i]])

print("50 temperature readings generated successfully!")
