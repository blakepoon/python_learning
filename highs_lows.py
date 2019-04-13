import csv
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	highss = []
	lowss= []
	datess = []
	for row in reader:
		highss.append(int(row[1]))
		lowss.append(int(row[3]))

		datee = datetime.strptime(row[0], '%Y-%m-%d')
		datess.append(datee)

filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	highs = []
	lows = []
	dates = []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(date, 'missing data')
		else:
			highs.append(high)
			lows.append(low)
			dates.append(date)

fig = plt.figure(figsize=(10, 6))

plt.plot(datess, highss, c='blue', alpha=0.1, label='Sitka')
plt.plot(datess, lowss, c='blue', alpha=0.1)
plt.fill_between(datess, highss, lowss, facecolor='blue', alpha=0.5)


plt.plot(dates, highs, c='red', alpha=0.1, label='Death Valley')
plt.plot(dates, lows, c='red', alpha=0.1)
plt.fill_between(dates, highs, lows, facecolor='red', alpha=0.5)

plt.title('Daily High and Low Temperatures, 2014', fontsize=24)
plt.xlabel('')
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
fig.autofmt_xdate()
fig.legend(loc='center right', fontsize=12)

plt.show()











