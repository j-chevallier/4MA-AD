sample = mars_data[::1000]
x = np.arange(0, 255)

for i in range(sample.shape[0]):
    plt.plot(x, sample[i, :])
     
plt.title("Spectrum of the first %i pixels" % sample.shape[0])
plt.xlabel("Wave length")
plt.ylabel("Measured value")
plt.show()