import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [x ** 2 for x in x_value]

fig, ax = plt.subplots()
ax.scatter(x_value, y_value, s=10)
# plt.show()

plt.savefig('squares_plt.png')
