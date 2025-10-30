total_rain = 0.0
total_wind = 0.0
day_count = 0

print("Enter rainfall (in inches) and wind speed (in mph) separated by a space, one day per line. "
      "End input with a line containing -1.0 for rainfall.\n")


lines = []
line = input()
while line.strip() != "-1.0":
    lines.append(line)
    line = input()

for line in lines:
    parts = line.strip().split()

    if len(parts) != 2:
        continue

    rain = float(parts[0])
    wind = float(parts[1])

    total_rain += rain
    total_wind += wind
    day_count += 1

if day_count > 0:
    avg_rain = total_rain / day_count
    avg_wind = total_wind / day_count
    severity = (avg_rain * 10) + avg_wind

    print(f"\nThe average rain is {avg_rain:.1f} inches")
    print(f"The average wind is {avg_wind:.1f} mph")
    print(f"The weather severity for these {day_count} readings is: {severity:.1f}")
else:
    print("No data entered.")
