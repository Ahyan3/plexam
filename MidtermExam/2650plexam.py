import numpy as np

# Instructions for the user
print("Weather Data Analysis for 30 Days")
print("=================================")
print("Instructions:")
print("- You will input the temperature (in Celsius) for each of 30 days.")
print("- Enter a number for each day (e.g., 25.5, -3, 18).")
print("- Use decimal points if needed (e.g., 22.7).")
print("- Press Enter after each input.")
print("\nOutcome:")
print("- The program will convert temperatures to Fahrenheit.")
print("- It will calculate the average temperature for the month.")
print("- It will find the hottest and coldest days.")
print("- It will count how many days were above the monthly average.")
print("=================================\n")

# Collect 30 days of temperatures
temperatures_celsius = []
for day in range(1, 31):
    while True:
        try:
            temp = float(input(f"Enter temperature for Day {day} (in Celsius): "))
            temperatures_celsius.append(temp)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 25.5, -3).")

# Convert list to NumPy array
temperatures_celsius = np.array(temperatures_celsius)

# Step 1: Display temperatures in Celsius
print("\nDaily Temperatures (Celsius):", temperatures_celsius)

# Step 2: Convert to Fahrenheit
temperatures_fahrenheit = (temperatures_celsius * 9/5) + 32
print("Daily Temperatures (Fahrenheit):", temperatures_fahrenheit)

# Step 3: Calculate average temperature
average_temp_celsius = np.mean(temperatures_celsius)
average_temp_fahrenheit = np.mean(temperatures_fahrenheit)
print(f"\nAverage Temperature: {average_temp_celsius:.2f}°C / {average_temp_fahrenheit:.2f}°F")

# Step 4: Find hottest and coldest days
hottest_temp_celsius = np.max(temperatures_celsius)
coldest_temp_celsius = np.min(temperatures_celsius)
hottest_temp_fahrenheit = np.max(temperatures_fahrenheit)
coldest_temp_fahrenheit = np.min(temperatures_fahrenheit)
print(f"Hottest Day Temperature: {hottest_temp_celsius:.2f}°C / {hottest_temp_fahrenheit:.2f}°F")
print(f"Coldest Day Temperature: {coldest_temp_celsius:.2f}°C / {coldest_temp_fahrenheit:.2f}°F")

# Step 5: Count days above average
days_above_average = np.sum(temperatures_celsius > average_temp_celsius)
print(f"Days Above Average Temperature: {days_above_average}")