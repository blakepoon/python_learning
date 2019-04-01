import matplotlib.pyplot as plt


x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, s=10, edgecolor='none', c=y_value, cmap=plt.cm.Reds)
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=24)
plt.ylabel('Square of Value', fontsize=24)
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis='both', labelsize=24, which='major')

#plt.show()
plt.savefig('square_plot.png', bbox_inches='tight')