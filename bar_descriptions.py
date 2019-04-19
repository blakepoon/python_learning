import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
	{'value': 16101, 'label': 'Description of Httpie.'},
	{'value': 15028, 'label': 'Description of Django.'},
	{'value': 14798, 'label': 'Description of Flask.'},
	]

chart.add(' ', plot_dicts)
chart.render_to_file('bar_description.svg')