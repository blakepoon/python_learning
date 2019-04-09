import pygal
from die import Die

die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
	results.append(die_1.roll() + die_2.roll())

frequencies = []
for value in range(2, die_1.num_sides+die_2.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')