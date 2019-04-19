import pygal
import math
import json
from itertools import groupby

filename = 'btc_close_2017.json'
with open(filename) as f:
	btc_data = json.load(f)

#global dates, months, weeks, weekdays, close
dates, months, weeks, weekdays, close = [], [], [], [], []

for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))

def draw_line(dates, close):
	line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
	line_chart.title = 'Close Price ($)'
	line_chart.x_labels = dates
	line_chart.x_labels_major = dates[::20]
	line_chart.add('Close Price', close)
	line_chart.render_to_file('Close Price.svg')
	return line_chart

def draw_logline(dates, close):
	line_chart_log = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
	line_chart_log.title = 'Close Price in Semi-logarithmic ($)'
	line_chart_log.x_labels = dates
	line_chart_log.x_labels_major = dates[::20]
	close_log = [math.log10(value) for value in close]
	line_chart_log.add('Close Price in Log', close_log)
	line_chart_log.render_to_file('Close Price in Log.svg')
	return line_chart_log

def draw_avgline(x_data, y_data, title, y_legend):
	xy_map = []
	for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
		y_list = [v for _, v in y]
		xy_map.append([x, sum(y_list) / len(y_list)])
	x, y = [*zip(*xy_map)]
	x_unique, y_mean = [], []
	for a in x:
		x_unique.append(str(a))
	for b in y:
		y_mean.append(b)
	line_chart = pygal.Line(show_minor_x_labels=False)
	line_chart.width = 1000
	line_chart.title = title
	line_chart.x_labels = x_unique
	if len(x_unique) > 20:
		line_chart.x_labels_major = x_unique[::2]
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart

idx_month = dates.index('2017-12-01')
idx_week = dates.index('2017-12-11')
idx_weekday = dates.index('2017-12-11')

wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
wd_int = [wd.index(w) + 1 for w in weekdays[1:idx_weekday]]

line_chart = draw_line(dates, close)

line_chart_log = draw_logline(dates, close)

line_chart_month = draw_avgline(months[:idx_month], close[:idx_month], 
	'Average Close Price per Month', 'Avg Price/month')

line_chart_week = draw_avgline(weeks[1:idx_week], close[1:idx_week], 
	'Average Close Price per Week', 'Avg Price/week')

Line_chart_weekday = draw_avgline(wd_int, close[1:idx_weekday], 
	'Average Close Price per Weekday', 'Avg Price/weekday')

with open('Dashboard.html', 'w', encoding='utf8') as html_file:
	html_file.write('<html><head><title>Dashboard</title><metacharset="utf-8"></head><body>\n')
	for svg in [
			'Close Price.svg', 'Close Price in Log.svg', 'Average Close Price per Month.svg',
			'Average Close Price per Week.svg', 'Average Close Price per Weekday.svg'
	]:
		html_file.write('	<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
	html_file.write('</body></html>')

