
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
# Generate 50 simulated temperature readings
for i in range(50):
    temperature += random.uniform(-0.8, 0.8)
    temperature = max(22, min(35, temperature))
    temperatures.append(round(temperature, 2))
    timestamps.append(
        (start_time + timedelta(minutes=i * 10)).strftime("%Y-%m-%d %H:%M:%S")
    )
# Save readings to CSV file
with open("temperature_readings.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading Number", "Timestamp", "Temperature (Celsius)"])
    for i in range(50):
        writer.writerow([i + 1, timestamps[i], temperatures[i]])
print("50 temperature readings generated successfully!")
# Read temperature readings from CSV file
csv_temperatures = []
with open("temperature_readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        csv_temperatures.append(float(row["Temperature (Celsius)"]))
# Calculate temperature statistics
minimum = min(csv_temperatures)
maximum = max(csv_temperatures)
average = statistics.mean(csv_temperatures)
print("\nTEMPERATURE ANALYSIS")
print("----------------------------")
print("Minimum Temperature:", minimum, "°C")
print("Maximum Temperature:", maximum, "°C")
print("Average Temperature:", round(average, 2), "°C")
# Display temperature status
if average > 30:
    print("Status: High Temperature")
elif average < 25:
    print("Status: Low Temperature")
else:
    print("Status: Normal Temperature")
# Plot temperature graph
plt.figure(figsize=(10, 5))
plt.plot(range(1, 51), csv_temperatures, marker="o")
plt.title("COS 324 - IoT Temperature Monitoring System")
plt.xlabel("Reading Number")
plt.ylabel("Temperature (Celsius)")
plt.grid(True)
plt.savefig("temperature_analysis.png")
plt.show()
print("\nTemperature analysis completed successfully!")
