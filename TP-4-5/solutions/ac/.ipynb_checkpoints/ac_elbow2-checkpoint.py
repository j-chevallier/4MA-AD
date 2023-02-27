n_sizes = 10
x = np.arange(n_sizes, 1, -1)
y = ac.distances_[-n_sizes:-1]

plt.scatter(x, y)
plt.show()